import pygame
import math

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

pygame.init()
font = pygame.font.Font(None, 24)


class ContextMenu:
    def __init__(self, x, y, options):
        self.x = x
        self.y = y
        self.options = options
        self.selected_option = None
        self.width = 120
        self.height = len(options) * 30

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
        for i, option in enumerate(self.options):
            text = font.render(option, True, BLACK)
            screen.blit(text, (self.x + 10, self.y + 5 + i * 30))

    def handle_click(self, pos):
        if self.contains_point(pos):
            index = (pos[1] - self.y) // 30
            if 0 <= index < len(self.options):
                self.selected_option = self.options[index]
                return self.selected_option
        return None

    def contains_point(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


class Box:
    def __init__(self, x, y, size=50, color=RED):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 0
        self.acceleration = 0.2
        self.max_speed = 2
        self.slow_down_distance = 50
        self.goal = None
        self.selected = False
        self.rect = pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)
        self.desired_velocity = [0, 0]
        self.offset_position = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(screen, GREEN, self.rect, 3)
        if self.goal:
            pygame.draw.circle(screen, BLUE, self.goal, 5)
        if self.offset_position:
            pygame.draw.circle(screen, (255, 255, 0), self.offset_position, 3)

    def set_selected(self, selected):
        self.selected = selected

    def contains_point(self, pos):
        return self.rect.collidepoint(pos)

    def calculate_desired_velocity(self):
         if self.offset_position:
            dx = self.offset_position[0] - self.x
            dy = self.offset_position[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 0:
                self.desired_velocity = [dx / distance * self.max_speed, dy / distance * self.max_speed]
            else:
                self.desired_velocity = [0, 0]
         elif self.goal:
            dx = self.goal[0] - self.x
            dy = self.goal[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 0:
                self.desired_velocity = [dx / distance * self.max_speed, dy / distance * self.max_speed]
            else:
                self.desired_velocity = [0, 0]

    def update_position(self, speed, all_boxes):
        if self.offset_position:
            dx = self.offset_position[0] - self.x
            dy = self.offset_position[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < speed:
                self.x = self.offset_position[0]
                self.y = self.offset_position[1]
                self.offset_position = None
                self.goal = None
                self.speed = 0
            else:
                 self.x += self.desired_velocity[0] * speed
                 self.y += self.desired_velocity[1] * speed
                 # Update the box's rectangle position
                 self.rect.topleft = (self.x - self.size // 2, self.y - self.size // 2)

        elif self.goal:
            dx = self.goal[0] - self.x
            dy = self.goal[1] - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < speed:  # Stop when close to the goal
                self.x, self.y = self.goal
                self.goal = None
                self.speed = 0
            else:
                self.x += self.desired_velocity[0] * speed
                self.y += self.desired_velocity[1] * speed
                # Update the box's rectangle position
                self.rect.topleft = (self.x - self.size // 2, self.y - self.size // 2)

def velocity_obstacle(box1, all_boxes, r):
    """
    Checks if two vehicles are in a potential collision and adjusts velocity.
    :param box1: Box object
     :param all_boxes: List of other boxes (position, velocity)
    :param r: Combined collision radius
    :return: Adjusted velocity for Vehicle 1
    """

    pos1 = [box1.x,box1.y]
    vel1 = box1.desired_velocity

    adjusted_vel = vel1
    for box2 in all_boxes:
        if box1 != box2: #skip the check with itself
            pos2 = [box2.x, box2.y]
            vel2 = box2.desired_velocity
            # Calculate relative position and velocity
            p_rel = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
            v_rel = [vel2[0] - vel1[0], vel2[1] - vel1[1]]

            # Distance between vehicles
            dist = math.sqrt(p_rel[0] ** 2 + p_rel[1] ** 2)

            # Check if vehicles are too close
            if dist < r:
                # Time to closest point of approach (CPA)
                t_cpa = -(p_rel[0] * v_rel[0] + p_rel[1] * v_rel[1]) / (v_rel[0] ** 2 + v_rel[1] ** 2 + 1e-5)

                # If moving toward each other
                if t_cpa > 0:
                    # Adjust velocity to steer outside collision cone
                    angle = math.atan2(p_rel[1], p_rel[0])  # Angle to the other vehicle
                    avoidance_angle = angle + math.pi / 2  # Perpendicular direction
                    adjusted_vel = [math.cos(avoidance_angle) * 3, math.sin(avoidance_angle) * 3]  # Adjust speed
                    return adjusted_vel
    return adjusted_vel


class Scene:
    def __init__(self, width, height, color=WHITE):
        self.width = width
        self.height = height
        self.color = color
        self.boxes = []
        self.context_menu = None
        self.movement_active = False
        self.goal_queue = [] # Queue of goals

    def draw(self, screen):
        screen.fill(self.color)
        for box in self.boxes:
            box.draw(screen)

        if self.context_menu:
            self.context_menu.draw(screen)

    def show_context_menu(self, pos, options):
        self.context_menu = ContextMenu(pos[0], pos[1], options)

    def handle_context_selection(self, selected_option):
        if selected_option == "Create Box":
            self.boxes.append(
                Box(self.context_menu.x + self.context_menu.width // 2,
                    self.context_menu.y + self.context_menu.height // 2))

        elif selected_option == "Delete Box":
            for box in self.boxes:
                if box.contains_point((self.context_menu.x, self.context_menu.y)):
                    self.boxes.remove(box)
                    break

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left-click for selection
                if self.context_menu and not self.context_menu.contains_point(event.pos):
                    self.context_menu = None
                elif self.context_menu:
                    selected_option = self.context_menu.handle_click(event.pos)
                    if selected_option:
                        self.handle_context_selection(selected_option)
                        self.context_menu = None
                else:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:  # Multi-select
                        for box in self.boxes:
                            if box.contains_point(event.pos):
                                box.set_selected(not box.selected)
                                return
                    else:  # Single-select
                        for box in self.boxes:
                            box.set_selected(False)
                        for box in self.boxes:
                            if box.contains_point(event.pos):
                                box.set_selected(True)
                                return

            elif event.button == 3:  # Right-click
                selected_boxes = [box for box in self.boxes if box.selected]
                if selected_boxes:  # If any box is selected, assign a goal
                    goal = event.pos
                    if goal not in self.goal_queue:
                        self.goal_queue.append(goal)
                    for box in selected_boxes:
                        box.goal = goal
                    self.context_menu = None  # Ensure the context menu does not show
                else:  # No box selected, show the context menu
                    for box in self.boxes:
                        if box.contains_point(event.pos):
                            self.show_context_menu(event.pos, ["Delete Box"])
                            return
                    self.show_context_menu(event.pos, ["Create Box"])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # Press 'm' to start movement
                self.movement_active = True

    def update_boxes(self):
      if self.movement_active:
          all_stopped = True

          # 1. Calculate desired velocities for all boxes
          for box in self.boxes:
              if box.goal:
                box.calculate_desired_velocity()

          # 2. Apply VO to all boxes and update velocities:
          for box in self.boxes:
              other_boxes = [other for other in self.boxes if other != box and other.goal is not None]
              adjusted_vel = velocity_obstacle(box, other_boxes, box.size * 2)
              box.desired_velocity = adjusted_vel

          # 3. Update position of all the boxes
          for box in self.boxes:
            if box.goal:
                box.update_position(2,self.boxes)
                all_stopped = False

          # 4. Handle goal completion
          for box in self.boxes:
              if box.goal is None and box.selected:
                box.set_selected(False)
              if box.goal is None and box.selected is False:
                 for goal in self.goal_queue:
                    if (box.x, box.y) == goal:
                       self.goal_queue.remove(goal)
                       break

          if all_stopped:
            for box in self.boxes:
              if box.goal:
                all_stopped = False
                break
          if all_stopped:
             self.movement_active = False

def main():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Context Menu with Movement")

    scene = Scene(screen_width, screen_height)
    #Need to create a different file graphics manager and import that (screen width, scrren height, everything)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            scene.handle_event(event)

        # Update boxes if movement is active
        scene.update_boxes()

        scene.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
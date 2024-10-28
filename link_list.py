#Single link List
class linkList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


#creating nodes
head = linkList(1)
head.next = linkList(2)
head.next.next = linkList(3)
head.next.next.next = linkList(4)


#traversing and printing all the node in list
def print_list(head):
    curr = head
    if curr:
        while curr:
            print(f"{curr.value}", end=" ")
            curr = curr.next
        print()


print_list(head)


#Reversing the list
def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

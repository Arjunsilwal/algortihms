#Binary Tree
class BinaryTree:
    def __init__(self, value, left =None, right = None):
        self.value = value
        self.left = left
        self.right = right


#preorder using stack iterative approach
def pre_order_iterative(root):
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

#postorder using stack iterative approach

def post_order_iterative(root):
    #left,right,root

    stack = [node]

    while stack:
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()
        print(node)
#checking binary tree is balanced or not? 110
def isBalanced(root):
        def traverse(node):
            if not node:
                return [True, 0]
            left = traverse(node.left)
            right = traverse(node.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return traverse(root)[0]
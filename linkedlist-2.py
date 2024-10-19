#double linked list
class doublelisnkedlist:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


head = tail = doublelisnkedlist(1)


#display the elements of the double linked list
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(elements)


display(head)


#insert element at the start of double linked list - O(1)
def insert_start(head, tail, value):
    new_node = doublelisnkedlist(value, next=head)
    head.prev = new_node
    return new_node, tail


head, tail = insert_start(head, tail, 3)
display(head)


#insert element at the end of double linked list - O(1)
def insert_end(head, tail, value):
    new_node = doublelisnkedlist(value, prev=tail)
    tail.next = new_node
    return tail, new_node


tail, new_node = insert_end(head, tail, 4)
display(head)

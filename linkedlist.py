#create a single linked list

class singlelinkedlist:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


Head = singlelinkedlist(1)
A = singlelinkedlist(3)
B = singlelinkedlist(5)
C = singlelinkedlist(6)

Head.next = A
A.next = B
B.next = C

print(Head)


#Traverse through the list to display all the elements O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(curr.value)
        curr = curr.next
    print(elements)


display(Head)


#find the specific node in linked list
def search(head, value):
    curr = head
    while curr:
        if value == curr.value:
            return True
        curr = curr.next
    return False


search(Head, 1)

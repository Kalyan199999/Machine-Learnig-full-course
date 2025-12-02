# define the single linkedlist
class SingleLinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

# double linked list
class DoubleLinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


# display the list
def display(head:SingleLinkedList) ->None:
    temp = head
    while(temp != None):
        print(temp.data,end=" ")
        temp = temp.next
    print()

def dsiplayFromBegin(head:DoubleLinkedList):
    temp = head
    while( temp.next != head):
        print(temp.data,end=" ")
        temp = temp.next
    print(temp.data)

def displayFromEnd(head:DoubleLinkedList):

    temp = head

    while( temp.prev != head):
        print(temp.data,end=" ")
        temp = temp.prev
    print(temp.data)
from LinkedLists import DoubleLinkedList,dsiplayFromBegin,displayFromEnd

if __name__ == "__main__":
    arr = [6,1,9,2,5,2,1,2]
    head = None
    tail = None

    for ele in arr:
        node = DoubleLinkedList(ele)
        if head is None:
            head = node
            tail = node
        else:
           node.prev = tail
           node.next = head
           head.prev = node
           tail.next = node
           tail = node
           
    print(arr)
    dsiplayFromBegin(head)
    displayFromEnd(tail)

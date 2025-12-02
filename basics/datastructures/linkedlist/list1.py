from LinkedLists import SingleLinkedList , display


if __name__ == "__main__":
    arr = [6,1,9,2,5,2,1,2]

    head = None
    tail = None

    for ele in arr:
        node = SingleLinkedList(ele)

        if( head == None):
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    print(arr)

    display(head)
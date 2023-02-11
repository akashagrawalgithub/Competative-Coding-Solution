class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def printlist(head):
    curr = head
    while(curr != None):
        print(curr.data)
        curr = curr.next


def insertatpositionspecific(head, key, position):
    temp = Node(key)
    if position == 1:
        temp.next = head
        return temp
    else:
        curr = head
        for i in range(position-2):
            curr = curr.next
            if curr == None:
                return head
        temp.next = curr.next
        curr.next = temp
        return head


def insertatbegin(head, key):
    temp = Node(key)
    temp.next = head
    head = temp
    return temp


def insertlast(head, key):
    curr = head
    temp = Node(key)
    while(curr.next != None):
        curr = curr.next
    curr.next = temp
    return head


def insertAtPositionAfter(head, pos, data):
    temp = Node(data)
    curr = head
    index = 1
    while curr != None:
        if (pos == index):
            temp.next = curr.next
            curr.next = temp
            break
        index += 1
        curr = curr.next
    return head


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp4 = Node(40)
temp5 = Node(50)
head = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
temp4.next = temp5
head = insertAtPositionAfter(head, 1, 1)
printlist(head)

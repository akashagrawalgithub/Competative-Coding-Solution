class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def printlist(head):
    curr = head
    while(curr != None):
        print(curr.data)
        curr = curr.next


def insertbegin(head, key):
    temp = Node(key)
    temp.next = head
    head = temp
    return head


def insertatlast(head, key):
    curr = head
    while(curr.next != None):
        curr = curr.next
    curr.next = Node(key)


def insertmiddle(head, key):
    curr = head
    count = 0
    while(curr != None):
        count += 1
        curr = curr.next
    curr = head
    if count == 0:
        head = Node(key)
    else:
        temp = Node(key)
        if count % 2 == 0:
            length = count/2
        else:
            length = (count+1)/2
        while(length > 1):
            length -= 1
            curr = curr.next
        temp.next = curr.next
        curr.next = temp


def insertatposition(head, key, position):
    temp = Node(key)
    if position == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(position-2):
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head


temp1 = Node(5)
temp2 = Node(6)
temp3 = Node(7)

head = temp1
temp1.next = temp2
temp2.next = temp3
head = insertatposition(head, "position", 1)
printlist(head)

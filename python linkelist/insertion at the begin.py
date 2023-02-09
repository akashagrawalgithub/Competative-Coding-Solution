class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def printlist(head):
    curr = head
    while(curr != None):
        print(curr.data)
        curr = curr.next


def insertatstart(head, key):
    temp = Node(key)
    temp.next = head
    return temp


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head = temp1
temp1.next = temp2
temp2.next = temp3


print("Initial Linkedlist")
printlist(head)
print("Linkedlist after inserting at the start")
head = insertatstart(head, 5)
printlist(head)
print("Linkedlist after inserting at the start")
head = insertatstart(head, 1)
printlist(head)

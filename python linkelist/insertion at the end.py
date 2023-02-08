class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def printlist(head):
    curr = head
    while(curr != None):
        print(curr.data)
        curr = curr.next


def insertlast(head, key):
    curr = head
    while(curr.next != None):
        curr = curr.next
    curr.next = Node(key)
    printlist(head)


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

head = temp1
temp1.next = temp2
temp2.next = temp3
print("Before Inserting")
printlist(head)
print("After inserting")
insertlast(head, 40)
print("After 2nd inserting")
insertlast(head, 50)

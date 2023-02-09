class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def printlist(head):
    if(head == None):
        print("empty linked list")
        print()
    else:
        curr = head
        while(curr != None):
            print(curr.data)
            curr = curr.next


def insertatfirst(head, key):
    temp = Node(key)
    temp.next = head
    head = temp
    return head


def insertatlast(head, key):
    curr = head
    while(curr.next != None):
        curr = curr.next
    curr.next = Node(key)


def insertinthemiddle(head, key):
    if(head == None):
        head = Node(key)
    else:
        temp = Node(key)
        curr = head
        count = 0
        while(curr != None):
            count += 1
            curr = curr.next
        curr = head
        if(count % 2 == 0):
            length = count/2
        else:
            length = (count+1)/2
        while(length > 1):
            length -= 1
            curr = curr.next
        temp.next = curr.next
        curr.next = temp


temp1 = Node(1)
temp2 = Node(2)
temp3 = Node(3)

head = None
# temp1.next=temp2
# temp2.next=temp3
print("Initial List")
printlist(head)
print("Insertion at the begin")
head = insertatfirst(head, 10)
printlist(head)
print("Insertion at the last")
insertatlast(head, 20)
printlist(head)
print("Insertion at the middle")
insertinthemiddle(head, 15)
printlist(head)

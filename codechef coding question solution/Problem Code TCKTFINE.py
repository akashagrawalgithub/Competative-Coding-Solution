#problem 
# Problem Code:TCKTFINE
# On a certain train, Chef-the ticket collector, collects a fine of Rs. XX if a passenger is travelling without a ticket. It is known that a passenger carries either a single ticket or no ticket.

# PP passengers are travelling and they have a total of QQ tickets. Help Chef calculate the total fine collected.


#solution

tc=int(input())
while(tc):
    A1,A2,A3=map(int,input().split(" "))
    x=A2-A3
    ans=A1*x
    print(ans)
    tc-=1
#question 
#https://www.codechef.com/problems/ACTEMP
#problems code :- ACTEMP
#Contest Code:- Practice

# Alice wants the air conditioner to be set to at least AA degrees, Bob wants it to be set to at most BB degrees, and Charlie wants it to be set to at least CC degrees.

# Is there a temperature that satisfies all three?


#solution
tc = int(input())
while(tc):
    a,b,c = map(int,input().split(" "))
    if a<=b and c<=b:
        print("yes")
    else:
        print("no")
    tc= tc -1 


#expalnation :-
# The code is doing the following:
# 1. It takes the input of three numbers a,b,c.
# 2. If a<=b and c<=b then it prints "yes" otherwise it prints "no".
# 3. The code runs for all the test cases.
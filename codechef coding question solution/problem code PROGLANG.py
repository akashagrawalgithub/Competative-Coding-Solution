#Question 
#problems code :- PROGLANG
#Contest Code:- Practice

# Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

#solution

tc = int(input())
while(tc):
    A,B,A1,B1,A2,B2 = map(int,input().split(" "))
    count=0
    if A1==A or A1==B:
        if B1==A or B1==B:
            count=1
        else:
            count=0
    elif A2==A or A2 == B:
        if B2==B or B2 ==A:
            count=2
        else:
            count=0
    print(count)
    tc-=1

#expalnation :-
# The code is doing the following:
# 1. If A1 is equal to A or B, then check if B1 is equal to A or B. If yes, then count=1. Else count=0.
# 2. If A2 is equal to A or B, then check if B2 is equal to A or B. If yes, then count=2. Else count=0.
# 3. If A1 and A2 are not equal to A or B, then check if B1 and B2 are equal to A or B. If yes, then count=2. Else count=0.
# 4. If A1 and A2 are not equal to A or B, then check if B1 and B2 are equal to A or B. If yes, then count=2. Else count=0.
# 5. If A1 and A2 are not equal to A or B, then check if B1 and B2 are equal to A or B. If
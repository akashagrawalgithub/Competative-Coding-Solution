#question
# Problem Code: WGHTS

# Contest Code:START53

#problem :-Chef has 3 weights, weighing x, y, and z. Can he measure a weight of exactly W using these?

#solution:-
tc=int(input())
while(tc):
    W,X,Y,Z = map(int,input().split(" "))
    if W == X or W == Y or W == Z:
        print("YES")
    else:
        if X+Y == W:
            print("YES")
        elif(X+Z==W):
            print("YES")
        elif(Y+Z==W):
            print("YES")
        elif X+Y+Z ==W:
            print("YES")
        else:
            print("NO")
    tc-=1

#explaination:-
# The code is doing the following:
# 1. It takes the input of 4 numbers and stores them in W,X,Y,Z variables.
# 2. If W is equal to X or Y or Z then it prints YES.
# 3. Else if X+Y = W then it prints YES.
# 4. Else if X+Z = W then it prints YES.
# 5. Else if Y+Z = W then it prints YES.
# 6. Else if X+Y+Z = W then it prints YES.
# 7. Else it prints NO.
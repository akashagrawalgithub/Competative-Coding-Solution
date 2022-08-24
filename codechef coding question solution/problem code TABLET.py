#Question 

#Problem Code: TABLET
#Contest Code: COOK103

#problem :- Chef has visited some tablet shops and listed all of his options. In total, there are NN available tablets, numbered 11 through NN. For each valid ii, the i_{th}i thtablet has width W_iW i, height H_iH iand price P_iP i​.Chef’s budget is equal to BB. He wants to buy the tablet with the largest screen (largest area) as long as its price fits with in the budget.


#Solution 
tc=int(input())
while(tc):
    listoflist=[]
    N,B = map(int,input().split(" "))
    for i in range(N):
        w,h,p=map(int, input().split())
        listn=[w,h,p]
        listoflist.append(listn)
    size=0
    for i in listoflist:
        if i[2] <= B:
            if i[0]*i[1]>size:
                size = i[0]*i[1]
    if size == 0:
        print("no tablet")
    else:
        print(size)
    tc-=1

#Time Complexity :- O(n^2)

#Explation :-
# The code is doing the following:
# 1. It is taking the input of N,B from the user.
# 2. It is creating a list of lists called listoflist.
# 3. It is taking the input of w,h,p for each element in the listoflist.
# 4. It is checking if the p value is less than or equal to B.
# 5. If it is true then it is checking if the size of the rectangle formed by w and h is greater than the size variable.
# 6. If it is true then it is assigning the size variable to the size of the rectangle formed by w and h.
# 7. If it is false then it is printing no tablet.
# 8. It is decrementing the tc variable by 1.
# 9. It is repeating the steps 1-8 until tc becomes 0.
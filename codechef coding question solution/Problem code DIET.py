#Question
#problems code :- DIET
# Contest Code: COOK112

#problem 
# chef decided to go on a diet during the following NN days (numbered 11 through NN). Part of the diet plan is to eat KK grams of protein during each day. For each valid ii, Chef wants to buy A_iA​ grams of protein in the morning of the ii-th day and then eat KK grams of protein as part of his dinner. If he has any protein remaining, he can store it and use it in later dinners. Initially, Chef is storing 00 grams of protein.Determine whether Chef will have enough protein all the time during his diet. In case he will not have enough, find the first day on which Chef will be unable to eat KK grams of protein.

#solution :- 
tc=int(input())
while(tc):
    N,K = map(int,input().split(" "))
    array = list(map(int,input().split(" ")))
    diet=0
    count=0
    for i in range(N):
        diet=diet+array[i]-K
        if diet<0:
            print("NO",(i+1))
            break
        if i == N-1:
            if diet>=0:
                print("YES")
    tc-=1 



#Expalnation :-
# The code is doing the following:
# 1. It is taking the input as N and K.
# 2. Then it is taking the array of size N.
# 3. Then it is taking the diet variable which is initially 0.
# 4. Then it is taking the count variable which is initially 0.
# 5. Then it is iterating through the array.
# 6. Then it is adding the current element of the array to the diet variable.
# 7. If the diet variable is less than 0, then it will print NO and the index where the problem was found.
# 8. If the diet variable is greater than or equal to 0, then it will increment the count variable.
# 9. If the count variable is equal to N, then it will print YES.
# 10. Then it will decrement the tc variable by 1.
# 11. Then it will go back to step 1.

#Time Complexity : O(N)
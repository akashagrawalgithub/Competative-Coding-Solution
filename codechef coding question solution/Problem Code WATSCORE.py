#question

# Problem Code:WATSCORE

# You are participating in a contest which has 11 problems (numbered 11 through 11). The first eight problems (i.e. problems 1, 2, \ldots, 81,2,…,8) are scorable, while the last three problems (99, 1010 and 1111) are non-scorable ― this means that any submissions you make on any of these problems do not affect your total score.

# Your total score is the sum of your best scores for all scorable problems. That is, for each scorable problem, you look at the scores of all submissions you made on that problem and take the maximum of these scores (or 00 if you didn't make any submissions on that problem); the total score is the sum of the maximum scores you took.

# You know the results of all submissions you made. Calculate your total score.



#solution

tc = int(input())
while(tc):
    ans=[0]*9
    N=int(input())
    sum=0
    for i in range(N):
        X,Y=map(int,input().split(" "))
        if X<=8 and ans[X]<Y:
            ans[X]=Y
    for i in range(len(ans)):
        sum=sum+ans[i]
    print(sum)
    tc-=1


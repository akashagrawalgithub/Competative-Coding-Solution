#question

# You have NN balls and KK boxes. You want to divide the NN balls into KK boxes such that:

# Each box contains 1≥1 balls.
# No two boxes contain the same number of balls.
# Determine if it is possible to do so.




#solution 

tc=int(input())
while(tc):
    n,k=map(int,input().split(" "))
    if (k*(k+1))//2<=n:
        print("yes")
    else:
        print("no")
    tc-=1
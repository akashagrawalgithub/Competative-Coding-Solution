#question 
#problem Code :- LUCKYFR
# Contest Code: Practice

#Problem Statement
# Karan likes the number 4 very much.Impressed by the power of this number, Karan has begun to look for occurrences of four anywhere. 
# He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. 
# He is too busy now, so please help him.


#solution
tc=int(input())
while(tc):
    x=int(input())
    count=0
    for i in str(x):
        if 4 == int(i):
            count+=1
    print(count)
    tc-=1

#Explaination :
# The code is doing the following:
# 1. It takes the input from the user as an integer.
# 2. It checks if the number is divisible by 4. If yes, it increments the count variable by 1.
# 3. It prints the value of count variable.
# 4. It decrements the value of tc by 1.
# 5. It repeats the steps 1 to 4 until tc becomes 0.
 
# Problem Code:THREEQ

# Contest Code:CDMN2021

# problem statement
# Once upon a time, there was a hero and an old saint. And like in any story with a hero and an old saint,
# the old saint asked the hero — three questions!But here's the twist: each question was a binary question, 
# which means that the answer to each must be either a 'Yes' or a 'No',not none, not both. Our hero, who was not so wise in the 
# ways of science, answered them arbitrarily and just hoped he is correct. The old saint, being so old, does not remember which 
# answers were correct. The only thing that he remembers is - how many of them were 'Yes', and how many of them were 'No'. 
# Our hero will pass the test if the old saint cannot distinguish his responses from the set of correct answers i.e. 
# if the number of 'Yes' and 'No' in the responses matches that in the correct answers, regardless of their order.You are given 
# the answers to each of the three questions, and the responses of the hero to the same. Find whether the hero will be able to 
# pass the old saint's test.


#solution

tc=int(input())
while(tc):
    A1,A2,A3=map(int,input().split(" "))
    B1,B2,B3=map(int,input().split(" "))
    reponsearray=[A1,A2,A3]
    answerarray=[B1,B2,B3]
    if reponsearray.count(0) == answerarray.count(0):
        if reponsearray.count(1) == answerarray.count(1):
            print("Pass")
    else:
        print("Fail")
    tc-=1


#explaination
# The code is doing the following:
# 1. It is taking the input from user and storing it in an array.
# 2. It is taking the input from user and storing it in another array.
# 3. It is checking if the number of 0's in the first array are equal to the number of 0's in the second array.
# 4. If yes, then it checks if the number of 1's in the first array are equal to the number of 1's in the second array.
# 5. If yes, then it prints "Pass" else it prints "Fail".
# 6. It decreases the value of tc by 1.
# 7. It repeats the above steps till tc becomes zero.
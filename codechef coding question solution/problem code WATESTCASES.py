#Question 
#problems code :- WATESTCASES
#Contest Code:- Practice

# Given the results (pass/fail) and sizes of NN test cases that a submission is run on. Find the smallest test case that fails this submission.

#solution

tc = int(input())
while(tc):
    n=int(input())
    array = list(map(int,input().split(" ")))
    s=input()
    minmum=1000
    for i in range (n):
        if s[i] == "0" and array[i]<minmum:
            minmum = array[i]
    print(minmum)
    tc-=1

#expalnation :-
# The code is doing the following:
# 1. It takes the number of elements in the array as input.
# 2. It then takes the array elements as input and stores it in a list.
# 3. It then takes the string as input and stores it in another list.
# 4. It then iterates through the string and checks if the element at that index is 0 or not.
# 5. If the element is 0, it checks if the corresponding element in the array is less than the current minimum value.
# 6. If yes, then it updates the minimum value to the corresponding element in the array.
# 7. Finally, it prints the minimum value.



#follow me for such more such updates and solutions

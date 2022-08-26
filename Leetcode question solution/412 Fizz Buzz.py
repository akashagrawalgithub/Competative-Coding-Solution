#question : 412 Fizz Buzz

#problem statement
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

 #solution:
def fizzBuzz(self, n: int) -> List[str]:
    ans=[]
    for i in range(n):
        x=i+1
        if (x%3==0) and (x%5==0):
            ans.append("FizzBuzz")
        elif x%3==0:
            ans.append("Fizz")
        elif x%5==0:
            ans.append("Buzz")
        else:
            y=str(x)
            ans.append(y)
    return ans
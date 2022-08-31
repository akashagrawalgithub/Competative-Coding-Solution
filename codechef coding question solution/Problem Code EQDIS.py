#problem
# Problem Code:EQDIS

# Let F(S)F(S) denote the number of distinct elements in the array SS. For example, F([1, 2, 3, 2]) = 3, F([1, 2]) = 2.F([1,2,3,2])=3,F([1,2])=2.

# You are given an array AA containing NN integers. Find if it is possible to divide the elements of the array AA into two arrays BB and CC such that :

# Every element of the array AA belongs either to array BB or to array CC.
# F(B) = F(C)F(B)=F(C).



#solution

tc=int(input())
while(tc):
    n=int(input())
    a=list(map(int,input().split(" ")))
    distinct = len(set(a))
    print('yes' if (distinct%2 == 0 or distinct < n) else 'no')
    tc-=1

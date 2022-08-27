# Problem Code: ZCOSCH

#problem statement:
# The ZCO Scholarship Contest has just finished, and you finish with a rank of R. You know that Rank 1 to Rank 50 will get 100% scholarship on the ZCO exam fee and 
# Rank 51 to Rank 100100 will get 50% percentage scholarship on the ZCO exam fee. The rest do not get any
# scholarship.What percentage of scholarship will you get ?

#solution:
R=int(input())
if R>=1 and R<=50:
    print(100)
elif R>=51 and R<=100:
    print(50)
else:
    print(0)

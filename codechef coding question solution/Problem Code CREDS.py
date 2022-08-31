#Question
# In the current semester, you have taken XX RTP courses, YY Audit courses and ZZ Non-RTP courses.

# The credit distribution for the courses are:

# 44 credits for clearing each RTP course.
# 22 credits for clearing each Audit course.
# No credits for clearing a Non-RTP course.
# Assuming that you cleared all your courses, report the number of credits you obtain this semester.



#Solution
tc=int(input())
while(tc):
    A1,A2,A3=map(int,input().split(" "))
    ans=(A1*4)+(A2*2)
    print(ans)
    tc-=1

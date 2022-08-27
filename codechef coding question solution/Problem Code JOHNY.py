#question

#Problem Code:JOHNY

#problem statement :
# lad enjoys listening to music. He lives in Sam's Town. A few days ago he had a birthday, so his parents gave 
# him a gift: MP3-player! Vlad was the happiest man in the world! Now he can listen his favorite songs whenever 
# he wants!Vlad built up his own playlist. The playlist consists of N songs, each has a unique positive integer 
# length. Vlad likes all the songs from his playlist, but there is a song, which he likes more than the others. 
# It's named "Uncle Johny".After creation of the playlist, Vlad decided to sort the songs in increasing order of 
# their lengths. For example, if the lengths of the songs in playlist was {1, 3, 5, 2, 4} after sorting it 
# becomes {1, 2, 3, 4, 5}. Before the sorting, "Uncle Johny" was on K-th position (1-indexing is assumed for the 
# playlist) in the playlist.Vlad needs your help! He gives you all the information of his playlist. 
# Your task is to find the position of "Uncle Johny" in the sorted playlist.


#solution : 
tc=int(input())
while(tc):
    k=int(input())
    array = list(map(int,input().split()))
    K=int(input())
    x=array[K-1]
    array.sort()
    for i in range(len(array)):
        if array[i]==x:
            print(i+1)
    tc-=1

#Explanation :
# The code is doing the following:
# 1. It takes the input of the number of test cases, k and array size.
# 2. It takes the input of the element to be searched.
# 3. It sorts the array in ascending order.
# 4. It iterates through the array and checks if the element is equal to the element at index K-1.
# 5. If it is equal to the element at index K-1, then it prints the index of the element.
# 6. It decrements the test case by 1.
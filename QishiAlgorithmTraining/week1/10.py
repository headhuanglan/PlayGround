#same as 
#https://www.geeksforgeeks.org/maximum-value-array-m-range-increment-operations/
"""
Input : n = 5 m = 3
        a = 0, b = 1, k = 100
        a = 1, b = 4, k = 100
        a = 2, b = 3, k = 100
Output : 200
Explanation:
Initially array = {0, 0, 0, 0, 0}
After first operation:
array = {100, 100, 0, 0, 0}
After second operation:
array = {100, 200, 100, 100, 100}
After third operation:
array = {100, 200, 200, 200, 100}
Maximum element after m operations 
is 200.
"""
Initially_array = [0, 0, 0, 0, 0]
lenarray=len(Initially_array)
def increment(a, b, k):
    if a>=0 and b<lenarray:
        Initially_array[a]+=k
        if b+1<lenarray:
            Initially_array[b+1]+=-k

def prefix_sum():
    curval=Initially_array[0]
    maxval=-999999999999
    for i in range(lenarray-1):
        Initially_array[i]=curval
        curval+=Initially_array[i+1]
        if Initially_array[i]>maxval:
            maxval=Initially_array[i]
    Initially_array[lenarray-1]=curval
    if Initially_array[lenarray-1]>maxval:
        maxval=Initially_array[i-1]

    print(maxval)






increment(0, 1, 100)
increment(1, 4, 100)
increment(2, 3, 100)
prefix_sum()    



    
 

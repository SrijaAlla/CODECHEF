# Python3 program to print sums of 
# all possible subsets. 

# Prints sums of all subsets of arr[l..r] 
def subsetSums(n):
    l = 0
    t = 1
    while(2**(t) < n):
     t+=1 
    t+=1
    print(t)
    #t = highestPowerof2(n)
    arr = list()
    for i in range(t):
       arr.append(3**i)
    r = len(arr)
    if(l > r): 
	  print(sum,end =" ")
      return 
	subsetSums(arr, l + 1, r, sum + arr[l]) 
	subsetSums(arr, l + 1, r, sum) 

# Driver code 
n = int(input())
subsetSums(n) 

# This code is contributed by Shreyanshi Arun. 

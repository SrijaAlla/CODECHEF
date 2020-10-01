import itertools 
from itertools import combinations, chain

def findsubsets(s, n): 
    return list(map(set, itertools.combinations(s, n))) 

def highestPowerof2(n): 
  
    res = 0
    for i in range(n, 0, -1): 
          
        # If i is a power of 2 
        if ((i & (i - 1)) == 0): 
            res = i 
            break          
    return res
    
def call(n):
    t = 1
    while(2**(t) < n):
     t+=1 
    t+=1
    print(t, 2**t)
    #t = highestPowerof2(n)
    s = set()
    sub = list()
    for i in range(t):
       s.add(3**i)
    print(s)  
    for i in range(1,t):
      findsubsets(s,i)
      for j in range(len(findsubsets(s,i))):
          sub.append(findsubsets(s,i)[j])
    print(sub)

    for u in range(len(sub)):
      for w in range(0,len(sub)-u-1):
        if(sum(sub[w]) > sum(sub[w+1])):
             sub[w], sub[w+1] = sub[w+1], sub[w] 
   # print(sub)
    #print(sub[n-1])
    print(len(sub[n-1]))
    final = list()
    final = sorted(sub[n-1])
    #for k in range(len(final)):
    print(*final, sep = " ")
        
t = int(input())
for i in range(t):
    n = int(input())
    call(n)

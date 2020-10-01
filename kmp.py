# your code goes here
# cook your dish here
def call():
 s = input()
 for x in range(int(s)):
    t=input()
    p=input()
    for i in p:
        k = t.index(i)
        print(k)
        t=t[:k]+t[k+1:]
        print(t[:k])
        print(t)
    t=''.join(sorted(t))
    print(t)
    i=0
    while(t[i]<=p[0]):
        i+=1
    t=t[:i]+p+t[i:]
    print(t)
    
call()
    
    
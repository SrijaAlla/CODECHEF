def fun():
   t = input()
   p = input()
   if(t.islower() == False or p.islower() == False):
     return
   if(len(t) > 1000):
     return
   for x in p:
     try:
       k = t.index(x)
       t = t[:k]+t[k+1:]
     except ValueError:
         return
   t = ''.join(sorted(t))
   i = 0 
   if(len(t) == 0):
     t = p
     print(t)
     return    
   else:
    if(len(t) >= 1):
      while(t[i] < p[0]):
        i+=1
        if(i == len(t)):
         t = t[:i]+p+t[i:]
         print(t)
         return
      if(t[i] == p[0] and len(p) > 1):
          while(t[i] == p[0] and p[1] > t[i]):
            print(t[i],i,"while")
            i+=1
            if(i == len(t)):
              break
      t = t[:i]+p+t[i:]
    #else:
     #   if(t[i] <= p[0]):
      #   t = t[i]+p
       # else:
        # t = p+t[i]
    print(t)
    

for _ in range(int(input())):
  fun()
       
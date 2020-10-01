def call():
      x = list()
      num, cost = map(int,input().split())
      print("total guests = ",num," cost of each table =",cost)
      x = list(map(int,input().strip().split()))[:num]
      #check repitiotions in list
      ans = cost
      i = 0
      #ans  = cost
      #for(i=0;i<len(x);i++){
      # for(j=i;j<len(x);j++){
      #  if(x[i] == x[j]){
             #ans = cost + ans
             # dupli++
             # x = x[:i]        
      #   }
      #  }
      # }
      for i in range(int(len(x))):
         if(i == len(x)):
             break
         if(x[i] == x[i+1]):
             ans+=cost
         else:
             continue
      print(ans)
call()

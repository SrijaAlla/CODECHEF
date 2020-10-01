class typeofquery:
    
def type1(arr,queries,t):
    L = queries[t][1]
    R = queries[t][2]
    x = queries[t][3]
    for i in range(len(arr)):
       if(arr[i] >= L and arr[i] <= R):
           arr[i]+=x
    #print(arr)
           
def type2(arr,queries,t):
    L = queries[t][1]
    R = queries[t][2]
    x = queries[t][3]
    for i in range(len(arr)):
       if(arr[i] > L and arr[i] < R):
           arr[i] = arr[i]*x
    #print(arr)

def type3(arr,queries,t):
    z = queries[t][1]
    pos = list()
    for i in range(len(arr)):
        if(z == arr[i]):
            pos.append(i)
    if(len(pos) == 0):
        print(-1)
        return
    #mini = min(pos)
    #maxi = max(pos)
    print(max(pos)-min(pos)+1)
    #print(arr)
    return
    #print(maxi-mini+1)
    #return(maxi-mini+1)


def call(queries,i):
    if(queries[i][0] == 1):
        return 1
    elif(queries[i][0] == 2):
         return 2
    elif(queries[i][0] == 3):
        return 3

def whole(arr,queries,q):

    for j in range(q):
        k = call(queries, j)
        if(k == 1):
            type1(arr,queries,j)
        if(k == 2):
            type2(arr,queries,j)
        if(k == 3):
            type3(arr,queries,j)

n = int(input())
if( n < 1 or n > 400000 ):
    exit
arr = list(map(int,input().strip().split()))[:n]
q = int(input())
if( q < 1 or q > 10000):
    exit
queries = list()
for i in range(q):
    queries.append(list(map(int,input().strip().split()))[:4])
#print("queries", queries)
#print(arr)
whole(arr,queries,q)

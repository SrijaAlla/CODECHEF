num = int(input())

if(num > 10 or num < 1):
    exit
x = list(map(int,input().strip().split()))[:num]
#print(x)
sum = 0
for p in x:
    if(int(p) > 10**10 or int(p) < 0):
        exit
    sum = sum + int(p)
print(sum)
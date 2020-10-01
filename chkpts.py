x = list()
y = list()

test = int(input())
num_points, c = map(int,input().split())
j = 0
print("number points",num_points,"c_value =",c)
for j in range(num_points):
    x_value, y_value = map(int,input().split())
    x.append(x_value)
    y.append(y_value)
print(x,y)

def fuc(x,y):
    
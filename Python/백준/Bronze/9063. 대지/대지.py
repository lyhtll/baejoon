n = int(input())
xl=[]
yl=[]
for i in range(n):
    x,y = map(int, input().split())
    xl.append(x)
    yl.append(y)
if len(xl) == 1 and len(yl) == 1:
    print(0)
else:
    print((max(xl)-min(xl))*(max(yl)-min(yl)))
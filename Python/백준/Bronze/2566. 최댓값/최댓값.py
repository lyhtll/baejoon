li=[]
for i in range(9):
    n=list(map(int,input().split()))
    li.append(n)
max=li[0][0]
a,b=0,0
for i in range(9):
    for j in range(9):
        if li[i][j]>max:
            max=li[i][j]
            a,b=i,j
        elif max==li[i][j]:
            continue
print(max)
print(a+1,b+1)
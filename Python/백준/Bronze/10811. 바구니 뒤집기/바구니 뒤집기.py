n,m=map(int,input().split())
li=[]
for i in range(1,n+1):
    li.append(i)
for i in range(m):
    i,j=map(int,input().split())
    li3=li[i-1:j]
    li3.reverse()
    li[i-1:j]=li3
for i in range(n):
    print(li[i],end=' ')

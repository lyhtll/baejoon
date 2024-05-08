li=[1,1,2,2,2,8]
li2=list(map(int,input().split()))
for i in range(6):
    li[i]-=li2[i]
print(*li)
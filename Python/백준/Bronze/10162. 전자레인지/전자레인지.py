t=int(input())
li=[0,0,0]
while True:
    if t-300>=0:
        t-=300
        li[0]+=1
    elif t-60>=0:
        t-=60
        li[1]+=1
    else:
        t-=10
        li[2]+=1
    if t==0:
        print(*li)
        break
    elif t<0:
        print(-1)
        break
    
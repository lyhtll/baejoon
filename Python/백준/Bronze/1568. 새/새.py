n=int(input())
t=0
while n>0:
    t2=1
    while n-t2>=0:
        n-=t2
        t+=1
        t2+=1
print(t)
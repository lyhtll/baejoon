while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        t=1
        t2=1
        if b > a - b:
            b = a - b
        for i in range(b):
            t*=a
            a-=1
        for i in range(1,b+1):
            t2*=i
        print(int(t/t2))
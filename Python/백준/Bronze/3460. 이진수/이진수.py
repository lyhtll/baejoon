r=int(input())
for i in range(r):
    li=[]
    n=int(input())
    while True:
        if n<1:
            break
        j=n%2
        n=n//2
        li.append(j)
    for k in range(len(li)):
        if li[k]==1:
            print(k,end=' ')
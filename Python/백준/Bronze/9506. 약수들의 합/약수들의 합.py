while True:
    n=int(input())
    li=[]
    if n==-1:
        break
    else:
        for i in range(1,n):
            if n%i==0:
                li.append(i)
    if n==sum(li):
        print(f'{n} =',end=' ')
        for i in range(len(li)):
            if i==len(li)-1:
                print(li[i])
            else:
                print(li[i],end=' + ')
    else:
        print(f'{n} is NOT perfect.')

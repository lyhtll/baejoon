t=int(input())
for i in range(t):
    ys=[]
    ks=[]
    for j in range(9):
        y,k=map(int,input().split())
        ys.append(y)
        ks.append(k)
    if sum(ys)>sum(ks):
        print('Yonsei')
    elif sum(ys)<sum(ks):
        print('Korea')
    else:
        print('Draw')
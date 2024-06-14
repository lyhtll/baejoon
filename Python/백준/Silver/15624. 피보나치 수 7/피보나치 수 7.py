n=int(input())
a=0
b=0
for i in range(1,int(n+1%1000000007)):
    if i==1:
        b=1
    else:
        a,b=b%1000000007,(a+b)%1000000007
print(b)
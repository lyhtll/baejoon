a,b,c=map(int,input().split())
for i in range(c):
    a=(a%b)*10
    n=a//b
print(n)
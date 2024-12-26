n=int(input())
n2=n
m=1
while n-m>0:
    n-=m
    m+=1

t=0
for i in range(1,m):
    t+=i

n2-=(t-1)

if m % 2 == 0:
    a = 1
    b = m
    for i in range(n-1):
        a+=1
        b-=1
else:
    a = m
    b = 1
    for i in range(n - 1):
        a -= 1
        b += 1

print(f"{a}/{b}")
n=int(input())
t=1
n-=1
while True:
    if (n - (t * 6)) >= 0:
        n -= t*6
        t += 1
    else:
        break
if n>0:
    t+=1
print(t)
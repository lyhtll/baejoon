N=int(input())
li=list(map(int,input().split()))
min=max=li[0]
for i in range(N):
    if li[i]>max:
        max=li[i]
    elif li[i]<min:
        min=li[i]
print(min,max)
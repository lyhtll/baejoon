n=int(input())
li=input().split()
if (sum(map(int,li)) == 0):
    print(0)
else:
    for i in li:
        for j in range(len(li)-1):
            if int(li[j]+li[j+1])<int(li[j+1]+li[j]):
                li[j],li[j+1]=li[j+1],li[j]
    print(*li,sep='')


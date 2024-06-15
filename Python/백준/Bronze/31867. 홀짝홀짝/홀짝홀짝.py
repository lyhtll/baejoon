n=int(input())
k=input()
hol=[1,3,5,7,9]
jjak=[0,2,4,6,8]
h=0
j=0
for i in range(n):
    if int(k[i]) in hol:
        h+=1
    elif int(k[i]) in jjak:
        j+=1
if h>j:
    print(1)
elif j>h:
    print(0)
else:
    print(-1)
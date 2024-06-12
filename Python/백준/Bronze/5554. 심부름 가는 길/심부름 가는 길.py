li=[]
for i in range(4):
    s=int(input())
    li.append(s)
t=sum(li)
print(t//60)
print(t%60)
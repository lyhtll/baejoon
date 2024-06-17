li=[]
for i in range(4):
    n=int(input())
    li.append(n)
li2=[]
for i in range(2):
    n2=int(input())
    li2.append(n2)
li.remove(min(li))
li2.remove(min(li2))
print(sum(li)+sum(li2))

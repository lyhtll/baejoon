r=int(input())
t=0
li=[]
for i in range(r):
    s=input()
    for j in range(len(s)):
        if j==0:
            li.append(s[j])
        elif s[j]!=li[j-1] and s[j] in li:
            break
        else:
            li.append(s[j])
    if len(li)==len(s):
        t+=1
    li=[]
print(t)
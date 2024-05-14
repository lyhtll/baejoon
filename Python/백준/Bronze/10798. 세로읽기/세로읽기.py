li=[]
le=[]
for i in range(5):
    s=input()
    le.append(len(s))
    li.append(s)
for i in range(max(le)):
    for j in range(5):
        if i<le[j]:
            print(li[j][i],end='')
li=['A+','A0','B+','B0','C+','C0','D+','D0','F']
t=0
t2=0
for i in range(20):
    a,b,c=input().split()
    if c=='P':
        continue
    elif c!='F':
        t+=float(b)*(4.5-li.index(c)*0.5)
        t2+=float(b)
    elif c=='F':
        t2+=float(b)
        t+=0
print(t/t2)
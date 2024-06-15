li=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s,n=map(int,input().split())
li2=[]
while s>0:
    li2.append(li[s%n])
    s=s//n
li2.reverse()
print(*li2,sep='')
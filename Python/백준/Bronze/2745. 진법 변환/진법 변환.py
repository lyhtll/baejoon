li=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s,n=input().split()
li2=[]
t2=0
for i in range(len(s)):
    li2.append(str(li.index(s[i])))
for i in range(len(li2)):
    t2+=int(li2[i])*(int(n)**(len(li2)-1-i))
print(t2)
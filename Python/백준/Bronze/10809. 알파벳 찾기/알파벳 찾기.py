s=input()
li=[-1 for i in range(26)]
l2=[]
for i in range(97,123):
    if chr(i) in s:
        for j in range(len(s)):
            if chr(i)==s[j]:
                if s[j] not in l2:
                    l2.append(s[j])
                    li[i-97]=j
print(*li)
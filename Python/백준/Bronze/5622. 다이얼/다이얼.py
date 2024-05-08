li=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']#번호판
s=input()
t=0
for i in range(len(s)):#문자 수만큼 반복
    for j in li:#리스트만큼 반복
        if s[i] in j:
            t+=(li.index(j)+3)
print(t)
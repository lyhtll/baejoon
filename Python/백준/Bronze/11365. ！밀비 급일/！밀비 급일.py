while True:
    s=input()
    li=[]
    for i in s:
        li.append(i)
    if s=='END':
        break
    else:
        li.reverse()
        print(*li,sep='')
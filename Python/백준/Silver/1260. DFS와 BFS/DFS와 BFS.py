import copy
from collections import deque
n,m,v = map(int,input().split())
dic = {}
dfl = []
bfl = []
for i in range(m):
    f,s = map(int,input().split())
    if f not in dic:
        dic[f] = []
    if s not in dic:
        dic[s] = []
    dic[f].append(s)
    dic[s].append(f)
dic2 = copy.deepcopy(dic)

def dfs(dic,key,dfl):
    dfl.append(key)
    for next in sorted(dic.get(key,[])):
        if next not in dfl and dic.get(next) is not None:
            dfs(dic,next,dfl)

def bfs(dic,key):
    bfl.append(key)
    queue = deque([key])
    while queue:
        key = queue.popleft()
        for next in sorted(dic.get(key,[])):
            if next not in bfl:
                bfl.append(next)
                queue.append(next)

dfs(dic,v,dfl)
bfs(dic2,v)
for i in dfl:
    print(i,end=' ')
print()
for i in bfl:
    print(i,end=' ')
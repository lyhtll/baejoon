from collections import deque
import sys

n = int(sys.stdin.readline())
ls = [0 for _ in range(n + 1)]
queue = deque([n])

while queue:
    x = queue.popleft() 
    if x == 1:
        break
    if x % 3 == 0 and (ls[x // 3] == 0 or ls[x // 3] > ls[x] + 1):
        ls[x // 3] = ls[x] + 1
        queue.append(x // 3)
    if x % 2 == 0 and (ls[x // 2] == 0 or ls[x // 2] > ls[x] + 1):
        ls[x // 2] = ls[x] + 1
        queue.append(x // 2)
    if x - 1 > 0 and (ls[x - 1] == 0 or ls[x - 1] > ls[x] + 1):
        ls[x - 1] = ls[x] + 1
        queue.append(x - 1)
print(ls[1])
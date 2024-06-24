import sys
n=sys.stdin.readline().rstrip()
s1=set()
for i in range(int(n)):
    s=sys.stdin.readline().rstrip()
    s1.add(s)
li = sorted(s1, key=lambda x: (len(x), x))
print(*li, sep='\n')
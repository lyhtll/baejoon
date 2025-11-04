n = int(input())
result = 0
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
for i in range(n):
    result+=(li[i % n][0] * li[(i+1) % n][1] - li[(i+1) % n][0] * li[i % n][1])
print(abs(result/2))
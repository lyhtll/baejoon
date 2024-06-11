S, D = map(int, input().split())
if (S + D) % 2 != 0 or (S - D) % 2 != 0 or S < D:
    print(-1)
else:
    a = (S + D) // 2
    b = (S - D) // 2
    print(a, b)

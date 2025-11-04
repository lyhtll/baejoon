n = int(input())
count = 0
num = 1
result = []
while num <= 9876543210:
    isMinus = True
    s = str(num)
    for i in range(len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            isMinus = False
            next_digit = int(s[i]) + 1
            num = int(s[:i] + str(next_digit) + '0' * (len(s) - i - 1))
            break

    if isMinus:
        count += 1
        result.append(num)
        num += 1
if len(result) < n:
    print(-1)
elif n == 0:
    print(0)
else:
    print(result[n-1])
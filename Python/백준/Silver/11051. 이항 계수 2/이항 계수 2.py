from math import factorial
n,k=map(int,input().split())
r=factorial(n)//(factorial(k)*factorial(n-k))
print(r%10007)
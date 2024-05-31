h,m,s=map(int,input().split())
u=int(input())
t=h*3600+m*60+s
t2=t+u
print(f'{t2//3600%24} {t2%3600//60} {t2%3600%60}')
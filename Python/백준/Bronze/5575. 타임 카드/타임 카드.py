for i in range(3):
    h,m,s,h2,m2,s2=map(int,input().split())
    ht=h2-h
    mt=m2-m
    st=s2-s
    t=ht*3600+mt*60+st
    print(t//3600,t%3600//60,t%3600%60)
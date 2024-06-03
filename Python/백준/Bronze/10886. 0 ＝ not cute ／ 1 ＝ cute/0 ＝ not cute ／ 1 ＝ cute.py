r=int(input())
agree=0
disagree=0
for i in range(r):
    n=int(input())
    if n==1:
        agree+=1
    elif n==0:
        disagree+=1
if agree>disagree:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
n=int(input())
a=1
b=1
if n!=1 and n!=2:
    i=3
    while i<=n:
        c=a+b
        a,b=b,c#a變成b,b變成c
        i+=1
    print(c)
elif n==1 or n==2:
    print(1)
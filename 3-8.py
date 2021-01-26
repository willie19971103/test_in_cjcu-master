# Given three integers, print the least of them.
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
elif a>b and b<c:
    print(b)
elif c<b and a>c:
    print(c)
else:
    pass
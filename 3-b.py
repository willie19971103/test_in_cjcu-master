# Given three integers, in which two are equal to each other and the third one is different. Print the order number of this different one - 1, 2 or 3.
a=int(input())
b=int(input())
c=int(input())
if a==b!=c:
    print(3)
elif a==c!=b:
    print(2)
elif b==c!=a:
    print(1)
else:
    pass
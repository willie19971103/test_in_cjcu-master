# Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a!=b!=c!=a:
    print(0)
else:
    print(2)
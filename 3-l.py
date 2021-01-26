# Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.
a=int(input())
b=int(input())
if a!=0:
    if b%a==0:
        print(b//a)
    if b%a!=0:
        print('no solution')
if a==0:
    if b!=0:
        print('no solution')
    if b==0:
        print('many solutions')
        
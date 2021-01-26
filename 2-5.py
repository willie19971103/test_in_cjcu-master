# Given a three-digit number. Find the sum of its digits.
n=int(input())
a=n//100
b=n%100//10
c=n%10
print(a+b+c)
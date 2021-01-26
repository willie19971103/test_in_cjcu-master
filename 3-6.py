# Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.
n=int(input())
a=n//100
b=n%100//10
c=n%10
# print(a,b,c)
if c>b>a :
    print('YES')
else :
    print('NO')
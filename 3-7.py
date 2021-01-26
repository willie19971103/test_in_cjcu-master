# Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
n=int(input())
a=n//1000
b=n%1000//100
c=n%100//10
d=n%10
if (a,b,c,d)==(d,c,b,a):
    print('YES')
else:
    print('NO')
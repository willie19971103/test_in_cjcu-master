# Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.
a=int(input())
len_a=len(str(a))
if len_a==3:
    print("YES")
else:
    print("NO")
# For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X. Print the exponent value and the result of the expression 2ⁿ.
n=int(input())
i=0
while 2**(i+1)<=n:
    i+=1
print(i,2**i)

# n=int(input())
# i=1
# while 2**(i)<=n:
#     i+=1
# print(i-1,2**(i-1))
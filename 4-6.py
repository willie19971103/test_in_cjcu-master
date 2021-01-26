# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n! = 1 × 2 × … × n
# For the given integer n calculate the value n!. Don't use math module in this exercise.
a=int(input())
sum=1
for n in range(1,a+1):
    sum*=n
print(sum)
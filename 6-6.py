# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the sum of the sequence.
x=int(input())
n=0
sum=0
while x!=0:
    n+=1
    sum+=x
    x=int(input())
print(sum)

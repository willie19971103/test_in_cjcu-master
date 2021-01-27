# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the maximum of the sequence
n=int(input())
b=[]
while n!=0:
    n=int(input())
    b.append(n)  
print(max(b))
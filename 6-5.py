# Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence. The sequence ends with 0. Print the length of the sequence (not counting the 0). The numbers following the number 0 should be omitted.
x=int(input())
n=0
while x!=0:
    x=int(input())
    n+=1
print(n)

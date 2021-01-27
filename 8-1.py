# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. Multiply every element by c and print the result.
# Read a 2D list of integers:
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# Print a value:
# print(a)
row,col=[int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]
mul=int(input())

for i in range(row):
    for j in range(col):
        a[i][j]*=mul
for row in a: #依序印
    print(*row) #印一排
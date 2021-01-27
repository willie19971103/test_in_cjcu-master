# Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:

# On the main diagonal put 0.
# On the diagonals adjacent to the main put 1.
# On the next adjacent diagonals put 2, and so forth.
n=int(input())
a=[[0]*n for i in  range(n)]#建第一排 然候用FOR 列其他排
for i in range(n): #輸入i
    for j in range(n): #輸入j
        a[i][j]=abs(i-j)#(ij相減絕對值剛好>條件)
for row in a: #印出
    print(*row)
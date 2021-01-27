# It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other. Thus, it requires that no two queens share the same row, column, or diagonal.  

# Given a placement of 8 queens on the chessboard. If there is a pair of queens that violates this rule, print YES, otherwise print NO. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chessboard with rows and columns numbered from 1 to 8.
#x數字不能重複
#y數字不能重複
#斜線數字不能重複
x1,y1=int(input().split())
x2,y2=int(input().split())
x3,y3=int(input().split())
x4,y4=int(input().split())
x5,y5=int(input().split())
x6,y6=int(input().split())
x7,y7=int(input().split())
x8,y8=int(input().split())

x=[x1,x2,x3,x4,x5,x6,x7,x8]
y=[y1,y2,y3,y4,y5,y6,y7,y8]
if set(x)!=8 or set(y)!=8:
    print('YES')

for x in  range(len(x)):
    
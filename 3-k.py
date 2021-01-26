# Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.
m=int(input())
d=int(input())
if m in(1,3,5,7,8,10):
    if d==31:
        print(m+1)
        print(1)
    else:
        print(m)
        print(d+1)
if m in(4,6,9,11):
    if d==30:
        print(m+1)
        print(1)
    else:
        print(m)
        print(d+1)
if m==2:
    if d==28:
         print(m+1)
         print(1)
    else:
        print(m)
        print(d+1)
if m==12:
    if d==31:
         print(1)
         print(1)
    else:
        print(m)
        print(d+1)
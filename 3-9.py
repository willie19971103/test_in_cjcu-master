# Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.
m=int(input())
# if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
#     print(31)
if m in[1,3,5,7,8,10,12]:
    print(31)
elif m in [4,6,9,11]:
    print(30)
else:
    print(28)
# if m==4 or m==6 or m==9 or m==11:
#     print(30)
# else:
#     print(28)
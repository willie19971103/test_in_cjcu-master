#Given a year (as a positive integer), find the respective number of the century. Note that, for example, 20th century began with the year 1901. 
Y=int(input())
if Y%100==0:
    print(Y//100)
else:
    print(Y//100+1)
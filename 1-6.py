# Given the integer N - the number of seconds that is passed since midnight - how many full hours and full minutes are passed since midnight?
# The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 1339).
# For example, if N = 3900, then 3900 seconds have passed since midnight - i.e. now it's 1:05am. So the program should print 1 65 - 1 full hour is passed since midnight, 65 full minutes passed since midnight. 
T=int(input())
a=T//60
b=a//60

print(b,a)

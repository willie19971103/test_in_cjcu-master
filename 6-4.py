# As a future athlete you just started your practice for an upcoming event. On the first day you run x miles, and by the day of the event you must be able to run y miles.

# Calculate the number of days required for you to finally reach the required distance for the event, if you increases your distance each day by 10% from the previous day.

# Print one integer representing the number of days to reach the required distance.
x=int(input())
y=int(input())
n=0
while x*(1.1**n)<y:
    n+=1
print(n+1)
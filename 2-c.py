# The hour hand of an analog clock turned α degrees since the midnight. Determine the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers
a=int(input())
h=a//30
m=a%30
mx1=m*2
mx2=int(mx1/60*360)
print(mx2)
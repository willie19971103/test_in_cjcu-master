# Given a list of numbers, determine and print the number of elements that are greater than both of their neighbors.
# The first and the last items of the list shouldn't be considered because they don't have two neighbors.

a=[int(i) for i in input().split()]
count=0
for i in range(1,len(a)-1):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        count+=1
print(count)
# Given a list of numbers with all elements sorted in ascending order, determine and print the number of distinct elements in it.
a=[int(i) for i in input().split()]
# print(len(set(a)))#set集合裡面不會有重複的項目
b=[]
count=0
for i in a:
    if i not in b:
        b.append(i)
        count+=1
print(count)
# Given a list of numbers, count a number of pairs of equal elements. Any two elements that are equal to each other should be counted exactly once.
a=[int(i) for i in input().split()]
count=0
for i in range(len(a)):#第一個開始比一行
    for j in range(i+1,len(a)):#第二個比第一輪
        if a[i]==a[j]:
            count+=1
print(count)

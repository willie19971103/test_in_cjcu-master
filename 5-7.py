# Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.
s=input()
a=s.find('h')
b=s.rfind('h')
c=s[:a]+s[b+1:]
print(c)
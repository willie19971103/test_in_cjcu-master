# Given a string that may contain a letter f. Print the index of the first and last occurrence of f. If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.
s=input()
if s.find('f')==s.rfind('f'):
    print(s.find('f'))
else:
    print(s.find('f'),s.rfind('f'))
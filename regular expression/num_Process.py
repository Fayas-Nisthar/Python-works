f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\regular expression\\number.txt")
from re import*
pattern="(91)?[6-9][\d]{9}"
for line in f:
    num=line.rstrip("\n")
    matcher=fullmatch(pattern,num)
    if matcher!=None:
        print(num)
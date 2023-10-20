f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\regular expression\\pancard.txt")
from re import*
pattern="[A-Z]{3}[PCAFHT][A-Z][\d]{4}[A-Z]"
for line in f:
    pan=line.rstrip("\n")
    matcher=fullmatch(pattern,pan)
    if matcher!=None:
        print(pan)

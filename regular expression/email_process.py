f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\regular expression\\data.txt")
from re import*
pattern="[a-z0-9_.]+@[a-z]{2,}.com"

for line in f:
    mail=line.rstrip("\n")
    matcher=fullmatch(pattern,mail)
    if matcher !=None:
        print(mail)


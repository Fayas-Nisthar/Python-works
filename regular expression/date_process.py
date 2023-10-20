f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\regular expression\\date.txt")
from re import*
# pattern="[\d]{2}[-][\d]{2}[-][\d]{4}"
# pattern="[\d]{2}[-][\d]{2}[-](20)[0-2]+[\d]"
pattern="([0][1-9]|[12][\d]|3[01])[-](0[1-9]|1[0-2])[-](20)([01][\d]|2[0-3])"
for line in f:
    date=line.rstrip("\n")
    matcher=fullmatch(pattern,date)
    if matcher!=None:
        print(date)

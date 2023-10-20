f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\regular expression\\reg_num.txt")
from re import*
pattern="(KL)[-\s][\d]{2}[-\s][A-Z]{1,2}[-\s][\d]{4}"
for line in f:
    reg_num=line.rstrip("\n")
    matcher=fullmatch(pattern,reg_num)
    if matcher !=None:
        print(reg_num)
from re import *
mob=input("enter mob number")
pattern="(91)?[6-9][0-9]{9}"
# pattern="[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}"   #\s is used for space
matcher=fullmatch(pattern,mob)
print("Invalid" if matcher==None else "valid")
from re import*
date=input("Enter date")
pattern="[\d]{4}[-\s][\d][0-2]?[-\s][\d]{2}"
matcher=fullmatch(pattern,date)
print("Invalid Date" if matcher==None else "valid date")
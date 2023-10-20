from re import*
email=input("Enter mail")
pattern="[a-z0-9]+@[a-z]{2,}.com"
matcher=fullmatch(pattern,email)
print("invalid email" if matcher==None else "valid email")
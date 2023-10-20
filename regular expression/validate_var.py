from re import*
varname=input("Enter a variable name")
pattern="[a-zA-z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,varname)
if matcher==None:
    print("invalid")
else:
    print("Valid")
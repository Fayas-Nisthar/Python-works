# starting with k,l,m,n
# 2nd that must be digit and divisible by 3
# followed by any num and alph

from re import *
lan=input("Enter a variable name")
pattern="[k-n][369][a-zA-Z0-9]*"
matcher=fullmatch(pattern,lan)
if matcher==None:
    print("invalid")
else:
    print("Valid")

    
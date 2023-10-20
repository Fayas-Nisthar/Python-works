from re import *
text="abcabABC k@&9z"
    # 0123456789
# pattern="[a-c]"    #a or b or c
# pattern="[0-9]" or pattern="\d"
# pattern="\D" #exclude digit "[^0-9]"
# pattern="[a-zA-Z0-9]" #a-z, A-Z, 0-9
# pattern="[^a-z]"   #exclude a-z
# pattern="[^a-zA-z0-9 ]"   #exclude a-z & A-Z & 0-9 & space
pattern="\w"   #alphanumeric values
pattern="\W"    #exclude alphanumeric values. special character

matcher=finditer(pattern,text)  #(start=0 group=a), (start=1 group=b) 
for m in matcher:
    print(m.start(),m.group())
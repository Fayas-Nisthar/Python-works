from re import*
text="abaabcaabaaaa"
# pattern="a+" #atleast one a
# pattern="a*" #matches of any number of a include 0 
# pattern="a?"  #a is optional (not consider as group)
# pattern="a{2}"  #limit group
pattern="a{2,4}"  #min 2, max 4
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

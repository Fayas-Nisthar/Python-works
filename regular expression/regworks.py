text="ababcdABabac"
pattern="ab"
from re import *
matcher=finditer(pattern,text)
count=0
for n in matcher:
    # print(n.start())
    # print(n.group())
    count+=1
print("count=",count)
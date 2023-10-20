lst=[10,14,11,15,12]
elem=int(input("Enter element"))
is_present=False
for i in range(0,len(lst)):
    if lst[i]==elem:
        is_present=True
        break

print(is_present)
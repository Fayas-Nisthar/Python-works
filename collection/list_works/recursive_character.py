text="ABACCD"
lst=[]
dup_lst=[]
for ch in text:
    char_count=lst.count(ch)

    if char_count==0:
        lst.append(ch)
    else:
        dup_lst.append(ch)

print(dup_lst[1])
    

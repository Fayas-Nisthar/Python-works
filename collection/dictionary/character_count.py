text="AABBCAB"
wc={}
for w in text:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
    # print(wc)

for k,v in wc.items():
        if v==3:
            print(k,v)
text="ABCDABB"
wc={}
for w in text:
    if w not in wc:
        wc[w]=1
    else:
        print(w,"is the first recursive character")
        break

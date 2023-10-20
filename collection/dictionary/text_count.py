text="the zoom community provides, a place for meeting provides"
word=text.casefold().replace(",","").split(" ")
wc={}
for w in word:
    if w not in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)

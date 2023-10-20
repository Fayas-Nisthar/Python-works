f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\news.txt")
wc={}
for line in f:
    word=line.rstrip("\n").split( )
    for w in word:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1
print(wc)
f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\news.txt",encoding="utf-8")
p=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\stopword.txt",encoding="utf-8")

stop_w={st.rstrip("\n")for st in p}
news_words=set()

for l in f:
    words=l.split( )
    for w in words:
        news_words.add(w)

print(news_words.difference(stop_w))


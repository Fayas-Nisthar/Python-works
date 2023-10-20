f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\data.txt","r")
print([l.rstrip("\n") for l in f])
f.close
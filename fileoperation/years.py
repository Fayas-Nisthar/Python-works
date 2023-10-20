f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\years.txt","w")
for y in range(1800,2025):
    f.write(str(y)+"\n")
f.close()


y=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\years.txt")

a=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\leapyear.txt","w")

for p in y :
    l=int(p)
    if (l%100==0 and l%400==0) or (l%100!=0 and l%4==0):
        a.write(str(l)+"\n")
y.close
a.close
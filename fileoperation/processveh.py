f_read=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\vehiclenumbers.txt")
f_write=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\kl_num.txt","w")

for line in f_read:
    reg_num=line.strip("\n")

    if reg_num.startswith("kl"):
        f_write.write(str(reg_num)+"\n")
f_write.close()
f_read.close()
f1=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\allstudents.txt")
f2=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\fileoperation\\failed.txt")
all_students={l.rstrip("\n") for l in f1}
failed={f.rstrip("\n") for f in f2}
passed=all_students.difference(failed)
print(passed)
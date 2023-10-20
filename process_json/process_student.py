from json import load
# f=open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\process_json\\student.json")
# data=load(f)
# print(len(data))
# f.close

with open("C:\\Users\\aravi\\OneDrive\\Desktop\\python july\\process_json\\student.json") as f:
    data=load(f)
print(len(data)) 
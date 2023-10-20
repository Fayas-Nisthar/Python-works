students=[
    {"rol":100,"name":"vijay","course":"django","marks":350,"gender":"m"},
    {"rol":101,"name":"ajay","course":"bigdata","marks":450,"gender":"m"},
    {"rol":102,"name":"bijoy","course":"django","marks":400,"gender":"m"},
    {"rol":103,"name":"hari","course":"bigdata","marks":250,"gender":"m"},
    {"rol":104,"name":"jhon","course":"testing","marks":220,"gender":"m"},
    {"rol":105,"name":"tinu","course":"django","marks":280,"gender":"m"},
    {"rol":106,"name":"vinu","course":"testing","marks":290,"gender":"m"},
    {"rol":107,"name":"abin","course":"django","marks":344,"gender":"m"},
    {"rol":108,"name":"riya","course":"bigdata","marks":360,"gender":"f"},
    {"rol":109,"name":"jini","course":"django","marks":480,"gender":"f"},
    {"rol":110,"name":"reshma","course":"testing","marks":200,"gender":"f"},

]

# print(len(students))

# django_students=[stu.get("name") for stu in students if stu.get("course")=="django"]
# print(django_students)

# mark_filter=[stu.get("name") for stu in students if stu.get("marks")>300]
# print(mark_filter)

# gender_filter=[st.get("name") for st in students if st.get("course")=="django" and st.get("gender")=="f"]
# print(gender_filter)

top_stu=max(students,key=lambda st:st.get("marks"))
# print(top_stu)

min_stu=min(students,key=lambda st:st.get("marks"))
# print(min_stu)

srt=sorted(students,reverse=True,key=lambda st:st.get("marks"))
# print(srt)


all_courses=[st.get("course") for st in students]
print(set(all_courses))

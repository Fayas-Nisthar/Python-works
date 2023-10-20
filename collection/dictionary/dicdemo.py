student={"name":"Fayas","roll_no":10,"class":"Python","place":"etpa"}
print (student["name"],student["roll_no"])
print("present" if "place" in student else "not present")
student["age"]=21    #add
print(student)
student["name"]+=" P N"    #update
print(student["name"])
age=int(input("enter age"))
if age<18:
    raise Exception("invalid age")    #custom error
else:
    print("eligible")
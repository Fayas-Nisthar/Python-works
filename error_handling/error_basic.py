# n1=int(input("enter num1 "))
# n2=int(input("enter num2 "))
lst=[10,20,30]
a=int(input("enter index position"))
try:
    print(lst[a])

except Exception as e:
    print(e.args)

# try:
#     res=n1/n2
#     print(f"result={res}")

# except Exception as e:
#     print(e.args)


print("database commit")
print("file transaction")
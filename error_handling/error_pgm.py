n1=int(input("enter num1 "))
n2=int(input("enter num2 "))
try:      #error expecting code
    res=n1/n2
    print(res)
except Exception as e:    #handling code
    print(e.args)

finally:  #must execute
    print("database commit")

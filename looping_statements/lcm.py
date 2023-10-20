num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
lg_num=num1 if num1>num2 else num2
lcm=1
product=num1*num2
for i in range (lg_num,product+1):
    if(i%num1==0) and (i%num2==0):
        lcm=i
        break
print(lcm) 
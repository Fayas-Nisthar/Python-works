num1=int(input("Enetr 1st number"))
num2=int(input("Enter 2nd number"))
# lg_num=num1 if num1>num2 else num2
# print(lg_num)
hcf=1
smallest_num=num1 if num1<num2 else num2 #
for i in range (1,smallest_num+1):
    if(num1%i==0) and (num2%i==0):
        hcf=i
lcm=(num1*num2)//hcf
print(lcm)
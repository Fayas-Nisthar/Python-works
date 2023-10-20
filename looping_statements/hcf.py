num1=int(input("enter 1st number"))#12
num2=int(input("enter 2nd number"))#24
hcf=1
smallest_num=num1 if num1<num2 else num2 #
for i in range (1,smallest_num+1):
    if(num1%i==0) and (num2%i==0):
        hcf=i
print(hcf)
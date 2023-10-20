num=input("Enter number")
dig_leng=len(num)
num=int(num)
orginal=num
sum=0
while(num!=0):
    last_digit=num%10
    power=last_digit**dig_leng
    sum=sum+power
    num=num//10
print("armstrong" if sum==orginal else "not armstrong")






# num2 =24 (2+22)
# num3 =369 (3+33+33)
# num4 =    (4+44+444+4444)
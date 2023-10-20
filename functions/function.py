#add
def add(num1,num2):
    rslt=num1+num2
    return rslt

#product
def mult(num1,num2):
    rslt=num1*num2 
    return rslt
#divi
def divi(num1,num2):
    rslt=num1/num2
    return rslt
# cube
def cube(n):
    rslt=n**3
    return rslt
#sub
def sub(num1,num2):
    rslt=num1-num2
    return rslt

#smart_sub
def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1


#factorial
def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact*=i
        i+=1
    return fact


#leap_year
def leap_year(year):
    if year%100==0 and year%400==0:
        return "centuary leap year"
    elif year%100!=0 and year%4==0:
        return "leap year"
    else:
        return "not a leap year"
    
    
#odd_even
def odd_even(n):
    return "even" if n%2==0 else "odd"

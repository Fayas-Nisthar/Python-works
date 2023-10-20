# def person_name(**kwargs):
#     print(kwargs.values())
# person_name(first_name="sachin",middle_name="ramesh",last_name="tendulkar")


# def emp_details(**kwargs):
#     empname=kwargs.get("name")
#     exp=kwargs.get("exp")
#     dep=kwargs.get("dep")
#     print(f"{empname} has {exp} year experience in {dep}")
# emp_details(name="john",exp="2",dep="web development")


# def balance_enq(**kwargs):
#    name=kwargs.get("bank_name")
#    acno=kwargs.get("acno")
#    balance=kwargs.get("balance")
#    print(f"your {name} {acno} accoount balance is INR {balance}")
# balance_enq(bank_name="sbi",acno="123",balance="23455")

def perform_operation(*args,**kwargs):
   num1,num2=args
   op=kwargs.get("operand")
   if op=="+":
      return num1+num2
   elif op=="-":
      return num1-num2
   else:
      return "invalid operand"
print(perform_operation(10,20,operand="+"))
    
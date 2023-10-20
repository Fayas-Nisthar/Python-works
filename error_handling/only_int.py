val=input("enter number")
# if val.isdigit()==False:
#     raise Exception("only integers allowed")
# else:
#     print ("it's a digit")

if val.isalnum()==False:
    raise Exception("only alpha numeric allowed")
else:
    print("allowed")


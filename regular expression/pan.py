from re import*
# pan=input("Enter pan num")
# pattern="[A-Z]{3}[PCAFHT][A-Z]\d{4}[A-Z]"
# matcher=fullmatch(pattern,pan)
# print("invalid" if matcher==None else "valid")

# ADHAAR
# --------------
# RULE for validate adhaar number  3218 0506 8789 & without space
# adhaar=input("Enter adhaar number")
# pattern="[\d]{4}[\s]?[\d]{4}[\s]?[\d]{4}"
# matcher=fullmatch(pattern,adhaar)
# print("invalid adhaar number" if matcher==None else "valid adhaar number")

# REG NUM
# --------------
#kerala vehicle registration number validate KL-05-D-8600
reg_num=input("Enter vehicle number")
pattern="(KL)[-\s]?[\d]{2}[-\s]?[A-Z]{1,2}[-\s]?[\d]{4}"
matcher=fullmatch(pattern,reg_num)
print("Invalid reg number" if matcher==None else "Valid reg number")
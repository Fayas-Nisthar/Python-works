item={"Brand":"samsung","model":"Galaxy 21","price":30000}
print(item["Brand"])
print("present" if "model" in item else "not present")
item["offer"]=2000
item["price"]-=2000
print(item["price"])



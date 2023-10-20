mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":65000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":45000},

    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},

    ]},
]

# all_mobiles_names=[mob.get("name") for mob in mobiles]
# print(all_mobiles_names)
# all_brands=[brand.get("brand") for brand in mobiles]
# print (set(all_brands))

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price")<35000:
#             print(mob.get("name"))


# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))
#same
price_f=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
print(price_f)

# ram_f=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
# print(ram_f)

# r_p=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="8gb" and v.get("price")<40001]
# print (set(r_p))



prices=[v.get("price") for mob in mobiles for v in mob.get("varients")] 
print(max(prices))

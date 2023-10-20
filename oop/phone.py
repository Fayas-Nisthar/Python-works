data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]

# def get(*args,**kwargs):
#     return data

# def create(*args,**kwargs):
#     data.append(kwargs)
#     return f" {kwargs} created successfully"
    

# def retrive(*args,**kwargs):
#     id=kwargs.get("id")
#     obj=[mob for mob in data if mob.get("id")==id]
#     return obj

#destroy
def destroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()
    data.remove(obj)
    return f"{obj}, removed from db"
#update
def edit(id,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj}, has been updated"

# print(get())
# # print(create(id=105,name="iphone 12",price=3200))
# print(retrive(id=100))
print(destroy(id=100))
print(edit(id=104,price=20000,name="realme neo 3"))


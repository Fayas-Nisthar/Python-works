data=[
    {"id":10,"name":"rich dad","author":"robert"},
    {"id":17,"name":"wings of fire","author":"kalam"},
    {"id":23,"name":"one night","author":"chetan"},
    ]

#list all resources
def get(*args,**kwargs):
    return data

def add_book(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs}, book added successfully" 
def retrive(*args,**kwargs):
    id=kwargs.get("id")
    obj=[bk for bk in data if bk.get("id")==id]
    return obj

print(get())
print(add_book(id=25,name="Book Theif",author="Markus"))
print(retrive(id=17))
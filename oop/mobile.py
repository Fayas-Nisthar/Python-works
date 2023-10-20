class Mobiles:
    data=[
            {"id":100,"name":"galaxya5","price":35000},
            {"id":101,"name":"mi11i","price":25000},
            {"id":102,"name":"iphone15","price":135000},
            {"id":103,"name":"s23","price":145000},
            {"id":104,"name":"neo","price":35000},
        ]


    def get(self,**kwargs):
        return self.data

    def create(self,**kwargs):
        self.data.append(kwargs)
        return f"{kwargs}, created successfully"
    
    def retrieve(self,id,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        return obj
    

    def put(self,id,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        obj.update(kwargs)
        return f"{obj},updated"
    
    def destroy(self,id,**kwargs):
        obj=[m for m in self.data if m.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj},removed successfully"
    


obj=Mobiles()
# print(obj.get())
# print(obj.create(id=106,name="pocof1",price=30000))
# print(obj.retrieve(id=103))
# print(obj.put(id=104,name="iq neo 3"))
print(obj.destroy(id=103))


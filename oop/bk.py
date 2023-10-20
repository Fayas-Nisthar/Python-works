class Book:
    data=[
    {"id":10,"name":"rich dad","author":"robert"},
    {"id":17,"name":"wings of fire","author":"kalam"},
    {"id":23,"name":"one night","author":"chetan"},
    ]

    def display(self):
        return self.data

    def create(self,**kwargs):
        self.data.append(kwargs)
        return f" {kwargs} added successfully"
    
    def delete(self,id):
        obj=[b for b in self.data if b.get("id")==id].pop()
        self.data.remove(obj)
        return f" {obj} successfully deleted"
    
    def retrieve(self,id):
        obj=[b for b in self.data if b.get("id")==id].pop()
        return obj
    
    def put(self,id,**kwagrs):
        obj=[b for b in self.data if b.get("id")==id].pop()
        obj.update(**kwagrs)
        return f"{obj} updated successfully"

obj=Book()
# print(obj.display())
# print(obj.create(id=108,name="Gitanjali",author="Tagore"))
# print(obj.delete(id=17))
# print(obj.retrieve(id=17))
print(obj.put(id=17,author="abdul kalam"))

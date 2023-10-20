class Book:
    name:str
    author:str
    price:int 
    publisher:str
    def set_book(self,name,author,price,publisher):
        #initializing instance variable
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher
    def display(self):
        print(self.name,self.author,self.price,self.publisher)
    def __str__(self):    #toString() object string representation __str__
        return self.name
    
bk1=Book()
bk1.set_book("Rich Dad Poor Dad","Robert",300,"Plata")
print(bk1)
bk1.display()
bk2=Book()
bk2.set_book("Glimpses of world","Nehru",500,"A&C")
bk2.display()
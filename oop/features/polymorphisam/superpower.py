class SuperHero:
    def __init__(self,name):
        self.name=name

    def super_power(self):
        context=["run","jump"]
        return context
class Spiderman(SuperHero):
    def super_power(self):                         #overriding
        self.context=super().super_power()
        self.context.append("fly")
        return self.context
class MinnalMuraly(SuperHero):
    def super_power(self):
        self.context=super().super_power()
        self.context.append("speed")
        return self.context
    
obj=Spiderman("spiderman")
print (obj.super_power())
obj1=MinnalMuraly("minnal")
print(obj1.super_power())

class Animal:
    name:str
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks")
    def __str__(self):
        return self.name
class Frog(Animal):
    def sound(self):
        print(f"{self.name} croaks")

dobj=Dog("Dog")
print(dobj)
dobj.sound()
fobj=Frog("Frog")
fobj.sound()

print(fobj.__class__)
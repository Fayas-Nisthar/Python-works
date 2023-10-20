class Parent:
    def mobile(self):
        print("Samsung S20FE")
    def car(self):
        print("Creta")

class Child(Parent):
    def mobile(self):
        print("iphone 15")
obj=Child()
obj.mobile()
obj.car()
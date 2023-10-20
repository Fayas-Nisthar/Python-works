class Parent:
    def mobile(self):
        print("samsung s21fe")
    def bike(self):
        print("passion pro")

class Child(Parent):
    pass

obj=Child()
obj.mobile()
obj.bike()
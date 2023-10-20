class P1:
    def m1(self):
        print("inside parent 1")
class P2:
    def m1 (self):
        print("inside parent 2")
class C(P2,P1):    #multiple inheritance
    def m3(self):
        print("inside child")

obj=C()
obj.m1()    #interpreter
# obj.m2()
obj.m3()
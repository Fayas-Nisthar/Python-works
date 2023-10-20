class P1:
    def m1(self):
        print("inside parent 1")
class P2(P1):                          
    def m2 (self):
        print("inside parent 2")                                #multilevel inheritance
class C(P2):    
    def m3(self):
        print("inside child")

obj=C()
obj.m1()    #interpreter
obj.m2()
obj.m3()
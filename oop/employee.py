class Employee:
    id:int
    name:str
    dep:str
    salary:int
    company_name:str="UST"
    def set_employee(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.dep=dep
        self.salary=sal

    def display(self):
        print(self.id,self.name,self.dep,self.salary,Employee.company_name)
    def __str__(self):
        return (self.name)

obj1=Employee()
obj1.set_employee(10,"Akash","Manager",40000)
print(obj1)
obj1.display()
obj2=Employee()
obj2.set_employee(11,"Prakash","Staff",20000)
obj2.display()


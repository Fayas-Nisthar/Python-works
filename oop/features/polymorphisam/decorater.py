# decorater can used for method access like property

class Employee:
    def __init__(self,name,salary,dep):
        self.name=name
        self.salary=salary
        self.dep=dep
    @property     #decorater
    def get_name(self):
        return self.name
    @property
    def get_salary(self):
        return self.salary
emp=Employee("Hari",40000,"HR")
print(emp.get_salary)
print(emp.get_name)
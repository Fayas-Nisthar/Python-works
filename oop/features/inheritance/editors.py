class Editors:
    name:str
    def __init__(self,name):
        self.name=name
    def spec(self):
        pass
class VsCode(Editors):
    def spec(self):
        print(f"{self.name} supports edit,debug,run, extension support")
    def __str__(self):
        return self.name

class Pycharm(Editors):
    def spec(self):
        print(f"{self.name} supports edit, debug,run")
    
vobj=VsCode("Vscode")
vobj.spec()
print(vobj)
pobj=Pycharm("Pycharm")
pobj.spec()
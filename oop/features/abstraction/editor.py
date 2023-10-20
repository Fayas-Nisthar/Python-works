from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def debug(self):
        pass
class VsCode(Editor):
    def edit(self):
        print("Vscode edit")
    def run(self):
        print("vscode run")
    def debug(self):
        print("vscode debug")

obj=VsCode()
obj.edit()
# abstraction hide implementation details

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Swift(Car):
    def start(self):
        print("Swift start method")
    def accelerate(self):
        return ("Swift accelerate method")
    def stop(self):
        print("swift stop method")
obj=Swift()
obj.start()
print(obj.accelerate())

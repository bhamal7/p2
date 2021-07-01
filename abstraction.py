#An abstract class can be considered as a blueprint for other classes. 
# It allows you to create a set of methods that must be created within any child classes built from the abstract class

from abc import ABC,abstractmethod
class Base(ABC):

    @abstractmethod #abstract method— methods having definition but no implementation
    def Eat(self):
        pass
class lion():
    # overriding abstract method
    def eat(self):
        print("Lion eat deer")
    
class deer():
    # overriding abstract method
    def eat(self):
        print("Deer eat grass")

class dog():
    # overriding abstract method
    def eat(self):
        print("Dog eat bones")

obj_lion = lion()
obj_deer = deer()
obj_dog = dog()

obj_lion.eat()
obj_deer.eat()
obj_dog.eat()

#A class is a blueprint that defines the variables and the methods (Characteristics) common to all objects of a certain kind.

class First:
    #initialize a constructor
    kind = 'Human'    # this is class variable assign inside the class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #name , age are instance variable which assign inside the constructor and method

    #define a method
    def Method(self):
        return f"my name is {self.name} and age is {self.age}"
    
    #define a second method
    def Method2(self, height):
        self.height = height
        return f"My naem is {self.name} and age is {self.age} and height is {self.height}"


obj1 = First("bishal",12)
obj2 = First("Ram",23)
print(obj1.Method())
print(obj2.Method2(12))
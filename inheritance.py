#Inheritance is the capability of one class to derive or inherit the properties from another class.
class Parent():
    #initialize the constructor 
    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    #define one method
    def Method(self):
        print(self.firstName,self.lastName)  

class Child(Parent):
    #initialize the constructor 
    def __init__(self, firstName, lastName, age):
        Parent.__init__(self,firstName, lastName) # this line can also be written as super().__init__(firstName,lastName)
        self.age = age
    def Method1(self):
        print("Child class also has age and it is",self.age)

obj1 = Child('Bishal','Hamal',23)
obj1.Method()
obj1.Method1()
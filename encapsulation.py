#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variable. 
#A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
# Python program to
# demonstrate protected members
 
 
# Creating a base class
class Sales():
    #define a constructor
    def __init__(self,carType):
        self.carType = carType
        self._color = "blue"

    def Officer(self):
        print("I am officer and I can only tell u the color which is",self._color)

class Finance(Sales):
    def __init__(self,carType,model):
        self.model = model
        super().__init__(carType) #invoking the super class or base class

    #define a method
    def Print(self):
        print(self.carType,self.model)
obj_Finance = Finance('Honda','Accord')
obj_Finance.Print()
obj_Sales = Sales(carType='BMW')
#lets try can we access the color outside the class
#print(obj_Sales.color) it makes a error becauseSales' object has no attribute 'color'
obj_Sales.Officer()

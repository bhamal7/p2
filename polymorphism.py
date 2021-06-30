#The word polymorphism means having many forms. In programming, 
# polymorphism means same function name (but different signatures) being uses for different types.

#example 1 simple
def add(x,y=1,z=2):
    return x+y+z

print(add(1))
print(add(1,2))
print(add(2,2,2))

#exmple 2 using class and method
class Nepal():
    def Capital(hi):
        print("The capital of Nepal is Kathmandu")
    def Language(hi):
        print("The language spoken in Nepal is Nepali")
    def Develope(hi):
        print("Nepal is developing country")

class USA():
    def Capital(hi):
        print("The capital of USA is Washiton DC")
    def Language(hi):
        print("The language spoken in USA ia English")
    def Develope(hi):
        print("USA is developed country")
obj_nepal = Nepal()
obj_usa = USA()

obj_nepal.Capital()
obj_nepal.Language()
obj_nepal.Develope()

obj_usa.Capital()
obj_usa.Language()
obj_usa.Develope()

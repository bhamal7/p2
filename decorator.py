#the decorators are used to modify the behavior of function or class. 
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

def decorator(func):
    #lets define the inner wrapper function 
    def wrapper():
        print("This is wrapper function before the function execute.")
        #now calling the argument functions
        func()

        print("This is after function execution")
    
    return wrapper

#function to be used as argument
def argument():
    print("This is the argument function.")


obj = decorator(argument)
obj()


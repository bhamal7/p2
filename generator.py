 #A generator-function is defined like a normal function, but whenever it needs to generate a value, it does 
 # so with the yield keyword rather than return. 
 # If the body of a def contains yield, the function automatically becomes a generator function.

def Generator1():
    i = 1
    while True:
        yield i*i
        i+=1

for i in Generator1():
    if i > 100:
        break
    print(i)

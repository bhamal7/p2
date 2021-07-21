# #
# x = lambda x: x*2
# print(x(9))
# #
# #make odd list from one to 20
# list_1to20 = [x for x in range(1,21)]
# odd_list = filter(lambda i: i %2 == 1,list_1to20)
# print(list(odd_list))

# #
# def Hi():
#     y = lambda a,b,c: a*b*c
#     return y
# z =Hi()
# print(z(1,3,3)) 

def lam(x,y,z):
    l = lambda x,y,z: x+y+z
    yield l 
x = lam(1,2,3)
for i in x:
    print(i)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("I like {} but dont like {}".format(thislist[0],thislist[4]))
print(thislist[::-1])
print(thislist[:3])
newlist = [x for x in thislist if "a" in x]
print(newlist)

num = [1,2,3,4,5,6,7,8,9,10]
print([x for x in num if x%2==0])

num = (1,2,3,4,5,6,7,8,9,10)
print(tuple([x for x in num if x%2==0]))

evenlist = filter(lambda i: i%2 == 0,num)
print(list(evenlist))

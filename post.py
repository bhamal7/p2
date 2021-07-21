
  
# x= "there is an interview"
# "ereht si na weivretni"
# for i in x.split(' '):
#     print(''.join(reversed(i)),end=' ')

# items=["biscuits","cakes","popcorns"]
# prices=[10,20,30]
# output={"biscuits":10,"cakes":20,"popcorns":30}
# print(dict(zip(items,prices)))

input="aaabbbbbccd"
#output={'a':3,'b':5,'c':2,'d':1}
x={}
for i in input:
    x[i]=input.count(i)
print(x)
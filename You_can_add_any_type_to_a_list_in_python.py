data=[]
# you can add data of any type to a list in python

data.append(123)# number
data.append("Hi") # String
data.append(1+2j)  # Complex
class C:
    pass
o = C()
data.append(o) # object

for x in data :
    print(x)

'''In python, the same list can keep elements that belong to diffrent data
type.'''
'''Here in this example,a number, a string complex number and later an
instance of a class are appended to the same list'''

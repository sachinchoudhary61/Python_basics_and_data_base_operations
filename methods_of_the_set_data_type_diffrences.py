# Method of the "set" data type "difference"
set1 = {1,2,3,4,5,6,7}

set2= {3,5,7,9,11,13}

diff1 = set1.difference(set2)
# kind of "set1 - set2"
diff2 = set2.difference(set1)
# "set2 - set1", different result

print(diff1)
print(diff2)

'''The "set" data type in python has the "differences" method. It returns
the new set containing from the elements that are in the first set but are
absent in the second.'''
'''Notice that a.differences(b) is not the same as b.differences(a)'''

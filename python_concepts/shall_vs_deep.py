original = [1, 2, 4]

copy = original
copy.append(9)
print (copy)
print (id(original))
print (original)
print (id(copy))
print (original is copy)
print (original == copy)

#demo

import copy
original = [ 1, 5, 8, 9, 12, 23,[3, 6, 9, 14]]
copy1 = copy.copy(original)
print (copy1)

copy2 = copy.deepcopy(original)
#print (copy2)
copy2[6][2] = "abc"
print (copy2)
print (original)
#take an arg, it will be int,
#make a list from o to N

list = lambda n:[i for i in range(0, n) if i % 2 == 0]
list1 = list(15)
print (f"{list1 = }")

'''
def add(*args):
    total = 0
    for arg in args:
        if type(arg) == int:
            total += arg
        elif type(arg) == list:
            for l in arg:
                total += l
    print (total)

#add(1, 2, [3, 4])
#add(1, 2, [3, 4, 100, 234], 23, 44, 77)


def add(**kwargs):
    for k, v in kwargs.items():
        print (k, v)
    print(f"{kwargs}")

add(name="gipson", age="22", gender="male")
'''

add_nums = lambda n1, n2, n3: n1 + n2 + n3

print (add_nums(1, 2, 3))
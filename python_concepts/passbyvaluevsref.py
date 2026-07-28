def add_number(x):
    x = x + 1
    print (f"Inside function = {x}")

num = 5
add_number(num)
print (f"Outside function value = {num}")

def add_item(x):
    x.append(100)
    print (f"Inside function {x}")

list = [1, 3, 5, 8]
add_item(list)
print (f"Outside function value = {list}")

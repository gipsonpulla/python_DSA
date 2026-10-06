'''
def greet():
    name = input("Enter the name")
    print (f"Hi {name}")

name = "xyz"
greet()
print (name)
'''

list = [ 1, 2, 3, 4, 5]
def add_list(list):
    total = 0
    for i in list:
        total += i
    return total

print (add_list(list))

def add (n1, n2):
    total = n1 + n2
    return total

def check(num):
    if num % 2 == 0:
        print ("Even")
    else:
        print ("Odd")
x = int(input("Enter number 1 ="))
y = int(input("Enter number 2 = "))
num = add (x, y)
check(num)


def add_num(x: int, y: int) -> int:
    return x + y

print (add_num(5, 6))

def cal_max(x: int, y: int, z: int) -> None:
    print (f"Max number of x, y, z is {max(x, y, z)}")

cal_max(5, 7, 9)

def max_marks(marks: list[int]) -> int:
    return max(marks)

marks = [65, 87, 98, 79]
print (max_marks(marks))

def print_list(lst: list[int | str]):
    print(lst)

lst = [234, 344, 223, 556, "abc",  54.33]
print_list(lst)

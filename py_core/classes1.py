class Student:
    def __init__(self) -> None:
        self.name = input("Enter the name")
        self.age = input("Enter the age")
    def info(self):
        print (f"{self.name}")
        print (f"{self.age}")

s1 = Student()
s1.name = "Gipson"
s1.age = "22"
s1.info()
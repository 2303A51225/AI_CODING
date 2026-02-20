# # class Student:
# #     def __init__(self, name, roll_no, marks):
# #         self.name = name
# #         self.roll_no = roll_no
# #         self.marks = marks

# #     def is_pass(self):
# #         return self.marks >= 40
# # s1 = Student("Mukesh", 101, 75)
# # s2 = Student("Ravi", 102, 35)

# # print(s1.name, "Pass Status:", s1.is_pass())
# # print(s2.name, "Pass Status:", s2.is_pass())
# # def triangle_for(n):
# #     for i in range(1, n+1):
# #         print("*" * i)

# # n=5
# # print(triangle_for(n))
# # def check_number(num):
# #     if num > 0:
# #         return "Positive"
# #     elif num < 0:
# #         return "Negative"
# #     else:
# #         return "Zero"


# # # Testing
# # print(check_number(10))
# # print(check_number(-5))
# # print(check_number(0))
# # def check_discount(age, is_member):
# #     if age >= 60:
# #         print("Eligible for Senior Discount")
# #         if is_member:
# #             print("Eligible for Additional Member Discount")
# #     else:
# #         if is_member:
# #             print("Eligible for Member Discount Only")
# #         else:
# #             print("No Discount")


# # # Testing
# # check_discount(65, True)
# # check_discount(30, True)
# # check_discount(25, False)
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def circumference(self):
#         return 2 * math.pi * self.radius


# # Testing
# c1 = Circle(7)

# print("Area:", c1.area())
# print("Circumference:", c1.circumference())



#generate python code for  simple calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    else:
        print("Invalid Input")
#generate testcase for above code
# Test cases for the simple calculator functions
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0
    
def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0
    
def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error! Division by zero."
    assert divide(-10, -2) == 5
    
# Run test cases

test_add()
test_subtract()         
test_multiply()
test_divide()
print("All test cases passed!")
#generate unique testcase for above code
def test_add_unique():
    assert add(1.5, 2.5) == 4.0
    assert add(-3, -7) == -10
    assert add(100, 200) == 300 
def test_subtract_unique():
    assert subtract(10, 5) == 5
    assert subtract(-5, -10) == 5
    assert subtract(0, 0) == 0

def test_multiply_unique():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    
def test_divide_unique():           
    assert divide(15, 3) == 5
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0
    
# Run unique test cases
test_add_unique()       
test_subtract_unique()
test_multiply_unique()
test_divide_unique()
print("All unique test cases passed!")

#  Multi line comment in Python is done using triple quotes. It can be used to write comments that span multiple lines. It is also used to write docstrings, which are used to document functions, classes, and modules.

#  '''
#  This is a multi line comment in Python. It can be used to write comments that span multiple lines. It is also used to write docstrings, which are used to document functions, classes, and modules.'''

# keywords_in_Python = ["if", "else", "elif", "for", "while", "break", "continue", "pass", "def", "return", "import", "from", "as", "class", "try", "except", "finally", "with", "lambda", "global", "nonlocal", "assert", "yield"]
# print(keywords_in_Python)

# input from user
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# #addition
# c = a + b
# print("The sum of", a, "and", b, "is", c)

# def add():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     return a + b

# def add_multiple_numbers():
#     n = int(input("Enter how many numbers you want to add: "))
#     total = 0
#     for i in range(n):
#         num = int(input(f"Enter number {i+1}: "))
#         total += num
#     return total

# print("This is a function that adds two numbers.")
# print("You can call this function multiple times to add different pairs of numbers.")
# print(add())
# print("\nFunction to add multiple numbers:")
# print(add_multiple_numbers())

# age user se lene hai check karna hai ki user ka age 18 se zyada hai ya nahi. if user is 18 or older ask for the user's voter id card 

# age = int(input("Enter your age: "))
# if age >= 18:
#     voterID = input("Do you have a voter ID card? (yes/no): ")
#     if voterID == "yes" or voterID == "Yes" or voterID == "YES" or voterID == "y" or voterID == "Y":
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote without a voter ID card.")
# else:
#     print("You are not eligible to vote as you are under 18 years old.")

#Loops in Python are used to execute a block of code repeatedly as long as a certain condition is met. There are two main types of loops in Python: for loops and while loops.

n = int(input("Enter a number: "))
for i in range(1, n+1): # range(starting number, ending number(starting number + 1), step)
    print(i)
# # List 
# # Dictionary
# # Tuple 
# # Set 

# # List: A list is a collection of items that are ordered and changeable. It allows duplicate members. Lists are defined by square brackets [].
# '''
# List:
# 1. Ordered: The items in a list have a defined order, and that order will not change unless you explicitly do so.
# 2. Changeable: You can change, add, and remove items in a list after it has been created.
# 3. Allows duplicate members: Since lists are indexed, lists can have items with the same value. [1,2,3,1,2,3] is a valid list.
# Types: 
# 1. Empty list: An empty list is a list that contains no items. It is defined by using empty square brackets [].
# 2. Long List: A long list is a list that contains many items. It can be defined by using square brackets [] and separating the items with commas.
# 3. Nested List: A nested list is a list that contains other lists as its items.
# Example:
# 1. Empty list: []
# 2. Long list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# 3. Nested list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# '''

# l1 = [] # Empty list
# l2 = [1, 2, 3, 4, 5] # Non-empty list
# l3 = list(range(1, 101)) # Long list generated from 1 to 100
# print(l3)
# print(l1)
# print(l2)

# #user input se list banani hai aur usme se even numbers print karne hai.
# # n = int(input("Enter the number of elements in the list: "))
# # l4 = []
# # for i in range(n):
# #     element = int(input(f"Enter element {i+1}: "))
# #     l4.append(element)
# # print("Even numbers in the list are:")
# # for num in l4:
# #     if num % 2 == 0:
# #         print(num)
# # user input se list banani hai aur usme se range, data type, aur mixed type ka option bhi hoga.
# print("\nCreate a custom list with range and data type selection.")

# available_types = ["int", "float", "str", "mixed"]
# while True:
#     selected_type = input("Enter the data type for the whole list (int, float, str, mixed): ").strip().lower()
#     if selected_type in available_types:
#         break
#     print("Please choose one of: int, float, str, mixed.")

# use_range = False
# if selected_type in ("int", "float"):
#     answer = input("Do you want to generate the list from a range? (yes/no): ").strip().lower()
#     use_range = answer.startswith("y")

# l5 = []
# if use_range:
#     if selected_type == "int":
#         start = int(input("Enter the start of the range: "))
#         end = int(input("Enter the end of the range: "))
#         step_input = input("Enter the step for the range (default 1): ").strip()
#         step = int(step_input) if step_input else 1
#         if step == 0:
#             step = 1
#         if step > 0:
#             end_value = end + 1
#         else:
#             end_value = end - 1
#         l5 = list(range(start, end_value, step))
#     else:
#         start = float(input("Enter the start of the range: "))
#         end = float(input("Enter the end of the range: "))
#         step_input = input("Enter the step for the range (default 1.0): ").strip()
#         step = float(step_input) if step_input else 1.0
#         if step == 0.0:
#             step = 1.0
#         current = start
#         if step > 0:
#             while current <= end:
#                 l5.append(current)
#                 current += step
#         else:
#             while current >= end:
#                 l5.append(current)
#                 current += step
# else:
#     n = int(input("Enter the number of elements in the list: "))
#     for i in range(n):
#         element = input(f"Enter element {i+1}: ")
#         if selected_type == "int":
#             l5.append(int(element))
#         elif selected_type == "float":
#             l5.append(float(element))
#         elif selected_type == "str":
#             l5.append(element)
#         else:
#             try:
#                 l5.append(int(element))
#             except ValueError:
#                 try:
#                     l5.append(float(element))
#                 except ValueError:
#                     l5.append(element)

# print("\nFinal list:", l5)
# if selected_type == "mixed":
#     print("Mixed data type list detected. Elements may include int, float, and str.")

# integer_items = [item for item in l5 if isinstance(item, int)]
# if integer_items:
#     even_numbers = [num for num in integer_items if num % 2 == 0]
#     odd_numbers = [num for num in integer_items if num % 2 != 0]
#     print("Odd numbers in the list are:", odd_numbers)
#     print("Even numbers in the list are:", even_numbers)
# else:
#     print("No integer values found in the list to classify as odd or even.")

#Dictionary: A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are defined by curly braces {}.
'''
1. Unordered: The items in a dictionary do not have a defined order, and that order may change.
2. Changeable: You can change, add, and remove items in a dictionary after it has been created.
3. Indexed: Dictionaries are indexed by keys, which can be of any immutable type (like strings, numbers, or tuples). Each key is unique within a dictionary.
Types:
1. Empty dictionary: An empty dictionary is a dictionary that contains no items. It is defined by using empty curly braces {}.
2. Long dictionary: A long dictionary is a dictionary that contains many key-value pairs. It
 can be defined by using curly braces {} and separating the key-value pairs with commas.
3. Nested dictionary: A nested dictionary is a dictionary that contains other dictionaries as its values.'''

d1 = {} # Empty dictionary
d2 = {"name": "Alice", "age": 30, "city": "New York"} # Non-empty dictionary
d3 = {i: i**2 for i in range(1, 11)} # Long dictionary generated from 1 to 10 with squares as values
d4 = {"person1": {"name": "Bob", "age": 25}, "person2": {"name": "Charlie", "age": 35}} # Nested dictionary
print(d1)
print(d2)
print(d3)
print(d4)
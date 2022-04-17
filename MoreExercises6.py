# 01. Rectangle of 10 x 10 Stars
# for i in range(0, 10):
#     for j in range(0, 10):
#         print("*", end="")
#     print()

# 02. Rectangle of N x N Stars
# command_input = int(input())
# for i in range(0, command_input):
#     for j in range(0, command_input):
#         print("*", end="")
#     print()

# 03. Square of Stars
# command_input = int(input())
# for i in range(0, command_input):
#     for j in range(0, command_input):
#         print("*", end=" ")
#     print()

# 04. Triangle of Dollars
# command_input = int(input())
# for i in range(1, command_input + 1):
#     for j in range(0, i):
#         print("$", end=" ")
#     print()

# 05. Square Frame
# command_input = int(input())
# for i in range(1, command_input + 1):
#     for j in range(1, command_input + 1):
#         if i == 1 and j == 1:
#             print("+", end=" ")
#         elif i == 1 and j == command_input:
#             print("+", end=" ")
#         elif i == command_input and j == 1:
#             print("+", end=" ")
#         elif i == command_input and j == command_input:
#             print("+", end=" ")
#         elif j == 1 or j == command_input:
#             print("|", end=" ")
#         else:
#             print("-", end=" ")
#     print()

# 06. Rhombus of Stars
# command_input = int(input())
# for i in range(1, command_input + 1):
#     if i == 1:
#         print(f"{' ' * (command_input - i)}*")
#     elif i == command_input:
#         print(f"{'* ' * (command_input - 1)}*")
#     else:
#         print(f"{' ' * (command_input - i)}*", "* " * (i - 1))
# for i in range(command_input - 1, 0, -1):
#     if i == 1:
#         print(f"{' ' * (command_input - i)}*")
#     else:
#         print(f"{' ' * (command_input - i)}*", "* " * (i - 1))

# 07. Christmas Tree
height_of_tree = int(input())
for i in range(height_of_tree, -1, -1):
    print(f"{' ' * i}{'*' * (height_of_tree - i)} | {'*' * (height_of_tree - i)}")

# 08. Sunglasses

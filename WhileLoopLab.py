# 01. Read Text
# command_text = input()
# while command_text != "Stop":
#     print(command_text)
#     command_text = input()

# 02. Password
# command_name = input()
# command_password = input()
# command_input = input()
# while command_input != command_password:
#     command_input = input()
# print(f"Welcome {command_name}!")

# 03. Sum Numbers
# first_number = int(input())
# sum_of_numbers = 0
# while sum_of_numbers < first_number:
#     sum_of_numbers += int(input())
# print(sum_of_numbers)

# 04. Sequence 2k+1
# number_input = int(input())
# max_number = 1
# while max_number <= number_input:
#     print(max_number)
#     max_number = (max_number * 2) + 1

# 05. Account Balance
# transaction_input = ""
# transaction_input_number = 0
# total_balance = 0
# while transaction_input != "NoMoreMoney":
#     transaction_input = input()
#     if transaction_input == "NoMoreMoney":
#         print(f"Total: {format(total_balance, '.2f')}")
#         break
#     if float(transaction_input) > 0:
#         transaction_input_number = float(transaction_input)
#         print(f"Increase: {format(transaction_input_number, '.2f')}")
#         total_balance += transaction_input_number
#     else:
#         print("Invalid operation!")
#         print(f"Total: {format(total_balance, '.2f')}")
#         break

# 06. Max Number
# command_input = input()
# input_to_number = []
# while command_input != "Stop":
#     input_to_number += [int(command_input)]
#     command_input = input()
# print(max(input_to_number))

# 07. Min Number
# command_input = input()
# input_to_number = []
# while command_input != "Stop":
#     input_to_number += [int(command_input)]
#     command_input = input()
# print(min(input_to_number))

# 08. Graduation pt.2
# name_of_student = input()
# failed_counter = 0
# year_average = 0
# passed_years = 0
# total_grades = 0
# while passed_years < 12:
#     year_average = float(input())
#     passed_years += 1
#     if year_average < 4:
#         failed_counter += 1
#         passed_years -= 1
#     if failed_counter > 1:
#         passed_years += 1
#         print(f"{name_of_student} has been excluded at {passed_years} grade")
#         break
#     elif year_average >= 4:
#         total_grades += year_average
# if passed_years >= 12:
#     print(f"{name_of_student} graduated. Average grade: {total_grades / 12:.2f}")

# 09. Moving
width = int(input())
depth = int(input())
height = int(input())
volume_of_condo = width * depth * height
number_of_boxes = ""
number_of_boxes_int = 0
while volume_of_condo >= 0:
    number_of_boxes = input()
    if number_of_boxes == "Done":
        break
    else:
        number_of_boxes_int = int(number_of_boxes)
        volume_of_condo -= number_of_boxes_int
if volume_of_condo >= 0:
    print(f"{volume_of_condo} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume_of_condo)} Cubic meters more.")

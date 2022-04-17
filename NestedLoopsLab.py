# 01. Clock
# for h in range(0, 24):
#     for m in range(0, 60):
#         print(f"{h}:{m}")

# 02. Multiplication Table
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

# 03. Combinations
# number_input = int(input())
# combination_count = 0
# for i in range(0, number_input+1):
#     for j in range(0, number_input+1):
#         for k in range(0, number_input+1):
#             if i + j + k == number_input:
#                 combination_count += 1
# print(combination_count)

# 04. Sum of Two Numbers
# begin_number = int(input())
# end_number = int(input())
# magical_number = int(input())
# combination_count = 0
# is_found = False
# for i in range(begin_number, end_number+1):
#     for j in range(begin_number, end_number+1):
#         combination_count += 1
#         if i + j == magical_number:
#             print(f"Combination N:{combination_count} ({i} + {j} = {magical_number})")
#             is_found = True
#             break
#     if is_found:
#         break
# if is_found is False:
#     print(f"{combination_count} combinations - neither equals {magical_number}")

# 05. Travelling
# command = input()
# savings = 0
# while command != "End":
#     minimal_budget = float(input())
#     while savings < minimal_budget:
#         savings += float(input())
#     print(f"Going to {command}!")
#     savings = 0
#     command = input()

# 06. Building
# number_of_floors = int(input())
# number_of_rooms = int(input())
# for a in range(number_of_floors, 0, -1):
#     print()
#     for b in range(0, number_of_rooms):
#         if a == number_of_floors:
#             print("L"+str(a)+str(b), end=' ')
#         elif a % 2 == 0:
#             print("O"+str(a)+str(b), end=' ')
#         else:
#             print("A"+str(a)+str(b), end=' ')

# 07. Cinema Tickets
command = input()
available_seats = 0
type_of_ticket = ""
used_seats = 0
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
total_ticket = 0
total_student = 0
total_standard = 0
total_kid = 0
while command != "Finish":
    available_seats = int(input())
    type_of_ticket = input()
    while used_seats < available_seats and type_of_ticket != "End":
        if type_of_ticket == "student":
            student_ticket += 1
            total_student += 1
        elif type_of_ticket == "standard":
            standard_ticket += 1
            total_standard += 1
        elif type_of_ticket == "kid":
            kid_ticket += 1
            total_kid += 1
        used_seats += 1
        total_ticket += 1
        if used_seats < available_seats:
            type_of_ticket = input()
        elif type_of_ticket == "Finish":
            break
    print(f"{command} - {((used_seats / available_seats) * 100):.2f}% full.")
    student_ticket = 0
    standard_ticket = 0
    kid_ticket = 0
    used_seats = 0
    if type_of_ticket == "Finish":
        break
    command = input()
print(f"Total tickets: {total_ticket}")
print(f"{((total_student / total_ticket) * 100):.2f}% student tickets.")
print(f"{((total_standard / total_ticket) * 100):.2f}% standard tickets.")
print(f"{((total_kid / total_ticket) * 100):.2f}% kids tickets.")

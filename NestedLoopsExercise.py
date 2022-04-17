# 01. Number Pyramid
# n = int(input())
# row = 0
# column = 0
# current = 1
# is_current_bigger_than_n = False
# for row in range(1, n+1):
#     for column in range(1, row+1):
#         if current > n:
#             is_current_bigger_than_n = True
#             break
#         print(str(current)+' ', end='')
#         current += 1
#     if is_current_bigger_than_n:
#         break
#     print()

# 02. Equal Sums Even Odd Position
# number_1 = int(input())
# number_2 = int(input())
# for i in range(number_1, number_2+1):
#     number_to_str = str(i)
#     even_sum = 0
#     odd_sum = 0
#
#     for index, digit in enumerate(number_to_str):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#
#     if even_sum == odd_sum:
#         print(i, end=' ')

# 03. Sum Prime Non Prime
# command_number = input()
# prime_sum = 0
# non_prime_sum = 0
# while command_number != "stop":
#     int_number = int(command_number)
#     if int_number < 0:
#         print("Number is negative.")
#     else:
#         for i in range(2, int_number):
#             if (int_number % i) == 0:
#                 non_prime_sum += int_number
#                 break
#         else:
#             prime_sum += int_number
#     command_number = input()
# print(f"Sum of all prime numbers is: {prime_sum}")
# print(f"Sum of all non prime numbers is: {non_prime_sum}")

# 04. Train The Trainers
# number_of_jury = int(input())
# name_of_presentation = input()
# grade_total = 0
# grand_total = 0
# grand_counter = 0
# command = ""
# average_grade = 0
# while command != "Finish":
#     for i in range(1, number_of_jury+1):
#         grade = float(input())
#         grade_total += grade
#         grand_total += grade
#         grand_counter += 1
#         average_grade = grade_total / number_of_jury
#     print(f"{name_of_presentation} - {average_grade:.2f}.")
#     grade_total = 0
#     average_grade = 0
#     command = input()
#     if command != "Finish":
#         name_of_presentation = command
# print(f"Student's final assessment is {grand_total/grand_counter:.2f}.")

# 05. Password Generator
# number_one = int(input())
# number_two = int(input())
# ascii_point_start = 97
# ascii_point_end = 97 + number_two
# for n in range(1, number_one):
#     for m in range(1, number_one):
#         for l in range(ascii_point_start, ascii_point_end):
#             for k in range(ascii_point_start, ascii_point_end):
#                 if n > m:
#                     z_target = n
#                 else:
#                     z_target = m
#                 for z in range(z_target+1, number_one+1):
#                     print(str(n)+str(m)+chr(l)+chr(k)+str(z), end=' ')

# 06. Special Numbers
number_input = int(input())
for a in range(1, number_input + 1):
    if number_input % a == 0:
        first_number = a
        for b in range(1, number_input + 1):
            if number_input % b == 0:
                second_number = b
                for c in range(1, number_input + 1):
                    if number_input % c == 0:
                        third_number = c
                        for d in range(1, number_input + 1):
                            if number_input % d == 0:
                                fourth_number = d
                                if int(str(a) + str(b) + str(c) + str(d)) <= 9999:
                                    print(str(a) + str(b) + str(c) + str(d), end=' ')
n = int(input())
for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if n % num1 == 0 and n % num2 == 0 and n % num3 == 0 and n % num4 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")

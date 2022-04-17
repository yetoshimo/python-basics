# 01. Old Books
# book_you_search = input()
# checked_book_name = ""
# checked_books = 0
# while checked_book_name != book_you_search:
#     checked_book_name = input()
#     if checked_book_name != book_you_search and checked_book_name != "No More Books":
#         checked_books += 1
#     if checked_book_name == "No More Books":
#         print(f"The book you search is not here!")
#         print(f"You checked {checked_books} books.")
#         break
# if checked_book_name == book_you_search:
#     print(f"You checked {checked_books} books and found it.")

# 02. Exam Preparation
# number_of_failures = int(input())
# set_failures = number_of_failures
# name_of_assignment = ""
# assignment_mark = 0
# number_of_assignments = 0
# total_of_assignments = 0
# last_assignment_name = ""
# while number_of_failures > 0:
#     name_of_assignment = input()
#     if name_of_assignment == "Enough":
#         print(f"Average score: {(total_of_assignments / number_of_assignments):.2f}")
#         print(f"Number of problems: {number_of_assignments}")
#         print(f"Last problem: {last_assignment_name}")
#         break
#     assignment_mark = int(input())
#     total_of_assignments += assignment_mark
#     last_assignment_name = name_of_assignment
#     number_of_assignments += 1
#     if assignment_mark <= 4:
#         number_of_failures -= 1
# if number_of_failures <= 0:
#     print(f"You need a break, {set_failures} poor grades.")

# 03. Vacation
# price_of_vacation = float(input())
# saved_money = float(input())
# days_counter = 0
# spend_counter = 0
# while saved_money < price_of_vacation:
#     action = input()
#     action_amount = float(input())
#     days_counter += 1
#     if action == "save":
#         saved_money += action_amount
#         spend_counter = 0
#     elif action == "spend":
#         if action_amount >= saved_money:
#             saved_money = 0
#         else:
#             saved_money -= action_amount
#         spend_counter += 1
#         if spend_counter == 5:
#             break
# if saved_money >= price_of_vacation:
#     print(f"You saved the money for {days_counter} days.")
# else:
#     print(f"You can't save the money.")
#     print(f"{days_counter}")

# 04. Walking
# total_steps = 0
# while total_steps < 10000:
#     command_line = input()
#     if command_line == "Going home":
#         total_steps += int(input())
#         break
#     else:
#         total_steps += int(command_line)
# if total_steps < 10000:
#     print(f"{10000 - total_steps} more steps to reach goal.")
# else:
#     print(f"Goal reached! Good job!")
#     print(f"{total_steps - 10000} steps over the goal!")

# 05. Coins
# from math import floor
# available_coins = floor(float(input()) * 100)
# two_counter = 0
# one_counter = 0
# fifty_counter = 0
# twenty_counter = 0
# ten_counter = 0
# five_counter = 0
# two_cent_counter = 0
# one_cent_counter = 0
# while available_coins > 0:
#     if available_coins >= 200:
#         available_coins -= 200
#         two_counter += 1
#     elif 100 <= available_coins < 200:
#         available_coins -= 100
#         one_counter += 1
#     elif 50 <= available_coins < 100:
#         available_coins -= 50
#         fifty_counter += 1
#     elif 20 <= available_coins < 50:
#         available_coins -= 20
#         twenty_counter += 1
#     elif 10 <= available_coins < 20:
#         available_coins -= 10
#         ten_counter += 1
#     elif 5 <= available_coins < 10:
#         available_coins -= 5
#         five_counter += 1
#     elif 2 <= available_coins < 5:
#         available_coins -= 2
#         two_cent_counter += 1
#     elif 1 <= available_coins < 2:
#         available_coins -= 1
#         one_cent_counter += 1
#         break
# print(f"{two_counter + one_counter + fifty_counter + twenty_counter + ten_counter + five_counter + two_cent_counter + one_cent_counter}")

# 06. Cake
size_1_of_cake = int(input())
size_2_of_cake = int(input())
size_of_cake = size_1_of_cake * size_2_of_cake
taken_pieces_int = 0
while size_of_cake > 0:
    taken_pieces = input()
    if taken_pieces == "STOP":
        break
    else:
        taken_pieces_int = int(taken_pieces)
        if taken_pieces_int > size_of_cake:
            needed_pieces = abs(size_of_cake - taken_pieces_int)
            break
        size_of_cake -= taken_pieces_int
if taken_pieces_int > size_of_cake:
    print(f"No more cake left! You need {abs(size_of_cake - taken_pieces_int)} pieces more.")
else:
    print(f"{size_of_cake} pieces are left.")

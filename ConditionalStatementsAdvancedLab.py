# 01. Day of Week
# number_of_day = int(input())
# if number_of_day == 1:
#     print('Monday')
# elif number_of_day == 2:
#     print('Tuesday')
# elif number_of_day == 3:
#     print('Wednesday')
# elif number_of_day == 4:
#     print('Thursday')
# elif number_of_day == 5:
#     print('Friday')
# elif number_of_day == 6:
#     print('Saturday')
# elif number_of_day == 7:
#     print('Sunday')
# else:
#     print('Error')

# 02.Weekend or Working Day
# day_of_the_week = input()
# working_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# weekends = ('Saturday', 'Sunday')
# if day_of_the_week in working_days:
#     print('Working day')
# elif day_of_the_week in weekends:
#     print('Weekend')
# else:
#     print('Error')

# 03. Animal Type
# animal_type = input()
# if animal_type == 'dog':
#     print('mammal')
# elif animal_type in ('crocodile', 'tortoise', 'snake'):
#     print('reptile')
# else:
#     print('unknown')

# 04. Personal Titles
# age = float(input())
# gender = input()
# if gender == 'm':
#     if age < 16:
#         print('Master')
#     else:
#         print('Mr.')
# else:
#     if age < 16:
#         print('Miss')
#     else:
#         print('Ms.')

# 05. Small Shop
# product = input()
# city = input()
# quantity = float(input())
# if city == 'Sofia':
#     if product == 'coffee':
#         print(quantity * 0.5)
#     elif product == 'water':
#         print(quantity * 0.8)
#     elif product == 'beer':
#         print(quantity * 1.2)
#     elif product == 'sweets':
#         print(quantity * 1.45)
#     else:
#         print(quantity * 1.6)
# if city == 'Plovdiv':
#     if product == 'coffee':
#         print(quantity * 0.4)
#     elif product == 'water':
#         print(quantity * 0.7)
#     elif product == 'beer':
#         print(quantity * 1.15)
#     elif product == 'sweets':
#         print(quantity * 1.3)
#     else:
#         print(quantity * 1.5)
# elif city == 'Varna':
#     if product == 'coffee':
#         print(quantity * 0.45)
#     elif product == 'water':
#         print(quantity * 0.7)
#     elif product == 'beer':
#         print(quantity * 1.1)
#     elif product == 'sweets':
#         print(quantity * 1.35)
#     else:
#         print(quantity * 1.55)

# 06. Number in Range
# entered_number = int(input())
# if -100 <= entered_number <= 100 and entered_number != 0:
#     print('Yes')
# else:
#     print('No')

# 07.Working Hours
# hour = int(input())
# day_of_week = input()
# working_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
# if 10 <= hour <= 18 and day_of_week in working_days:
#     print('open')
# else:
#     print('closed')

# 08.Cinema Ticket
# day_of_week = input()
# if day_of_week in ('Monday', 'Tuesday', 'Friday'):
#     print(12)
# elif day_of_week in ('Wednesday', 'Thursday'):
#     print(14)
# elif day_of_week in ('Saturday', 'Sunday'):
#     print(16)

# 09. Fruit or Vegetable
# name_of_product = input()
# if name_of_product in ('banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'):
#     print('fruit')
# elif name_of_product in ('tomato', 'cucumber', 'pepper', 'carrot'):
#     print('vegetable')
# else:
#     print('unknown')

# 10. Invalid Number
# given_number = int(input())
# if given_number not in range(100,201) and given_number != 0:
#     print('invalid')
# else:
#     pass

# # 11. Fruit Shop
# fruit = input()
# day_of_week = input()
# quantity = float(input())
# if fruit in ('banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes'):
#     if day_of_week in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
#         price_list = {"banana": 2.5, "apple": 1.2, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.7, "pineapple": 5.5,
#                       "grapes": 3.85}
#         total_sum = price_list[fruit] * quantity
#         print(format(total_sum, '.2f'))
#     elif day_of_week in ('Saturday', 'Sunday'):
#         price_list = {"banana": 2.7, "apple": 1.25, "orange": 0.9, "grapefruit": 1.6, "kiwi": 3, "pineapple": 5.6,
#                       "grapes": 4.2}
#         total_sum = price_list[fruit] * quantity
#         print(format(total_sum, '.2f'))
#     else:
#         print('error')
# else:
#     print('error')

# 12. Trade Commissions
# city_name = input()
# sales_volume = float(input())
# if sales_volume < 0 or city_name not in ('Sofia', 'Varna', 'Plovdiv'):
#     print('error')
# elif city_name == 'Sofia':
#     if 0 <= sales_volume <= 500:
#         print(format(sales_volume * 0.05, '.2f'))
#     elif 500 < sales_volume <= 1000:
#         print(format(sales_volume * 0.07, '.2f'))
#     elif 1000 < sales_volume <= 10000:
#         print(format(sales_volume * 0.08, '.2f'))
#     else:
#         print(format(sales_volume * 0.12, '.2f'))
# elif city_name == 'Varna':
#     if 0 <= sales_volume <= 500:
#         print(format(sales_volume * 0.045, '.2f'))
#     elif 500 < sales_volume <= 1000:
#         print(format(sales_volume * 0.075, '.2f'))
#     elif 1000 < sales_volume <= 10000:
#         print(format(sales_volume * 0.10, '.2f'))
#     else:
#         print(format(sales_volume * 0.13, '.2f'))
# else:
#     if 0 <= sales_volume <= 500:
#         print(format(sales_volume * 0.055, '.2f'))
#     elif 500 < sales_volume <= 1000:
#         print(format(sales_volume * 0.08, '.2f'))
#     elif 1000 < sales_volume <= 10000:
#         print(format(sales_volume * 0.12, '.2f'))
#     else:
#         print(format(sales_volume * 0.145, '.2f'))

# 13. Ski Trip
days_to_stay = int(input())
number_of_nights = days_to_stay - 1
type_of_accommodation = input()
evaluation = input()
# price_list = {"room for one person": 18, "apartment": 25, "president apartment": 35}
if type_of_accommodation == "room for one person":
    if evaluation == "positive":
        total_sum_to_pay = number_of_nights * 18 * 1.25
        print(format(total_sum_to_pay, '.2f'))
    else:
        total_sum_to_pay = number_of_nights * 18 * 0.9
        print(format(total_sum_to_pay, '.2f'))
elif type_of_accommodation == "apartment":
    if evaluation == "positive":
        if number_of_nights < 10:
            total_sum_to_pay = number_of_nights * 25 * 0.7 * 1.25
            print(format(total_sum_to_pay, '.2f'))
        elif 10 <= number_of_nights <= 15:
            total_sum_to_pay = number_of_nights * 25 * 0.65 * 1.25
            print(format(total_sum_to_pay, '.2f'))
        else:
            total_sum_to_pay = number_of_nights * 25 * 0.5 * 1.25
            print(format(total_sum_to_pay, '.2f'))
    else:
        if number_of_nights < 10:
            total_sum_to_pay = number_of_nights * 25 * 0.7 * 0.9
            print(format(total_sum_to_pay, '.2f'))
        elif 10 <= number_of_nights <= 15:
            total_sum_to_pay = number_of_nights * 25 * 0.65 * 0.9
            print(format(total_sum_to_pay, '.2f'))
        else:
            total_sum_to_pay = number_of_nights * 25 * 0.5 * 0.9
            print(format(total_sum_to_pay, '.2f'))
else:
    if evaluation == "positive":
        if number_of_nights < 10:
            total_sum_to_pay = number_of_nights * 35 * 0.9 * 1.25
            print(format(total_sum_to_pay, '.2f'))
        elif 10 <= number_of_nights <= 15:
            total_sum_to_pay = number_of_nights * 35 * 0.85 * 1.25
            print(format(total_sum_to_pay, '.2f'))
        else:
            total_sum_to_pay = number_of_nights * 35 * 0.8 * 1.25
            print(format(total_sum_to_pay, '.2f'))
    else:
        if number_of_nights < 10:
            total_sum_to_pay = number_of_nights * 35 * 0.9 * 0.9
            print(format(total_sum_to_pay, '.2f'))
        elif 10 <= number_of_nights <= 15:
            total_sum_to_pay = number_of_nights * 35 * 0.85 * 0.9
            print(format(total_sum_to_pay, '.2f'))
        else:
            total_sum_to_pay = number_of_nights * 35 * 0.8 * 0.9
            print(format(total_sum_to_pay, '.2f'))

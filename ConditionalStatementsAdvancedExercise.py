# 01. Cinema
# projection_type = input()
# row_numbers = int(input())
# column_numbers = int(input())
# income = 0
# if projection_type == 'Premiere':
#     income = 12 * row_numbers * column_numbers
#     print(f"{income:.2f} leva")
# elif projection_type == 'Normal':
#     income = 7.5 * row_numbers * column_numbers
#     print(f"{income:.2f} leva")
# else:
#     income = 5 * row_numbers * column_numbers
#     print(f"{income:.2f} leva")

# 02. Summer Outfit
# temperature = int(input())
# time_of_day = input()
# if 10 <= temperature <= 18:
#     if time_of_day == 'Morning':
#         print(f"It's {temperature} degrees, get your Sweatshirt and Sneakers.")
#     elif time_of_day == 'Afternoon' or time_of_day == 'Evening':
#         print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
# elif 18 < temperature <= 24:
#     if time_of_day == 'Morning' or time_of_day == 'Evening':
#         print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
#     elif time_of_day == 'Afternoon':
#         print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")
# else:
#     if time_of_day == 'Morning':
#         print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")
#     elif time_of_day == 'Afternoon':
#         print(f"It's {temperature} degrees, get your Swim Suit and Barefoot.")
#     else:
#         print(f"It's {temperature} degrees, get your Shirt and Moccasins.")

# 03. New House
# type_of_flower = input()
# number_of_flowers = int(input())
# budget = int(input())
# price_list = {'Roses': 5, 'Dahlias': 3.8, 'Tulips': 2.8, 'Narcissus': 3, 'Gladiolus': 2.5}
# price_change_list = {'Roses': 0.9, 'Dahlias': 0.85, 'Tulips': 0.85, 'Narcissus': 1.15, 'Gladiolus': 1.2}
# cost_of_flowers = price_list[type_of_flower] * number_of_flowers
# if type_of_flower == 'Roses' or type_of_flower == 'Tulips':
#     if number_of_flowers > 80:
#         cost_of_flowers = cost_of_flowers * price_change_list[type_of_flower]
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
#     else:
#         cost_of_flowers = cost_of_flowers
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
# elif type_of_flower == 'Dahlias':
#     if number_of_flowers > 90:
#         cost_of_flowers = cost_of_flowers * price_change_list[type_of_flower]
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
#     else:
#         cost_of_flowers = cost_of_flowers
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
# elif type_of_flower == 'Narcissus':
#     if number_of_flowers < 120:
#         cost_of_flowers = cost_of_flowers * price_change_list[type_of_flower]
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
#     else:
#         cost_of_flowers = cost_of_flowers
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
# elif type_of_flower == 'Gladiolus':
#     if number_of_flowers < 80:
#         cost_of_flowers = cost_of_flowers * price_change_list[type_of_flower]
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
#     else:
#         cost_of_flowers = cost_of_flowers
#         money_left = budget - cost_of_flowers
#         if money_left >= 0:
#             print(
#                 f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
#         else:
#             print(f"Not enough money, you need {abs(money_left):.2f} leva more.")

# 04. Fishing Boat
# group_budget = int(input())
# season = input()
# number_of_fisherman = int(input())
# price_of_rent = {'Spring': 3000, 'Summer': 4200, 'Autumn': 4200, 'Winter': 2600}
# cost_of_fishing = 0
# budget_cost_difference = 0
# if number_of_fisherman <= 6:
#     cost_of_fishing = price_of_rent[season] * 0.9
#     budget_cost_difference = group_budget - cost_of_fishing
# elif 7 <= number_of_fisherman <= 11:
#     cost_of_fishing = price_of_rent[season] * 0.85
#     budget_cost_difference = group_budget - cost_of_fishing
# elif number_of_fisherman >= 12:
#     cost_of_fishing = price_of_rent[season] * 0.75
#     budget_cost_difference = group_budget - cost_of_fishing
#
# if (number_of_fisherman % 2) == 0 and season != "Autumn":
#     cost_of_fishing = cost_of_fishing * 0.95
#     budget_cost_difference = group_budget - cost_of_fishing
# else:
#     pass
#
# if budget_cost_difference >= 0:
#     print(f"Yes! You have {budget_cost_difference:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {abs(budget_cost_difference):.2f} leva.")

# 05. Journey
# holiday_budget = float(input())
# season = input()
# destination = ""
# type_of_accommodation = ""
# total_cost = 0
# accommodation_list = {"summer": "Camp", "winter": "Hotel"}
# if holiday_budget <= 100:
#     type_of_accommodation = accommodation_list[season]
#     if type_of_accommodation == "Camp":
#         total_cost = holiday_budget * 0.3
#     else:
#         total_cost = holiday_budget * 0.7
#     destination = "Bulgaria"
# elif holiday_budget <= 1000:
#     type_of_accommodation = accommodation_list[season]
#     if type_of_accommodation == "Camp":
#         total_cost = holiday_budget * 0.4
#     else:
#         total_cost = holiday_budget * 0.8
#     destination = "Balkans"
# else:
#     total_cost = holiday_budget * 0.9
#     type_of_accommodation = "Hotel"
#     destination = "Europe"
#
# print(f"Somewhere in {destination}")
# print(f"{type_of_accommodation} - {total_cost:.2f}")

# 06. Operations Between Numbers
# first_number = int(input())
# second_number = int(input())
# math_operator = input()
# type_of_number = ""
# math_operation = f"{first_number} {math_operator} {second_number}"
# if second_number == 0 and math_operator in ("/", "%"):
#     print(f"Cannot divide {first_number} by zero")
# elif math_operator in ("+", "-", "*"):
#     if eval(math_operation) % 2 == 0:
#         type_of_number = "even"
#     else:
#         type_of_number = "odd"
#     print(f"{first_number} {math_operator} {second_number} = {eval(math_operation)} - {type_of_number}")
# elif math_operator == "%":
#     print(f"{first_number} {math_operator} {second_number} = {eval(math_operation)}")
# else:
#     print(f"{first_number} {math_operator} {second_number} = {eval(math_operation):.2f}")

# 07. Hotel Room
# month_of_holiday = input()
# number_of_nights = int(input())
# apartment_price = 0
# studio_price = 0
# if month_of_holiday == "May" or month_of_holiday == "October":
#     if 7 < number_of_nights <= 14:
#         apartment_price = number_of_nights * 65
#         studio_price = number_of_nights * 50 * 0.95
#     elif number_of_nights > 14:
#         apartment_price = number_of_nights * 65 * 0.9
#         studio_price = number_of_nights * 50 * 0.7
#     else:
#         apartment_price = number_of_nights * 65
#         studio_price = number_of_nights * 50
# elif month_of_holiday == "June" or month_of_holiday == "September":
#     if number_of_nights > 14:
#         apartment_price = number_of_nights * 68.7 * 0.9
#         studio_price = number_of_nights * 75.2 * 0.8
#     else:
#         apartment_price = number_of_nights * 68.7
#         studio_price = number_of_nights * 75.2
# elif month_of_holiday == "July" or month_of_holiday == "August":
#     if number_of_nights > 14:
#         apartment_price = number_of_nights * 77 * 0.9
#         studio_price = number_of_nights * 76
#     else:
#         apartment_price = number_of_nights * 77
#         studio_price = number_of_nights * 76
# print(f"Apartment: {apartment_price:.2f} lv.")
# print(f"Studio: {studio_price:.2f} lv.")

# 08. On Time for the Exam
# exam_hours = int(input())
# exam_minutes = int(input())
# arrival_hours = int(input())
# arrival_minutes = int(input())
# total_exam_min = exam_hours * 60 + exam_minutes
# total_arrival_min = arrival_hours * 60 + arrival_minutes
# hours_left = 0
# min_left = 0
# diff = abs(total_exam_min - total_arrival_min)
# if total_arrival_min == total_exam_min:
#     print("On time")
# elif total_arrival_min > total_exam_min:
#     print("Late")
#     if diff >= 60:
#         hours_left = diff // 60
#         min_left = diff % 60
#         print(f"{hours_left}:{min_left:02d} hours after the start")
#     else:
#         print(f"{diff} minutes after the start")
# elif total_arrival_min < total_exam_min:
#     if diff <= 30:
#         print("On time")
#         print(f"{diff} minutes before the start")
#     else:
#         if diff >= 60:
#             hours_left = diff // 60
#             min_left = diff % 60
#             print("Early")
#             print(f"{hours_left}:{min_left:02d} hours before the start")
#         else:
#             print("Early")
#             print(f"{diff} minutes before the start")

# 09. Volleyball
from math import floor

year_type = input()
bank_holidays = int(input())
travel_weekends = int(input())
sofia_weekends = 48 - travel_weekends
sofia_plays = sofia_weekends * 3 / 4
bank_holiday_plays = bank_holidays * 2 / 3
if year_type == "normal":
    total_plays = floor(sofia_plays + travel_weekends + bank_holiday_plays)
    print(total_plays)
else:
    total_plays = floor((sofia_plays + travel_weekends + bank_holiday_plays) * 1.15)
    print(total_plays)

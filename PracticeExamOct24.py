# 01. Moon
# from math import ceil
# moon_to_earth = 384400 * 2
# average_speed = float(input())
# needed_fuel = float(input())
# travel_time = ceil(moon_to_earth / average_speed) + 3
# fuel_consumption = (moon_to_earth * needed_fuel) / 100
# print(travel_time)
# print(f"{fuel_consumption:.0f}")

# 02. Spaceship
# from math import floor
# width_of_ship = float(input())
# length_of_ship = float(input())
# height_of_ship = float(input())
# average_height_crew = float(input())
# volume_ship = width_of_ship * length_of_ship * height_of_ship
# volume_room = (average_height_crew + 0.4) * 2 * 2
# number_of_crew = volume_ship / volume_room
# if 3 <= number_of_crew <= 10:
#     print(f"The spacecraft holds {floor(number_of_crew)} astronauts.")
# elif number_of_crew < 3:
#     print(f"The spacecraft is too small.")
# elif number_of_crew > 10:
#     print(f"The spacecraft is too big.")

# 03. Football Souvenirs
# name_of_country = input()
# name_of_souvenir = input()
# number_of_souvenirs = int(input())
# total_price = 0
# stock_and_country = True
# if name_of_country == "Argentina":
#     if name_of_souvenir == "flags":
#         total_price = 3.25 * number_of_souvenirs
#     elif name_of_souvenir == "caps":
#         total_price = 7.2 * number_of_souvenirs
#     elif name_of_souvenir == "posters":
#         total_price = 5.1 * number_of_souvenirs
#     elif name_of_souvenir == "stickers":
#         total_price = 1.25 * number_of_souvenirs
#     else:
#         print("Invalid stock!")
#         stock_and_country = False
#     if stock_and_country:
#         print(f"Pepi bought {number_of_souvenirs} {name_of_souvenir} of {name_of_country} for {total_price:.2f} lv.")
# elif name_of_country == "Brazil":
#     if name_of_souvenir == "flags":
#         total_price = 4.2 * number_of_souvenirs
#     elif name_of_souvenir == "caps":
#         total_price = 8.5 * number_of_souvenirs
#     elif name_of_souvenir == "posters":
#         total_price = 5.35 * number_of_souvenirs
#     elif name_of_souvenir == "stickers":
#         total_price = 1.2 * number_of_souvenirs
#     else:
#         print("Invalid stock!")
#         stock_and_country = False
#     if stock_and_country:
#         print(f"Pepi bought {number_of_souvenirs} {name_of_souvenir} of {name_of_country} for {total_price:.2f} lv.")
# elif name_of_country == "Croatia":
#     if name_of_souvenir == "flags":
#         total_price = 2.75 * number_of_souvenirs
#     elif name_of_souvenir == "caps":
#         total_price = 6.9 * number_of_souvenirs
#     elif name_of_souvenir == "posters":
#         total_price = 4.95 * number_of_souvenirs
#     elif name_of_souvenir == "stickers":
#         total_price = 1.1 * number_of_souvenirs
#     else:
#         print("Invalid stock!")
#         stock_and_country = False
#     if stock_and_country:
#         print(f"Pepi bought {number_of_souvenirs} {name_of_souvenir} of {name_of_country} for {total_price:.2f} lv.")
# elif name_of_country == "Denmark":
#     if name_of_souvenir == "flags":
#         total_price = 3.1 * number_of_souvenirs
#
#     elif name_of_souvenir == "caps":
#         total_price = 6.5 * number_of_souvenirs
#     elif name_of_souvenir == "posters":
#         total_price = 4.8 * number_of_souvenirs
#     elif name_of_souvenir == "stickers":
#         total_price = 0.9 * number_of_souvenirs
#     else:
#         print("Invalid stock!")
#         stock_and_country = False
#     if stock_and_country:
#         print(f"Pepi bought {number_of_souvenirs} {name_of_souvenir} of {name_of_country} for {total_price:.2f} lv.")
# else:
#     print("Invalid country!")

# 04. Cat Food
# number_of_cats = int(input())
# needed_food = 0
# group_one = 0
# group_two = 0
# group_three = 0
# total_food = 0
# for i in range(1, number_of_cats + 1):
#     needed_food = float(input())
#     total_food += needed_food
#     if 100 <= needed_food < 200:
#         group_one += 1
#     if 200 <= needed_food < 300:
#         group_two += 1
#     if 300 <= needed_food < 400:
#         group_three += 1
# print(f"Group 1: {group_one} cats.")
# print(f"Group 2: {group_two} cats.")
# print(f"Group 3: {group_three} cats.")
# print(f"Price for food per day: {(total_food / 1000) * 12.45:.2f} lv.")

# 05. Puppy Care
# bought_food_in_kg = int(input()) * 1000
# consumed_food = input()
# while consumed_food != "Adopted":
#     bought_food_in_kg -= int(consumed_food)
#     consumed_food = input()
# if bought_food_in_kg < 0:
#     print(f"Food is not enough. You need {abs(bought_food_in_kg)} grams more.")
# else:
#     print(f"Food is enough! Leftovers: {bought_food_in_kg} grams.")

# 06. Gold Mine
number_of_locations = int(input())
total_daily_finding = 0
avg_daily_finding = 0
for i in range(1, number_of_locations + 1):
    average_daily_findings_expected = float(input())
    number_of_digging_days = int(input())
    for j in range(1, number_of_digging_days + 1):
        daily_findings = float(input())
        total_daily_finding += daily_findings
        avg_daily_finding = total_daily_finding / number_of_digging_days
    if avg_daily_finding >= average_daily_findings_expected:
        print(f"Good job! Average gold per day: {avg_daily_finding:.2f}.")
    else:
        print(f"You need {average_daily_findings_expected - avg_daily_finding:.2f} gold.")
    avg_daily_finding = 0
    total_daily_finding = 0

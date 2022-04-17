# 01. Repainting
# needed_cover = int(input()) + 2
# needed_paint = int(input()) * 1.1
# paint_thinner = int(input())
# man_hours = int(input())
# material_expenses = (needed_cover * 1.5) + (needed_paint * 14.5) + (paint_thinner * 5) + 0.4
# worker_expenses = material_expenses * 0.3 * man_hours
# total_expenses = material_expenses + worker_expenses
# print(f"Total expenses: {total_expenses:.2f} lv.")

# 02. Shopping
# total_budget = float(input())
# video_card_number = int(input())
# processor_number = int(input())
# ram_number = int(input())
# video_card_price = 250
# price_of_video_card = video_card_number * video_card_price
# price_of_processor = (price_of_video_card * 0.35) * processor_number
# price_of_ram = (price_of_video_card * 0.1) * ram_number
# total_price = price_of_video_card + price_of_processor + price_of_ram
# if video_card_number > processor_number:
#     total_price = total_price * 0.85
# if total_budget >= total_price:
#     print(f"You have {total_budget - total_price:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {abs(total_budget - total_price):.2f} leva more!")

# 03. Travel Agency
# name_of_city = input()
# type_of_packet = input()
# vip_logical = input()
# number_of_days = int(input())
# price_per_day = 0
# total_price = 0
# vip_discount = 0
# if number_of_days > 7:
#     number_of_days = number_of_days - 1
# if name_of_city == "Bansko" or name_of_city == "Borovets":
#     if type_of_packet == "withEquipment":
#         price_per_day = 100
#         vip_discount = 0.9
#     else:
#         price_per_day = 80
#         vip_discount = 0.95
#     if vip_logical == "yes":
#         total_price = number_of_days * price_per_day * vip_discount
#     else:
#         total_price = number_of_days * price_per_day
# if name_of_city == "Varna" or name_of_city == "Burgas":
#     if type_of_packet == "withBreakfast":
#         price_per_day = 130
#         vip_discount = 0.88
#     else:
#         price_per_day = 100
#         vip_discount = 0.93
#     if vip_logical == "yes":
#         total_price = number_of_days * price_per_day * vip_discount
#     else:
#         total_price = number_of_days * price_per_day
# if number_of_days < 1:
#     print(f"Days must be positive number!")
# elif name_of_city not in ("Bansko", "Borovets", "Varna", "Burgas") or type_of_packet not in ("withEquipment", "noEquipment" , "noBreakfast", "withBreakfast"):
#     print(f"Invalid input!")
# else:
#     print(f"The price is {total_price:.2f}lv! Have a nice time!")

# 04. Fitness Center
# number_of_visitors = int(input())
# back_training = 0
# chest_training = 0
# legs_training = 0
# abs_training = 0
# protein_shake = 0
# protein_bar = 0
# workout_number = 0
# protein_number = 0
# for i in range(1, number_of_visitors + 1):
#     type_of_training = input()
#     if type_of_training == "Back":
#         back_training += 1
#         workout_number += 1
#     elif type_of_training == "Chest":
#         chest_training += 1
#         workout_number += 1
#     elif type_of_training == "Legs":
#         legs_training += 1
#         workout_number += 1
#     elif type_of_training == "Abs":
#         abs_training += 1
#         workout_number += 1
#     elif type_of_training == "Protein shake":
#         protein_shake += 1
#         protein_number += 1
#     elif type_of_training == "Protein bar":
#         protein_bar += 1
#         protein_number += 1
# print(f"{back_training} - back")
# print(f"{chest_training} - chest")
# print(f"{legs_training} - legs")
# print(f"{abs_training} - abs")
# print(f"{protein_shake} - protein shake")
# print(f"{protein_bar} - protein bar")
# print(f"{(workout_number/number_of_visitors) * 100:.2f}% - work out")
# print(f"{(protein_number/number_of_visitors) * 100:.2f}% - protein")

# 05. Club
# needed_profit = float(input())
# name_of_cocktail = input()
# cocktail_price = 0
# club_income = 0
# price_of_order = 0
# while name_of_cocktail != "Party!":
#     number_of_orders = int(input())
#     cocktail_price = len(name_of_cocktail)
#     price_of_order = cocktail_price * number_of_orders
#     if price_of_order % 2 == 0:
#         club_income += cocktail_price * number_of_orders
#     else:
#         club_income += cocktail_price * number_of_orders * 0.75
#     if club_income >= needed_profit:
#         break
#     name_of_cocktail = input()
# if needed_profit > club_income:
#     print(f"We need {needed_profit - club_income:.2f} leva more.")
#     print(f"Club income - {club_income:.2f} leva.")
# else:
#     print(f"Target acquired.")
#     print(f"Club income - {club_income:.2f} leva.")

# 06. Easter Competition
number_of_bakers = int(input())
bakery_total = 0
cake_evaluation = ""
total_chef_point = {}
champion_points = 0
champion = ""
for i in range(1, number_of_bakers + 1):
    name_of_bakery = input()
    cake_evaluation = input()
    while cake_evaluation != "Stop":
        if 1 <= int(cake_evaluation) <= 10:
            bakery_total += int(cake_evaluation)
            cake_evaluation = input()
        else:
            cake_evaluation = input()
    print(f"{name_of_bakery} has {bakery_total} points.")
    if i == 1:
        print(f"{name_of_bakery} is the new number 1!")
    total_chef_point[name_of_bakery] = bakery_total
    champion = max(total_chef_point, key=total_chef_point.get)
    champion_points = max(total_chef_point.values())
    if bakery_total >= champion_points and i != 1:
        print(f"{name_of_bakery} is the new number 1!")
    bakery_total = 0
print(f"{champion} won competition with {champion_points} points!")

number_of_bakers = int(input())
bakery_total = 0
cake_evaluation = ""
total_chef_point = {}
champion_points = 0
champion = ""
name_of_chef = ""
points_of_chef = 0
for i in range(1, number_of_bakers + 1):
    name_of_bakery = input()
    cake_evaluation = input()
    while cake_evaluation != "Stop":
        if 1 <= int(cake_evaluation) <= 10:
            bakery_total += int(cake_evaluation)
            cake_evaluation = input()
        else:
            cake_evaluation = input()
    print(f"{name_of_bakery} has {bakery_total} points.")
    if i == 1:
        print(f"{name_of_bakery} is the new number 1!")
        name_of_chef = name_of_bakery
        points_of_chef = bakery_total
    if bakery_total > points_of_chef and i != 1:
        print(f"{name_of_bakery} is the new number 1!")
        name_of_chef = name_of_bakery
        points_of_chef = bakery_total
    bakery_total = 0
print(f"{name_of_chef} won competition with {points_of_chef} points!")

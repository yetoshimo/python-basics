# 01. Trapeziod Area
# b1 = float(input())
# b2 = float(input())
# h = float(input())
# print(format(((b1 + b2) * h / 2),'.2f'))

# 02. Triangle Area
# side = float(input())
# height = float(input())
# print(format((side * height / 2),'.2f'))

# 03. Celsius to Fahrenheit
# celsius = float(input())
# print(format((celsius * 1.8 + 32),'.2f'))

# 04. Vegetable Market
# veggie_price = float(input())
# fruit_price = float(input())
# veggie_price_eur = veggie_price / 1.94
# fruit_price_eur = fruit_price / 1.94
# veggie_weight = int(input())
# fruit_weight = int(input())
# print(format(veggie_price_eur * veggie_weight + fruit_price_eur * fruit_weight,'.2f'))

# 05. Training Lab
# width = float(input())
# height = float(input())
# if 3 <= height <= width <= 100:
# table_per_column = (height - 1) // 0.7
# table_per_row = width // 1.2
# total_tables = table_per_row * table_per_column - 3
# total_tables = ((height - 1) // 0.7) * (width // 1.2) - 3
# print(format(total_tables, '.0f'))
# else:
#     print('Invalid input!')

# 06. Fishland
# mackerel_price = float(input()) #skumriqta
# sprat_price = float(input()) #tsatsa
# bonito_weight = float(input()) #palamud
# horse_mackerel_weight = float(input()) #safrid
# mussels_weight = int(input()) #midi
# price_to_pay = bonito_weight * 1.6 * mackerel_price + horse_mackerel_weight * 1.8 * sprat_price + mussels_weight * 7.5
# print(format(round(price_to_pay,2),'.2f'))

# 07. House Painting
# x_height = float(input())
# y_length = float(input())
# h_height = float(input())
# green_paint = ((x_height * y_length * 2 - 4.5) + (x_height * x_height * 2 - 2.4)) / 3.4
# red_paint = ((x_height * y_length * 2) + ((x_height * h_height / 2) * 2)) / 4.3
# print(format(green_paint,'.2f'))
# print(format(red_paint,'.2f'))

# 08. Circle Area and Perimeter
# import math
# radius = float(input())
# area = radius * radius * math.pi
# circumference = radius * 2 * math.pi
# print(format(area,'.2f'))
# print(format(circumference,'.2f'))

# 09. Weather Forecast
# weather = input()
# if weather == 'sunny':
#     print("It's warm outside!")
# else:
#     print("It's cold outside!")

# 10. Weather Forecast - Part 2
temperature = float(input())
if 26 <= temperature <= 35:
    print('Hot')
elif 20.1 <= temperature <= 25.9:
    print('Warm')
elif 15 <= temperature <= 20:
    print('Mild')
elif 12 <= temperature <= 14.9:
    print('Cool')
elif 5 <= temperature <= 11.9:
    print('Cold')
else:
    print('unknown')

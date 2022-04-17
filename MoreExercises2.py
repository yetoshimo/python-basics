# 01. Pipes In Pool
# pool_volume = int(input())
# first_pipe_flow = int(input())
# second_pipe_flow = int(input())
# time = float(input())
# pool_fill = (first_pipe_flow + second_pipe_flow) * time
# if pool_fill <= pool_volume:
#     print(f"The pool is {format(pool_fill/pool_volume*100, '.2f')}% full. Pipe 1: {format(first_pipe_flow * time/pool_fill*100, '.2f')}%. Pipe 2: {format(second_pipe_flow * time/pool_fill*100, '.2f')}%.")
# else:
#     print(f"For {time} hours the pool overflows with {format(pool_fill-pool_volume, '.2f')} liters.")

# 02. Sleepy Tom Cat
# vacation_days = int(input())
# play_hours = (vacation_days * 127) + ((365 - vacation_days) * 63)
# difference = abs(30000-play_hours)
# difference_h = difference // 60
# difference_m = difference - difference_h * 60
# if play_hours <= 30000:
#     print('Tom sleeps well')
#     print(f'{difference_h} hours and {difference_m} minutes less for play')
# else:
#     print('Tom will run away')
#     print(f'{difference_h} hours and {difference_m} minutes more for play')

# 03. Harvest
# import math
# area_vineyard = int(input())
# grape_per_m2 = float(input())
# needed_wine_liters = int(input())
# workers = int(input())
# wine_produced = (area_vineyard * grape_per_m2 * 0.4) / 2.5
# if 10 <= area_vineyard <= 5000 and 0 <= grape_per_m2 <= 10 and 10 <= needed_wine_liters <= 600 and 1 <= workers <= 20:
#     if needed_wine_liters <= wine_produced:
#         left_wine = wine_produced - needed_wine_liters
#         per_worker_wine = left_wine / workers
#         print(f"Good harvest this year! Total wine: {format(math.floor(wine_produced), '.0f')} liters.")
#         print(f"{format(math.ceil(left_wine), '.0f')} liters left -> {format(math.ceil(per_worker_wine), '.0f')} liters per person.")
#     else:
#         more_wine_needed = abs(wine_produced - needed_wine_liters)
#         print(f"It will be a tough winter! More {format(math.floor(more_wine_needed), '.0f')} liters wine needed.")
# else:
#     print("Invalid input!")

# 04. Transport Price
# kilometers = int(input())
# time_of_day = input()
# if kilometers < 20 and time_of_day == 'day':
#     fee_day_taxi = 0.7 + kilometers * 0.79
#     print(format(fee_day_taxi, '.2f'))
# elif kilometers < 20 and time_of_day == 'night':
#     fee_night_taxi = 0.7 + kilometers * 0.9
#     print(format(fee_night_taxi, '.2f'))
# elif 20 <= kilometers < 100:
#     fee_bus = 0.09 * kilometers
#     print(format(fee_bus, '.2f'))
# else:
#     fee_train = 0.06 * kilometers
#     print(format(fee_train, '.2f'))

# 05. Firm
# import math
# needed_hours = int(input())
# days = int(input())
# overtime_workers = int(input())
# project_hours = (days * 0.9 * 8) + (overtime_workers * 2 * days)
# leftover_time = math.floor(project_hours - needed_hours)
# if 0 <= leftover_time:
#     print(f'Yes!{leftover_time} hours left.')
# else:
#     print(f'Not enough time!{abs(leftover_time)} hours needed.')

# 06. Pets
# import math
# days = int(input())
# available_food_kg = int(input())
# dog_needed_kg = float(input())
# cat_needed_kg = float(input())
# turtle_needed_gr = float(input()) / 1000
# needed_food = days * (dog_needed_kg + cat_needed_kg + turtle_needed_gr)
# leftover_food = available_food_kg - needed_food
# if 0 <= leftover_food:
#     print(f'{math.floor(leftover_food)} kilos of food left.')
# else:
#     print(f'{math.ceil(abs(leftover_food))} more kilos of food are needed.')

# 07. Flower Shop
# import math
# magnolia = int(input()) * 3.25 #magnoliq
# hyacinth = int(input()) * 4 #zyumbyul
# roses = int(input()) * 3.5 #roze
# cactus = int(input()) * 8 #kaktus
# profit = (magnolia + hyacinth + roses + cactus) * 0.95
# gift_price = float(input())
# left_money = profit - gift_price
# if 0 <= left_money:
#     print(f'She is left with {math.floor(left_money)} leva.')
# else:
#     print(f'She will have to borrow {math.ceil(abs(left_money))} leva.')

# 08. Fuel Tank
# fuel_type = input().lower()
# types_of_fuel = ['diesel', 'gasoline', 'gas']
# leftover_fuel = float(input())
# if fuel_type not in types_of_fuel:
#     print('Invalid fuel!')
# elif leftover_fuel < 25:
#     print(f'Fill your tank with {fuel_type}!')
# elif 25 <= leftover_fuel:
#     print(f'You have enough {fuel_type}.')

# 08. Fuel Tank - Part 2
fuel_type = input()
liters_of_fuel = float(input())
club_card = input()
if club_card == 'Yes':
    gasoline_price = 2.04
    diesel_price = 2.21
    gas_price = 0.85
    if liters_of_fuel < 20:
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price
            print(format(total_price, '.2f') + ' lv.')
    elif 20 <= liters_of_fuel <= 25:
        after_discount = 0.92
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
    elif 25 < liters_of_fuel:
        after_discount = 0.9
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
else:
    gasoline_price = 2.22
    diesel_price = 2.33
    gas_price = 0.93
    if liters_of_fuel < 20:
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price
            print(format(total_price, '.2f') + ' lv.')
    if 20 <= liters_of_fuel <= 25:
        after_discount = 0.92
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
    elif 25 < liters_of_fuel:
        after_discount = 0.9
        if fuel_type == 'Gas':
            total_price = liters_of_fuel * gas_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        elif fuel_type == 'Gasoline':
            total_price = liters_of_fuel * gasoline_price * after_discount
            print(format(total_price, '.2f') + ' lv.')
        else:
            total_price = liters_of_fuel * diesel_price * after_discount
            print(format(total_price, '.2f') + 'lv.')

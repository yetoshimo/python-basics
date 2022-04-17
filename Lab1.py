# 01. USD to BGN
# usd = float(input())
# bgn = usd * 1.79549
# print(bgn)

# 02. Radians to Degrees
# import math
# radiant = float(input())
# degree = radiant * 180 / math.pi
# print(math.floor(degree))

# 03. Deposit Calculator
# deposit_sum = float(input())
# invest_months = int(input())
# yearly_interest_rate = float(input()) / 100
# returns = deposit_sum + invest_months * ((deposit_sum * yearly_interest_rate) / 12)
# print(format(returns, '.2f'))

# 04. Vacation books list
# total_pages = int(input())
# pages_read_h = int(input())
# total_days = int(input())
# daily_to_be_read = (total_pages / pages_read_h) / total_days
# print(daily_to_be_read)

# 05. Birthday party
# rent = int(input())
# budget = (rent * 1.31) + ((1 / 3) * rent)
# print(budget)

# 06. Charity Campaign
# number_of_days = int(input())
# number_of_bakeries = int(input())
# number_of_cakes = int(input()) * 45 * number_of_bakeries
# number_of_waffles = int(input()) * 5.8 * number_of_bakeries
# number_of_pancakes = int(input()) * 3.2 * number_of_bakeries
# total_money = (number_of_cakes + number_of_waffles + number_of_pancakes) * number_of_days
# left_money = total_money * 0.875
# print(left_money)

# 07. Fruit Market
# price_strawberry = float(input())
# banana_kg = float(input())
# orange_kg = float(input())
# raspberry_kg = float(input())
# strawberry_price = float(input()) * price_strawberry
# raspberry_price = price_strawberry * 0.5 * raspberry_kg
# orange_price = price_strawberry * 0.3 * orange_kg
# banana_price = price_strawberry * 0.1 * banana_kg
# total_price = strawberry_price + raspberry_price + orange_price + banana_price
# print(total_price)

# 08. Fish Tank
length = int(input()) / 10
width = int(input()) / 10
height = int(input()) / 10
occupied_volume = 1 - (float(input()) / 100)
needed_water = length * width * height * occupied_volume
print(needed_water)

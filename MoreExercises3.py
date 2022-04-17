# # 01. Match Tickets
# budget = float(input())
# category = input()
# number_of_fans = int(input())
# vip_ticket = 499.99
# normal_ticket = 249.99
# if 1 <= number_of_fans <= 4:
#     budget_left = budget * 0.25
#     if category == 'VIP':
#         ticket_cost = number_of_fans * vip_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
#     else:
#         ticket_cost = number_of_fans * normal_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
# elif 5 <= number_of_fans <= 9:
#     budget_left = budget * 0.4
#     if category == 'VIP':
#         ticket_cost = number_of_fans * vip_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
#     else:
#         ticket_cost = number_of_fans * normal_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
# elif 10 <= number_of_fans <= 24:
#     budget_left = budget * 0.5
#     if category == 'VIP':
#         ticket_cost = number_of_fans * vip_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
#     else:
#         ticket_cost = number_of_fans * normal_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
# elif 25 <= number_of_fans <= 49:
#     budget_left = budget * 0.6
#     if category == 'VIP':
#         ticket_cost = number_of_fans * vip_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
#     else:
#         ticket_cost = number_of_fans * normal_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
# elif 50 <= number_of_fans:
#     budget_left = budget * 0.75
#     if category == 'VIP':
#         ticket_cost = number_of_fans * vip_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")
#     else:
#         ticket_cost = number_of_fans * normal_ticket
#         total_left = budget_left - ticket_cost
#         if ticket_cost <= budget_left:
#             total_left = budget_left - ticket_cost
#             print(f"Yes! You have {format(total_left, '.2f')} leva left.")
#         else:
#             print(f"Not enough money! You need {format(abs(total_left), '.2f')} leva.")

# 02. Bike Race
# number_of_juniors = int(input())
# number_of_seniors = int(input())
# race_type = input()
# if race_type == 'trail':
#     donation_sum = (number_of_juniors * 5.5 + number_of_seniors * 7) * 0.95
#     print(format(round(donation_sum, 2), '.2f'))
# elif race_type == 'cross-country' and 50 <= (number_of_juniors + number_of_seniors):
#     donation_sum = (number_of_juniors * 6 + number_of_seniors * 7.125) * 0.95
#     print(format(round(donation_sum, 2), '.2f'))
# elif race_type == 'cross-country':
#     donation_sum = (number_of_juniors * 8 + number_of_seniors * 9.5) * 0.95
#     print(format(round(donation_sum, 2), '.2f'))
# elif race_type == 'downhill':
#     donation_sum = (number_of_juniors * 12.25 + number_of_seniors * 13.75) * 0.95
#     print(format(round(donation_sum, 2), '.2f'))
# elif race_type == 'road':
#     donation_sum = (number_of_juniors * 20 + number_of_seniors * 21.5) * 0.95
#     print(format(round(donation_sum, 2), '.2f'))

# 03. Flowers
# chrysanthemum = int(input()) #hrizantema
# rose = int(input()) #roza
# tulip = int(input()) #lale
# season = input()
# holiday = input()
# high_season = ['Spring', 'Summer']
# total_number = chrysanthemum + rose + tulip
# if season in high_season:
#     if holiday == 'Y':
#         chrysanthemum_price = 2 * 1.15
#         rose_price = 4.1 * 1.15
#         tulip_price = 2.5 * 1.15
#         if 7 < tulip and 20 < total_number:
#             total_price = (((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.95) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         elif 7 < tulip:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.95) + 2
#             print(format(total_price, '.2f'))
#         elif 20 < total_number:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         else:
#             total_price = (chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) + 2
#             print(format(total_price, '.2f'))
#     elif holiday == 'N':
#         chrysanthemum_price = 2
#         rose_price = 4.1
#         tulip_price = 2.5
#         if 7 < tulip and 20 < total_number:
#             total_price = (((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.95) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         elif 7 < tulip:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.95) + 2
#             print(format(total_price, '.2f'))
#         elif 20 < total_number:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         else:
#             total_price = (chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) + 2
#             print(format(total_price, '.2f'))
# else:
#     if holiday == 'Y':
#         chrysanthemum_price = 3.75 * 1.15
#         rose_price = 4.5 * 1.15
#         tulip_price = 4.15 * 1.15
#         if season == 'Winter' and 10 <= rose and 20 < total_number:
#             total_price = (((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.9) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         elif season == 'Winter' and 10 <= rose:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.9) + 2
#             print(format(total_price, '.2f'))
#         elif 20 < total_number:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         else:
#             total_price = (chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) + 2
#             print(format(total_price, '.2f'))
#     elif holiday == 'N':
#         chrysanthemum_price = 3.75
#         rose_price = 4.5
#         tulip_price = 4.15
#         if season == 'Winter' and 10 <= rose and 20 < total_number:
#             total_price = (((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.9) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         elif season == 'Winter' and 10 <= rose:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.9) + 2
#             print(format(total_price, '.2f'))
#         elif 20 < total_number:
#             total_price = ((chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) * 0.8) + 2
#             print(format(total_price, '.2f'))
#         else:
#             total_price = (chrysanthemum * chrysanthemum_price + rose * rose_price + tulip * tulip_price) + 2
#             print(format(total_price, '.2f'))

# 04. Car To Go
# budget = float(input())
# season = input()
# if budget <= 100:
#     car_class = 'Economy class'
#     if season == 'Summer':
#         car_cost = budget * 0.35
#         car_type = 'Cabrio'
#         print(car_class)
#         print(f"{car_type} - {format(car_cost, '.2f')}")
#     else:
#         car_cost = budget * 0.65
#         car_type = 'Jeep'
#         print(car_class)
#         print(f"{car_type} - {format(car_cost, '.2f')}")
# elif 100 < budget <= 500:
#     car_class = 'Compact class'
#     if season == 'Summer':
#         car_cost = budget * 0.45
#         car_type = 'Cabrio'
#         print(car_class)
#         print(f"{car_type} - {format(car_cost, '.2f')}")
#     else:
#         car_cost = budget * 0.8
#         car_type = 'Jeep'
#         print(car_class)
#         print(f"{car_type} - {format(car_cost, '.2f')}")
# elif 500 < budget:
#     car_class = 'Luxury class'
#     car_type = 'Jeep'
#     car_cost = budget * 0.9
#     print(car_class)
#     print(f"{car_type} - {format(car_cost, '.2f')}")

# 05. Vacation
# budget = float(input())
# season = input()
# if budget <= 1000:
#     accommodation = 'Camp'
#     if season == 'Summer':
#         location = 'Alaska'
#         cost = format(budget * 0.65, '.2f')
#         print(f"{location} - {accommodation} - {cost}")
#     else:
#         location = 'Morocco'
#         cost = format(budget * 0.45, '.2f')
#         print(f"{location} - {accommodation} - {cost}")
# elif 1000 < budget <= 3000:
#     accommodation = 'Hut'
#     if season == 'Summer':
#         location = 'Alaska'
#         cost = format(budget * 0.8, '.2f')
#         print(f"{location} - {accommodation} - {cost}")
#     else:
#         location = 'Morocco'
#         cost = format(budget * 0.6, '.2f')
#         print(f"{location} - {accommodation} - {cost}")
# elif 3000 < budget:
#     accommodation = 'Hotel'
#     cost = format(budget * 0.9, '.2f')
#     if season == 'Summer':
#         location = 'Alaska'
#         print(f"{location} - {accommodation} - {cost}")
#     else:
#         location = 'Morocco'
#         print(f"{location} - {accommodation} - {cost}")

# 06. Truck Driver
# season = input()
# monthly_kms = float(input())
# low_season = ['Spring', 'Autumn']
# if monthly_kms <= 5000:
#     if season in low_season:
#         wage = format(monthly_kms * 0.75 * 4 * 0.9, '.2f')
#         print(wage)
#     elif season == 'Summer':
#         wage = format(monthly_kms * 0.9 * 4 * 0.9, '.2f')
#         print(wage)
#     else:
#         wage = format(monthly_kms * 1.05 * 4 * 0.9, '.2f')
#         print(wage)
# elif 5000 < monthly_kms <= 10000:
#     if season in low_season:
#         wage = format(monthly_kms * 0.95 * 4 * 0.9, '.2f')
#         print(wage)
#     elif season == 'Summer':
#         wage = format(monthly_kms * 1.1 * 4 * 0.9, '.2f')
#         print(wage)
#     else:
#         wage = format(monthly_kms * 1.25 * 4 * 0.9, '.2f')
#         print(wage)
# elif 10000 < monthly_kms <= 20000:
#     wage = format(monthly_kms * 1.45 * 4 * 0.9, '.2f')
#     print(wage)

# 07. School Camp
# season = input()
# group_gender = input()
# number_of_students = int(input())
# number_of_nights = int(input())
# if season == 'Winter':
#     if group_gender == 'girls':
#         type_of_sport = 'Gymnastics'
#         price_per_night = 9.6
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     elif group_gender == 'boys':
#         type_of_sport = 'Judo'
#         price_per_night = 9.6
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     else:
#         type_of_sport = 'Ski'
#         price_per_night = 10
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
# elif season == 'Spring':
#     if group_gender == 'girls':
#         type_of_sport = 'Athletics'
#         price_per_night = 7.2
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     elif group_gender == 'boys':
#         type_of_sport = 'Tennis'
#         price_per_night = 7.2
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     else:
#         type_of_sport = 'Cycling'
#         price_per_night = 9.5
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
# elif season == 'Summer':
#     if group_gender == 'girls':
#         type_of_sport = 'Volleyball'
#         price_per_night = 15
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     elif group_gender == 'boys':
#         type_of_sport = 'Football'
#         price_per_night = 15
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#     else:
#         type_of_sport = 'Swimming'
#         price_per_night = 20
#         if 50 <= number_of_students:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.5, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 20 <= number_of_students < 50:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.85, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         elif 10 <= number_of_students < 20:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night * 0.95, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")
#         else:
#             cost_of_stay = format(number_of_students * number_of_nights * price_per_night, '.2f')
#             print(f"{type_of_sport} {cost_of_stay} lv.")

# 08. Point on Rectangle Border
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x = float(input())
# y = float(input())
# if x == x1 or x == x2:
#     if y1 <= y <= y2:
#         print('Border')
#     else:
#         print('Inside / Outside')
# elif y == y1 or y == y2:
#     if x1 <= x <= x2:
#         print('Border')
#     else:
#         print('Inside / Outside')
# else:
#     print('Inside / Outside')

# 09. Numbers from 1 to 10
# i = 1
# while i < 11:
#     print(i)
#     i = i +1

# 10. Multiply by 2
i = float(input())
while 0 <= i:
    print("Result: " + format(i * 2, '.2f'))
    i = float(input())
    continue
else:
    print('Negative number!')

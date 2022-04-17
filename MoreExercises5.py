# 01. Back To The Past
# heritage_money = float(input())
# target_year = int(input())
# age = 18
# for i in range(1800, target_year + 1):
#     if i % 2 == 0:
#         heritage_money -= 12000
#         age += 1
#     else:
#         heritage_money -= (12000 + (50 * age))
#         age += 1
#     if i == target_year:
#         break
# if heritage_money >= 0:
#     print(f"Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.")
# else:
#     print(f"He will need {abs(heritage_money):.2f} dollars to survive.")

# 02. Hospital
# needed_period = int(input())
# treated_patients = 0
# untreated_patients = 0
# number_of_doctors = 7
# for i in range(1, needed_period + 1):
#     number_patients = int(input())
#     if i % 3 == 0 and untreated_patients > treated_patients:
#         number_of_doctors += 1
#     if number_patients <= number_of_doctors:
#         treated_patients += number_patients
#     else:
#         untreated_patients += number_patients - number_of_doctors
#         treated_patients += number_of_doctors
# print(f"Treated patients: {treated_patients}.")
# print(f"Untreated patients: {untreated_patients}.")

# 03. Logistics
# number_of_cargo = int(input())
# total_tonnage = 0
# carriage_sum = 0
# bus_weight = 0
# truck_weight = 0
# train_weight = 0
# for i in range(1, number_of_cargo + 1):
#     weight_of_cargo = int(input())
#     total_tonnage += weight_of_cargo
#     if 1 <= weight_of_cargo <= 3:
#         carriage_sum += weight_of_cargo * 200
#         bus_weight += weight_of_cargo
#     elif 4 <= weight_of_cargo <= 11:
#         carriage_sum += weight_of_cargo * 175
#         truck_weight += weight_of_cargo
#     elif 12 <= weight_of_cargo:
#         carriage_sum += weight_of_cargo * 120
#         train_weight += weight_of_cargo
# print(f"{carriage_sum/total_tonnage:.2f}")
# print(f"{((bus_weight/total_tonnage)*100):.2f}%")
# print(f"{((truck_weight/total_tonnage)*100):.2f}%")
# print(f"{((train_weight/total_tonnage)*100):.2f}%")

# 04. Grades
# number_of_students = int(input())
# top_students = 0
# good_students = 0
# average_students = 0
# failed_students = 0
# total_results = 0
# for i in range(1, number_of_students + 1):
#     exam_result = float(input())
#     if 5 <= exam_result:
#         top_students += 1
#         total_results += exam_result
#     elif 4 <= exam_result <= 4.99:
#         good_students += 1
#         total_results += exam_result
#     elif 3 <= exam_result <= 3.99:
#         average_students += 1
#         total_results += exam_result
#     elif exam_result < 3:
#         failed_students += 1
#         total_results += exam_result
# print(f"Top students: {((top_students/number_of_students)*100):.2f}%")
# print(f"Between 4.00 and 4.99: {((good_students/number_of_students)*100):.2f}%")
# print(f"Between 3.00 and 3.99: {((average_students/number_of_students)*100):.2f}%")
# print(f"Fail: {((failed_students/number_of_students)*100):.2f}%")
# print(f"Average: {(total_results/number_of_students):.2f}")

# 05. Game Of Intervals
# number_of_entries = int(input())
# total_points = 0
# zero_to_nine = 0
# teens = 0
# twenties = 0
# thirties = 0
# forties = 0
# invalid_numbers = 0
# for i in range(1, number_of_entries + 1):
#     command_number = int(input())
#     if command_number < 0 or command_number > 50:
#         total_points = total_points / 2
#         invalid_numbers += 1
#     elif 0 <= command_number <= 9:
#         total_points += command_number * 0.2
#         zero_to_nine += 1
#     elif 10 <= command_number <= 19:
#         total_points += command_number * 0.3
#         teens += 1
#     elif 20 <= command_number <= 29:
#         total_points += command_number * 0.4
#         twenties += 1
#     elif 30 <= command_number <= 39:
#         total_points += 50
#         thirties += 1
#     elif 40 <= command_number <= 50:
#         total_points += 100
#         forties += 1
# print(f"{total_points:.2f}")
# print(f"From 0 to 9: {((zero_to_nine/number_of_entries)*100):.2f}%")
# print(f"From 10 to 19: {((teens/number_of_entries)*100):.2f}%")
# print(f"From 20 to 29: {((twenties/number_of_entries)*100):.2f}%")
# print(f"From 30 to 39: {((thirties/number_of_entries)*100):.2f}%")
# print(f"From 40 to 50: {((forties/number_of_entries)*100):.2f}%")
# print(f"Invalid numbers: {((invalid_numbers/number_of_entries)*100):.2f}%")

# 06. Bills
# number_of_months = int(input())
# electric_total = 0
# other_utilities = 0
# water_total = 0
# internet_total = 0
# for i in range(1, number_of_months + 1):
#     electricity_bill = float(input())
#     electric_total += electricity_bill
#     water_total += 20
#     internet_total += 15
#     other_utilities += ((electricity_bill + 20 + 15) * 1.2)
# print(f"Electricity: {electric_total:.2f} lv")
# print(f"Water: {20 * number_of_months:.2f} lv")
# print(f"Internet: {15 * number_of_months:.2f} lv")
# print(f"Other: {other_utilities:.2f} lv")
# print(f"Average: {(electric_total + water_total + internet_total + other_utilities)/number_of_months:.2f} lv")

# 07. Football League
# stadium_capacity = int(input())
# number_of_fans = int(input())
# sector_a = 0
# sector_b = 0
# sector_v = 0
# sector_g = 0
# for i in range(1, number_of_fans + 1):
#     stadium_sector = input()
#     if stadium_sector == "A":
#         sector_a += 1
#     elif stadium_sector == "B":
#         sector_b += 1
#     elif stadium_sector == "V":
#         sector_v += 1
#     elif stadium_sector == "G":
#         sector_g += 1
# print(f"{((sector_a/number_of_fans) * 100):.2f}%")
# print(f"{((sector_b/number_of_fans) * 100):.2f}%")
# print(f"{((sector_v/number_of_fans) * 100):.2f}%")
# print(f"{((sector_g/number_of_fans) * 100):.2f}%")
# print(f"{((number_of_fans/stadium_capacity) * 100):.2f}%")

# 08. Equal Pairs
# number_of_entries = int(input()) * 2
# pair_total = 0
# list_of_pairs = []
# list_of_pair_difference = []
# for i in range(0, number_of_entries, 2):
#     number_one = int(input())
#     number_two = int(input())
#     pair_total = number_one + number_two
#     list_of_pairs += [pair_total]
# element = list_of_pairs[0]
# check = True
# j = 0
# for item in list_of_pairs:
#     if element != item:
#         list_of_pair_difference += [abs(list_of_pairs[j + 1] - list_of_pairs[j])]
#         check = False
#         j += 1
# if check:
#     print(f"Yes, value={list_of_pairs[0]}")
# else:
#     print(f"No, maxdiff={max(list_of_pair_difference)}")

# 09. Clock
# for i in range(0, 24):
#     for j in range(0, 60):
#         print(f"{i} : {j}")

# 10. Clock - part 2
for i in range(0, 24):
    for j in range(0, 60):
        for m in range(0, 60):
            print(f"{i} : {j} : {m}")

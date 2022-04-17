# 01. Sum Seconds
# from math import floor
# first_seconds = int(input())
# second_seconds = int(input())
# third_seconds = int(input())
# total_minutes = floor((first_seconds + second_seconds + third_seconds) / 60)
# total_seconds = (first_seconds + second_seconds + third_seconds) % 60
# if total_seconds < 10:
#     print(f"{total_minutes}:0{total_seconds}")
# else:
#     print(f"{total_minutes}:{total_seconds}")

# 02. Bonus Score
# score = int(input())
# if score <= 100:
#     if score % 2 == 0:
#         bonus_points = 6
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     elif score % 5 == 0:
#         bonus_points = 7
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     else:
#         bonus_points = 5
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
# elif 100 < score <= 1000:
#     if score % 2 == 0:
#         bonus_points = (score * 0.2) + 1
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     elif score % 5 == 0:
#         bonus_points = (score * 0.2) + 2
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     else:
#         bonus_points = score * 0.2
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
# else:
#     if score % 2 == 0:
#         bonus_points = (score * 0.1) + 1
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     elif score % 5 == 0:
#         bonus_points = (score * 0.1) + 2
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)
#     else:
#         bonus_points = score * 0.1
#         total_points = score + bonus_points
#         print(bonus_points)
#         print(total_points)

# 03. Speed Info
# speed = float(input())
# if speed <= 10:
#     print("slow")
# elif 10 < speed <= 50:
#     print("average")
# elif 50 < speed <= 150:
#     print("fast")
# elif 150 < speed <= 1000:
#     print("ultra fast")
# else:
#     print("extremely fast")

# 04. Metric Converter
# length = float(input())
# input_measure = input()
# output_measure = input()
# if input_measure == "m":
#     if output_measure == "cm":
#         print(format(length * 100, ".3f"))
#     elif output_measure == "mm":
#         print(format(length * 1000, ".3f"))
# elif input_measure == "cm":
#     if output_measure == "m":
#         print(format(length / 100, ".3f"))
#     elif output_measure == "mm":
#         print(format(length * 10, ".3f"))
# elif input_measure == "mm":
#     if output_measure == "m":
#         print(format(length / 1000, ".3f"))
#     elif output_measure == "cm":
#         print(format(length / 10, ".3f"))

# 05. Time + 15 Minutes
# hour_input = int(input())
# minute_input = int(input())
# if 45 <= minute_input <= 59:
#     if hour_input < 23:
#         hour_input += 1
#         minute_to_show = minute_input - 45
#         if minute_to_show < 10:
#             print(f"{hour_input}:0{abs(minute_to_show)}")
#         else:
#             print(f"{hour_input}:{abs(minute_to_show)}")
#     else:
#         hour_input = 0
#         minute_to_show = minute_input - 45
#         if minute_to_show < 10:
#             print(f"{hour_input}:0{abs(minute_to_show)}")
#         else:
#             print(f"{hour_input}:{abs(minute_to_show)}")
# else:
#     minute_to_show = minute_input + 15
#     if minute_to_show < 10:
#         print(f"{hour_input}:0{minute_to_show}")
#     else:
#         print(f"{hour_input}:{minute_to_show}")

# 06. Godzilla vs. Kong
# film_budget = float(input())
# number_of_artists = int(input())
# price_of_clothing = float(input())
# price_of_decor = film_budget * 0.1
# if 150 <= number_of_artists:
#     clothing_budget = (number_of_artists * price_of_clothing ) * 0.9
#     if (clothing_budget + price_of_decor) <= film_budget:
#         print("Action!")
#         print(f"Wingard starts filming with {format(film_budget - clothing_budget - price_of_decor, '.2f')} leva left.")
#     else:
#         print("Not enough money!")
#         print(f"Wingard needs {format(abs(film_budget - clothing_budget - price_of_decor), '.2f')} leva more.")
# else:
#     clothing_budget = number_of_artists * price_of_clothing
#     if (clothing_budget + price_of_decor) <= film_budget:
#         print("Action!")
#         print(f"Wingard starts filming with {format(film_budget - clothing_budget - price_of_decor, '.2f')} leva left.")
#     else:
#         print("Not enough money!")
#         print(f"Wingard needs {format(abs(film_budget - clothing_budget - price_of_decor), '.2f')} leva more.")

# 07. World Swimming Record
# from math import floor
# record_seconds = float(input())
# length = float(input())
# speed_per_meter = float(input())
# swimming_time = length * speed_per_meter + floor(length / 15) * 12.5
# if record_seconds <= swimming_time:
#     print(f"No, he failed! He was {format(swimming_time - record_seconds, '.2f')} seconds slower.")
# else:
#     print(f"Yes, he succeeded! The new world record is {format(swimming_time, '.2f')} seconds.")

# 08. Scholarship
from math import floor

income = float(input())
grade_point_average = float(input())
minimum_wage = float(input())
gpa_scholarship = grade_point_average * 25
social_scholarship = minimum_wage * 0.35
if income < minimum_wage and 5.5 <= grade_point_average:
    if social_scholarship < gpa_scholarship:
        print(f"You get a scholarship for excellent results {floor(gpa_scholarship)} BGN")
    elif social_scholarship == gpa_scholarship:
        print(f"You get a scholarship for excellent results {floor(gpa_scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif 5.5 <= grade_point_average:
    print(f"You get a scholarship for excellent results {floor(gpa_scholarship)} BGN")
elif income < minimum_wage and 4.5 < grade_point_average < 5.5:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")

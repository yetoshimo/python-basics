# 01. Excellent Result
# grade = float(input())
# if 5.5 <= grade:
#     print("Excellent!")

# 02. Greater Number
# number_1 = int(input())
# number_2 = int(input())
# if number_2 < number_1:
#     print(number_1)
# else:
#     print(number_2)

# 03. Even or Odd
# number = int(input())
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 04. Number 100...200
# number = int(input())
# if number < 100:
#     print("Less than 100")
# elif 100 <= number <= 200:
#     print("Between 100 and 200")
# else:
#     print("Greater than 200")

# 05. Password Guess
# password_string = input()
# if password_string == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# else:
#     print("Wrong password!")

# 06. Area of Figures
# from math import pi
# geometric_shape = input()
# if geometric_shape == "square":
#     first_input = float(input())
#     print(format(first_input * first_input, ".3f"))
# elif geometric_shape == "rectangle":
#     first_input = float(input())
#     second_input = float(input())
#     print(format(first_input * second_input, ".3f"))
# elif geometric_shape == "circle":
#     first_input = float(input())
#     print(format(first_input * first_input * pi, ".3f"))
# elif geometric_shape == "triangle":
#     first_input = float(input())
#     second_input = float(input())
#     print(format(first_input * second_input / 2, ".3f"))

# 07. Toy Shop
price_of_holiday = float(input())
number_of_puzzles = int(input())
number_of_puppets = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
total_number_of_purchase = number_of_puzzles + number_of_puppets + number_of_bears + number_of_minions + number_of_trucks
if 50 <= total_number_of_purchase:
    total_sum = ((
                             number_of_puzzles * 2.6 + number_of_puppets * 3 + number_of_bears * 4.1 + number_of_minions * 8.2 + number_of_trucks * 2) * 0.75) * 0.9
    if price_of_holiday <= total_sum:
        print(f"Yes! {format(total_sum - price_of_holiday, '.2f')} lv left.")
    else:
        print(f"Not enough money! {format(price_of_holiday - total_sum, '.2f')} lv needed.")
else:
    total_sum = (
                            number_of_puzzles * 2.6 + number_of_puppets * 3 + number_of_bears * 4.1 + number_of_minions * 8.2 + number_of_trucks * 2) * 0.9
    if price_of_holiday <= total_sum:
        print(f"Yes! {format(total_sum - price_of_holiday, '.2f')} lv left.")
    else:
        print(f"Not enough money! {format(price_of_holiday - total_sum, '.2f')} lv needed.")

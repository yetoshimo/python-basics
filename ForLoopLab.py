# 01. Numbers from 1 to 100
# for i in range(1, 101):
#     print(i)

# 02. Numbers 1...N with Step 3
# given_number = int(input())
# for i in range(1, given_number+1, 3):
#     print(i)

# 03. Even Powers of 2
# from math import pow
# power_of_two = int(input())
# for i in range(0, power_of_two+1, 1):
#     if i % 2 == 0:
#         print(f"{pow(2, i):.0f}")
#     else:
#         pass

# 04. Numbers N...1
# given_number = int(input())
# for i in range(given_number, 0, -1):
#     print(i)

# 05. Character Sequence
# given_text = input()
# for i in given_text:
#     print(i)

# 06. Vowels Sum
# given_text = input()
# vowels_list = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
# total_of_vowels = 0
# for i in given_text:
#     if i in vowels_list:
#         total_of_vowels += vowels_list[i]
#     else:
#         pass
# print(total_of_vowels)

# 07. Sum Numbers
# total_of_numbers = int(input())
# sum_of_numbers = 0
# for i in range(1, total_of_numbers+1):
#     sum_of_numbers += int(input())
# print(sum_of_numbers)

# 08. Number sequence
# total_of_numbers = int(input())
# number_series = []
# entered_number = 0
# for i in range(1, total_of_numbers+1):
#     entered_number = int(input())
#     number_series.append(entered_number)
# print(f"Max number: {max(number_series)}")
# print(f"Min number: {min(number_series)}")

# 09. Left and Right Sum
# power_numbers = int(input())
# total_of_numbers = power_numbers * 2
# left_entered_number = 0
# right_entered_number = 0
# half_of_the_list = total_of_numbers // 2
# for i in range(1, half_of_the_list+1):
#     left_entered_number += int(input())
# for i in range(half_of_the_list+1, total_of_numbers+1):
#     right_entered_number += int(input())
# if left_entered_number == right_entered_number:
#     print(f"Yes, sum = {left_entered_number}")
# else:
#     print(f"No, diff = {abs(left_entered_number - right_entered_number)}")

# 10. Odd Even Sum
# total_of_numbers = int(input())
# even_sum = 0
# odd_sum = 0
# for i in range(1, total_of_numbers+1):
#     if i % 2 != 0:
#         odd_sum += int(input())
#     else:
#         even_sum += int(input())
# if even_sum == odd_sum:
#     print("Yes")
#     print(f"Sum = {even_sum}")
# else:
#     print(f"No")
#     print(f"Diff = {abs(even_sum - odd_sum)}")

# 11. Clever Lily
age_of_lily = int(input())
price_of_machine = float(input())
price_of_toy = int(input())
toy_sell_sum = 0
money_gather_sum = 0
total_money = 0
for i in range(1, age_of_lily + 1):
    if i % 2 != 0:
        toy_sell_sum += price_of_toy
    else:
        money_gather_sum += (i * 5) - 1
total_money = toy_sell_sum + money_gather_sum
if total_money >= price_of_machine:
    print(f"Yes! {format(total_money - price_of_machine, '.2f')}")
else:
    print(f"No! {format(abs(total_money - price_of_machine), '.2f')}")

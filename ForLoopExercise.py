# 01. Numbers Ending in 7
# for i in range(1, 1001):
#     if i % 10 == 7:
#         print(i)
#     else:
#         pass

# 02. Half Sum Element
# total_number_entries = int(input())
# entered_number = 0
# max_number = 0
# sum_of_the_list = 0
# list_of_numbers = []
# for i in range(0, total_number_entries):
#     entered_number = int(input())
#     list_of_numbers += [entered_number]
#     max_number = max(list_of_numbers)
#     sum_of_the_list = sum(list_of_numbers) - max_number
# if sum_of_the_list == max_number:
#     print("Yes")
#     print(f"Sum = {max_number}")
# else:
#     print("No")
#     print(f"Diff = {abs(sum_of_the_list - max_number)}")

# 03. Odd / Even Position
# total_number_entries = int(input())
# entered_number = 0
# total_odd_sum = 0
# min_odd_number = 0
# max_odd_number = 0
# odd_numbers_list = []
# total_even_sum = 0
# min_even_number = 0
# max_even_number = 0
# even_numbers_list = []
# for i in range(1, total_number_entries+1):
#     entered_number = float(input())
#     if i % 2 == 0:
#         total_even_sum += entered_number
#         even_numbers_list += [entered_number]
#         min_even_number = min(even_numbers_list)
#         max_even_number = max(even_numbers_list)
#     else:
#         total_odd_sum += entered_number
#         odd_numbers_list += [entered_number]
#         min_odd_number = min(odd_numbers_list)
#         max_odd_number = max(odd_numbers_list)
# if total_odd_sum != 0:
#     print(f"OddSum={total_odd_sum:.2f},")
#     print(f"OddMin={min_odd_number:.2f},")
#     print(f"OddMax={max_odd_number:.2f},")
# else:
#     print(f"OddSum={total_odd_sum:.2f},")
#     print(f"OddMin=No,")
#     print(f"OddMax=No,")
# if total_even_sum != 0:
#     print(f"EvenSum={total_even_sum:.2f},")
#     print(f"EvenMin={min_even_number:.2f},")
#     print(f"EvenMax={max_even_number:.2f}")
# else:
#     print(f"EvenSum={total_even_sum:.2f},")
#     print(f"EvenMin=No,")
#     print(f"EvenMax=No")

# 04. Histogram
# total_number_entries = int(input())
# entered_number = 0
# p1_list = []
# p1_list_numbers = 0
# p2_list = []
# p2_list_numbers = 0
# p3_list = []
# p3_list_numbers = 0
# p4_list = []
# p4_list_numbers = 0
# p5_list = []
# p5_list_numbers = 0
# for i in range(0, total_number_entries):
#     entered_number = int(input())
#     if 1 <= entered_number < 200:
#         p1_list += [entered_number]
#         p1_list_numbers = len(p1_list)
#     elif 200 <= entered_number <= 399:
#         p2_list += [entered_number]
#         p2_list_numbers = len(p2_list)
#     elif 400 <= entered_number <= 599:
#         p3_list += [entered_number]
#         p3_list_numbers = len(p3_list)
#     elif 600 <= entered_number <= 799:
#         p4_list += [entered_number]
#         p4_list_numbers = len(p4_list)
#     else:
#         p5_list += [entered_number]
#         p5_list_numbers = len(p5_list)
# print(f"{(p1_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p2_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p3_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p4_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p5_list_numbers/total_number_entries) * 100:.2f}%")

# 05. Divide Without Remainder
# total_number_entries = int(input())
# entered_number = 0
# p1_list = []
# p1_list_numbers = 0
# p2_list = []
# p2_list_numbers = 0
# p3_list = []
# p3_list_numbers = 0
# for i in range(0, total_number_entries):
#     entered_number = int(input())
#     if entered_number % 2 == 0:
#         p1_list += [entered_number]
#         p1_list_numbers = len(p1_list)
#     if entered_number % 3 == 0:
#         p2_list += [entered_number]
#         p2_list_numbers = len(p2_list)
#     if entered_number % 4 == 0:
#         p3_list += [entered_number]
#         p3_list_numbers = len(p3_list)
# print(f"{(p1_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p2_list_numbers/total_number_entries) * 100:.2f}%")
# print(f"{(p3_list_numbers/total_number_entries) * 100:.2f}%")

# 06. Salary
number_of_opened_tabs = int(input())
salary = int(input())
fine_sites_list = {"Facebook": 150, "Instagram": 100, "Reddit": 50}
for i in range(0, number_of_opened_tabs):
    url_of_the_tab = input()
    if url_of_the_tab in fine_sites_list:
        salary -= fine_sites_list[url_of_the_tab]
    if salary > 0:
        continue
    else:
        print("You have lost your salary.")
        break
if salary > 0:
    print(f"{salary:.0f}")

# 01. Dishwasher
# detergent = int(input()) * 750
# dishes_washed = 0
# washing_count = 0
# pots_washed = 0
# while 0 <= detergent:
#     washing_count += 1
#     if washing_count == 3:
#         pots = input()
#         if pots != "End":
#             pots = int(pots)
#             detergent = detergent - (pots * 15)
#             if detergent < 0:
#                 print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
#                 break
#             else:
#                 pots_washed = pots_washed + pots
#                 washing_count = 0
#         else:
#             print("Detergent was enough!")
#             print(f"{dishes_washed} dishes and {pots_washed} pots were washed.")
#             print(f"Leftover detergent {detergent} ml.")
#             break
#     else:
#         dishes = input()
#         if dishes != "End":
#             dishes = int(dishes)
#             detergent = detergent - (dishes * 5)
#             if detergent < 0:
#                 print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
#                 break
#             else:
#                 dishes_washed = dishes_washed + dishes
#         else:
#             print("Detergent was enough!")
#             print(f"{dishes_washed} dishes and {pots_washed} pots were washed.")
#             print(f"Leftover detergent {detergent} ml.")
#             break

# 02. Report System
# donation_target = int(input())
# cash_counter = 0
# credit_counter = 0
# cash_paid = 0
# credit_paid = 0
# while 0 < donation_target:
#     cash_transaction = input()
#     if cash_transaction != "End" and cash_transaction != "0":
#         cash_transaction = int(cash_transaction)
#         if cash_transaction <= 100:
#             cash_paid = cash_paid + cash_transaction
#             cash_counter += 1
#             print("Product sold!")
#             donation_target = donation_target - cash_transaction
#         else:
#             print("Error in transaction!")
#     else:
#         print("Failed to collect required money for charity.")
#         break
#     credit_transaction = input()
#     if credit_transaction != "End" and credit_transaction != "0":
#         credit_transaction = int(credit_transaction)
#         if 10 <= credit_transaction:
#             credit_paid = credit_paid + credit_transaction
#             credit_counter += 1
#             print("Product sold!")
#             donation_target = donation_target - credit_transaction
#         else:
#             print("Error in transaction!")
#     else:
#         print("Failed to collect required money for charity.")
#         break
#     if donation_target <= 0:
#         print(f"Average CS: {format(cash_paid/cash_counter, '.2f')}")
#         print(f"Average CC: {format(credit_paid/credit_counter, '.2f')}")

# 03. Stream Of Letters
# letter = input()
# letter_check = letter.isalpha()
# new_word = ""
# whole_word = ""
# master_word = ""
# secret_word = 0
# c_count = 0
# o_count = 0
# n_count = 0
# while letter != "End":
#     if letter_check is True:
#         if letter == "c":
#             c_count += 1
#             if c_count < 2:
#                 secret_word += 1
#                 if secret_word < 3:
#                     letter = input()
#                     letter_check = letter.isalpha()
#                 else:
#                     secret_word = 0
#                     c_count = 0
#                     o_count = 0
#                     n_count = 0
#                     new_word = new_word + str(" ")
#                     master_word = new_word
#                     letter = input()
#                     letter_check = letter.isalpha()
#             else:
#                 new_word += letter
#                 letter = input()
#                 letter_check = letter.isalpha()
#         elif letter == "o":
#             o_count += 1
#             if o_count < 2:
#                 secret_word += 1
#                 if secret_word < 3:
#                     letter = input()
#                     letter_check = letter.isalpha()
#                 else:
#                     secret_word = 0
#                     c_count = 0
#                     o_count = 0
#                     n_count = 0
#                     new_word = new_word + str(" ")
#                     master_word = new_word
#                     letter = input()
#                     letter_check = letter.isalpha()
#             else:
#                 new_word += letter
#                 letter = input()
#                 letter_check = letter.isalpha()
#         elif letter == "n":
#             n_count += 1
#             if n_count < 2:
#                 secret_word += 1
#                 if secret_word < 3:
#                     letter = input()
#                     letter_check = letter.isalpha()
#                 else:
#                     secret_word = 0
#                     c_count = 0
#                     o_count = 0
#                     n_count = 0
#                     new_word = new_word + str(" ")
#                     master_word = new_word
#                     letter = input()
#                     letter_check = letter.isalpha()
#             else:
#                 new_word += letter
#                 letter = input()
#                 letter_check = letter.isalpha()
#         else:
#             new_word += letter
#             letter = input()
#             letter_check = letter.isalpha()
#     else:
#         letter = input()
#         letter_check = letter.isalpha()
# else:
#     print(master_word)

# 04. Numbers Divided by 3 Without Reminder
# for i in range (1, 101):
#     if i % 3 == 0:
#         print(i)

# 05. Average Number
how_many_numbers = int(input())
counter = how_many_numbers
total_number = 0
while 1 <= counter:
    total_number += int(input())
    counter -= 1
else:
    final_number = format(total_number / how_many_numbers, ".2f")
    print(final_number)

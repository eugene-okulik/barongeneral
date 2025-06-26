import random

try:
    salary = int(input("Введите зарплату:"))
except (ValueError, EOFError):
    print("Ошибка при вводе зарплаты. Установлено значение 0.")
    salary = 0

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(100, 3500)
    final_salary = salary + bonus_amount
else:
    final_salary = salary

print(f"{salary}, {bonus} - '${final_salary}'")

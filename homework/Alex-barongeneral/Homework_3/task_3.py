import math

num1 = 16
num2 = 4   

average_arithmetic = (num1 + num2) / 2

if num1 >= 0 and num2 >= 0:
    average_geometric = math.sqrt(num1 * num2)
    print(f"{average_geometric}")
else:
    print("Ошибка")
print(f"{average_arithmetic}")

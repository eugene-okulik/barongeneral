def get_number(line):
    return int(line.split()[-1]) + 10


lines = [

    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    print(get_number(line))
    
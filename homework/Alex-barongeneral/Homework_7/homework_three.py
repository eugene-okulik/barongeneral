def process_result(line):
    return int(line.split()[-1]) + 10

lines = ["результат операции: 42", "результат операции: 54", "результат работы программы: 209", "результат: 2"]

list(map(lambda x: print(process_result(x)), lines))
import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
target_indices = [5, 200, 1000, 100000]
results = {}

for i in range(1, max(target_indices) + 1):
    num = next(fib_gen)
    if i in target_indices:
        results[i] = num

for index in sorted(target_indices):
    print(f"{index}-е число Фибоначчи: {results[index]}")

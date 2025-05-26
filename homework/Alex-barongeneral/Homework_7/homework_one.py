secret_number = 19
while True:
    user_input = input("Угадайте цифру (или введите 'Выход' для выхода): ")
    if user_input == "Выход":
        print("До свидания!")
        break
    guess = int(user_input)
    if guess == secret_number:
        print("Верно!")
        print("До свидания!")
        break
    else:
        print("Попробуйте снова")

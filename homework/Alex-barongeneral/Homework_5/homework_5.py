person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name)
print(last_name)
print(city)
print(phone)
print(country)

line1 = 'результат операции: 42'
line2 = 'результат операции: 514'
line3 = 'результат работы программы: 9'

num1 = int(line1[line1.index(':') + 2:]) + 10
num2 = int(line2[line2.index(':') + 2:]) + 10
num3 = int(line3[line3.index(':') + 2:]) + 10

print(num1)
print(num2)
print(num3)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")

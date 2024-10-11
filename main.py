"""
 _____         _      __  
|_   _|       | |    /  | 
  | | __ _ ___| | __ `| | 
  | |/ _` / __| |/ /  | | 
  | | (_| \__ \   <  _| |_
  \_/\__,_|___/_|\_\ \___/

Напишите программу, которая выводит в консоль "Hello world"

hint: что такое print?
"""

print('Hello world!')

"""
 _____         _      _____ 
|_   _|       | |    / __  \
  | | __ _ ___| | __ `' / /'
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /___
  \_/\__,_|___/_|\_\ \_____/

Напишите рограмму, которая выводит числа от 1 до введенного пользователем. Для чисел, кратных 3, выводится "Fizz",'
для кратных 5 — "Buzz", а для чисел, кратных 3 и 5 — "FizzBuzz"

hint: цикл, если и "%"
"""

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

try:
    user_input = int(input("Введите число: "))
    fizz_buzz(user_input)
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
"""
 _____         _      _____ 
|_   _|       | |    |____ |
  | | __ _ ___| | __     / /
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  .___/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая проверяет, является ли введенный пользователем год високосным

hint: https://ru.wikihow.com/%D0%B2%D1%8B%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B5-%D0%B3%D0%BE%D0%B4%D1%8B
"""

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
  return False

try:
    user_input = int(input("Введите год: "))
    if is_leap_year(user_input):
        print(f"{user_input} является високосным годом.")
    else:
        print(f"{user_input} не является високосным годом.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

"""
 _____         _        ___ 
|_   _|       | |      /   |
  | | __ _ ___| | __  / /| |
  | |/ _` / __| |/ / / /_| |
  | | (_| \__ \   <  \___  |
  \_/\__,_|___/_|\_\     |_/

Напишите программау, которая проверяет, является ли введенная пользователем строка или число палиндромом, то есть читается ли оно одинаково с обеих сторон

hint: https://letpy.com/handbook/builtins/reversed/
"""

def is_palindrome(value):
    cleaned_value = str(value).replace(" ", "").lower()
    return cleaned_value == cleaned_value[::-1]

user_input = input("Введите строку или число: ")

if is_palindrome(user_input):
    print(f"{user_input} является палиндромом.")
else:
    print(f"{user_input} не является палиндромом.")

"""
 _____         _      _____ 
|_   _|       | |    |  ___|
  | | __ _ ___| | __ |___ \ 
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  /\__/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая запрашивает число у пользователя и вычисляет факториал заданного числа, используя цикл или рекурсию

hint: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
"""

def factorial_iterative(x):
    if x < 0:
        return "Факториал не определен для отрицательных чисел."
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

try:
    user_input = int(input("Введите неотрицательное целое число: "))
    print(f"Факториал {user_input} равен {factorial_iterative(user_input)}.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

"""
 _____         _       ____ 
|_   _|       | |     / ___|
  | | __ _ ___| | __ / /___ 
  | |/ _` / __| |/ / | ___ \
  | | (_| \__ \   <  | \_/ |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая проверяет, является ли число простым (делится только на 1 и само на себя). Используйте перебор делителей.

hint: x <= 1 - не простые числа
hint 2: %
"""

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

try:
    user_input = int(input("Введите целое число: "))
    if is_prime(user_input):
        print(f"{user_input} является простым числом.")
    else:
        print(f"{user_input} не является простым числом.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

"""
 _____         _      ______
|_   _|       | |    |___  /
  | | __ _ ___| | __    / / 
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /   
  \_/\__,_|___/_|\_\ \_/    

Напишите программу, которая находит сумму всех цифр числа

hint: циклы
"""

def sum_of_digits(x):
    total = 0
    x = abs(x) 
    while x > 0:
        total += x % 10  
        x //= 10  
    return total

try:
    user_input = int(input("Введите целое число: "))
    result = sum_of_digits(user_input)
    print(f"Сумма всех цифр числа {user_input} равна {result}.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")

"""
 _____         _      _____ 
|_   _|       | |    |  _  |
  | | __ _ ___| | __  \ V / 
  | |/ _` / __| |/ /  / _ \ 
  | | (_| \__ \   <  | |_| |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая генерирует последовательность Фибоначчи до указанного числа или количества элементов

hint: 1, 1, 2, 3 https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
hint 2: попробуйте решить с помощью рекурсии
"""

def fibonacci_count(x):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(x):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

try:
    count = int(input("Введите количество элементов последовательности Фибоначчи: "))
    if count < 0:
        print("Пожалуйста, введите неотрицательное число.")
    else:
        result = fibonacci_count(count)
        print(f"Последовательность Фибоначчи до {count} элементов: {result}")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")





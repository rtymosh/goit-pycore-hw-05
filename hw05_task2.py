# Завдання 2

# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа в тексті записані без помилок,
# чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і розрахунку загального прибутку.


# Вимоги до завдання:

# Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа в тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
# Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.


# Рекомендації для виконання:

# Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа чітко відокремлені пробілами.
# Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
# Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.


# Критерії оцінювання:

# Правильність визначення та повернення дійсних чисел функцією generator_numbers.
# Коректність обчислення загальної суми в sum_profit.
# Чистота коду, наявність коментарів і відповідність стилю кодування PEP8.


# Приклад використання:

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")


# Очікуване виведення:

# Загальний дохід: 1351.46

import re
from typing import Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Regular expression to find floating-point numbers surrounded by spaces
    pattern = r"(?<=\s)(-?\d+\.\d+)(?=\s)"
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: callable) -> float:
    total = 0.0
    for number in func(text):
        total += number
    return total


# Usage example:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів don't touch this10000 nubmers."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
text2 = "Need to sum up 2500.50 dollars, with  1500.75 dollars and these sum 300.26 dollars and minus -500.00 and do not use or 10000numbers."
total_income2 = sum_profit(text2, generator_numbers)
print(f"Загальний дохід: {total_income2}")

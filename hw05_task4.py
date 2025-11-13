# Завдання 4

# Доробіть консольного бота-помічника з попереднього домашнього завдання та додайте обробку помилок за допомогою декораторів.


# Вимоги до завдання:

# Усі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях handler, і це винятки KeyError, ValueError, IndexError. Коли відбувається виняток, декоратор повинен повертати потрібну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# Як приклад додамо декоратор input_error для обробки помилки ValueError.

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner


# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

# @input_error
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."


# Вам треба додати обробники до інших команд (функцій), а також додати в декоратор обробку винятків інших типів з відповідними повідомленнями.


# Критерії оцінювання:

# Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
# Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
# Кожна функція для обробки команд має декоратор input_error, який обробляє відповідні помилки та повертає повідомлення про помилку.
# Коректна реакція бота на різні команди й обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог із ботом повинен бути схожим на цей.

# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356
# Enter a command:


# from commands_handler import add_contact, change_contact, show_phone, show_all  # noqa, do not realize import modules now witnin functions


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name"

    return inner


def parse_input(user_input):  # parses user input into command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts) -> str:  # cmd: "add username phone"
    name, phone = args  # ValueError: if args is empty or does not have 2 elements
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts) -> str:  # cmd: "change username phone"
    name, phone = args  # ValueError: if args is empty or does not have 2 elements
    if name not in contacts:
        raise KeyError  # KeyError: explicitly raised if wrong contact name
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts) -> str:  # cmd: "phone username"
    name = args[0]  # IndexError: if args is empty
    if name not in contacts:
        raise KeyError  # KeyError: explicitly raised
    return f"{name}: {contacts[name]}"


def show_all(contacts) -> str:  # cmd: "all"
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        print("-" * 50)
        print(
            "Available commands:\n- hello\n- add username phone\n- change username phone\n- phone username\n- all\n- close / exit"
        )
        print("-" * 50)

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

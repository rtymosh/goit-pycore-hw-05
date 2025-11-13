# Завдання 3 (не обов'язкове)

# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен уміти читати лог-файл, переданий як аргумент командного рядка,
# і виводити статистику за рівнями логування: наприклад, INFO, ERROR, DEBUG.
# Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.


# Файли логів — це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах.
# Вони допомагають відстежувати й аналізувати поведінку системи, виявляти та діагностувати проблеми.


# Для виконання завдання візьміть наступний приклад лог-файлу:

# 2024-01-22 08:30:01 INFO User logged in successfully.
# 2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
# 2024-01-22 09:00:45 ERROR Database connection failed.
# 2024-01-22 09:15:10 INFO Data export completed.
# 2024-01-22 10:30:55 WARNING Disk usage above 80%.
# 2024-01-22 11:05:00 DEBUG Starting data backup process.
# 2024-01-22 11:30:15 ERROR Backup process failed.
# 2024-01-22 12:00:00 INFO User logged out.
# 2024-01-22 12:45:05 DEBUG Checking system health.
# 2024-01-22 13:30:30 INFO Scheduled maintenance.


# Вимоги до завдання:

# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати необов'язковий аргумент командного рядка після аргументу шляху до файлу логів.
# Він відповідає за виведення всіх записів певного рівня логування. І приймає значення відповідно до рівня логування файлу.
# Наприклад, аргумент error виведе всі записи рівня ERROR з файлу логів.
# Скрипт має зчитувати й аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня.
# Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати.
# Вона приймає результати виконання функції count_logs_by_level.


# Рекомендації для виконання:

# Перш ніж почати, ознайомтеся зі структурою вашого лог-файлу. Зверніть увагу на формат дати й часу, рівні логування INFO, ERROR, DEBUG, WARNING і структуру повідомлень.
# Зрозумійте, як розділені різні компоненти логу, це зазвичай пробіли або спеціальні символи.
# Розділіть ваше завдання на логічні блоки та функції для кращої читабельності й подальшого розширення.
# Парсинг рядка логу виконує функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення.
# Використовуйте методи рядків, як-от split(), для розділення рядка на частини.
# Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен рядок і застосовує до нього функцію parse_log_line, зберігаючи результати у список.
# Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. Вона дозволить вам отримати всі записи логу для певного рівня логування.
# Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, яка проходить по всіх записах і підраховує кількість записів для кожного рівня логування.
# Вивід результатів виконайте за допомогою функції display_log_counts(counts: dict), яка форматує та виводить результати підрахунку в читабельній формі.
# Ваш скрипт повинен уміти обробляти різні види помилок, як-от відсутність файлу або помилки при його читанні. Використовуйте блоки try / except для обробки виняткових ситуацій.


# Критерії оцінювання:

# Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
# Скрипт коректно обробляє такі помилки, як неправильний формат лог-файлу або відсутність файлу.
# При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функцію, списковий вираз, функцію filter тощо.
# Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.


# Приклад використання:

# При запуску скрипту

# python [main.py](<http://main.py/>) /path/to/logfile.log


# Ми повинні очікувати таке виведення:

# Рівень логування | Кількість
# -----------------|----------
# INFO             | 4
# DEBUG            | 3
# ERROR            | 2
# WARNING          | 1


# Якщо користувач хоче переглянути всі записи певного рівня логування, він може запустити скрипт із додатковим аргументом, наприклад:

# python main.py path/to/logfile.log error


# Це виведе загальну статистику за рівнями, а також детальну інформацію для всіх записів із рівнем ERROR.

# Рівень логування | Кількість
# -----------------|----------
# INFO             | 4
# DEBUG            | 3
# ERROR            | 2
# WARNING          | 1

# Деталі логів для рівня 'ERROR':
# 2024-01-22 09:00:45 - Database connection failed.
# 2024-01-22 11:30:15 - Backup process failed.


def parse_log_line(line: str) -> dict:  # Parse a single log line into its components
    parts = line.split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3] if len(parts) > 3 else "",
    }


def load_logs(file_path: str) -> list:  # Load logs from a file
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            logs.append(parse_log_line(line.strip()))
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:  # Filter logs by their level
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:  # Count logs by their level
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict) -> None:  # Display log counts in a formatted table
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print(f"{'-' * 17}-|{'-' * 8}")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please enter the path to the log file.")
        sys.exit(1)

    log_file_path = sys.argv[1]

    if len(sys.argv) > 2:
        filter_level = sys.argv[2]
        if filter_level.lower() not in ["info", "debug", "error", "warning"]:
            print("Invalid log level specified for filtering.")
            sys.exit(1)
    else:
        filter_level = None

    try:
        logs = load_logs(log_file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if filter_level:
            filtered_logs = filter_logs_by_level(logs, filter_level)
            print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")

    except FileNotFoundError:
        print(f"File is not found: {log_file_path}")
    except Exception as e:
        print(f"Another error occurred: {e}")

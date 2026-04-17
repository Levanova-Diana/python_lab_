"Запускающий модуль для лабораторных работ №4-6"

import typer
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

from rare_package import (
    unpack_recursive, unpack_iterative,
    sequence_recursive, sequence_iterative,
    get_file_reader, log_c,
    generate_primes
)

app = typer.Typer()


#лаба 4
@app.command()
def lab4():
    """Лабораторная №4: рекурсивные и итеративные алгоритмы"""
    rprint(Panel.fit("[bold cyan]Лабораторная работа №4[/bold cyan]", border_style="cyan"))

    print("\n1. Распаковка списка (рекурсия)")
    print("2. Распаковка списка (итеративно)")
    print("3. Последовательность w_i (рекурсия)")
    print("4. Последовательность w_i (итеративно)")

    choice = input("\nВыберите программу (1-4): ")

    if choice == "1":
        data_str = input("Введите данные (пример: [None, [1, ({2, 3}, {'foo': 'bar'})]]): ")
        try:
            data = eval(data_str)
            result = unpack_recursive(data)
            print(f"\nРезультат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        data_str = input("Введите данные (пример: [None, [1, ({2, 3}, {'foo': 'bar'})]]): ")
        try:
            data = eval(data_str)
            result = unpack_iterative(data)
            print(f"\nРезультат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "3":
        try:
            i = int(input("Введите номер члена последовательности: "))
            if i <= 0:
                print("Ошибка: номер должен быть положительным")
                return
            result = sequence_recursive(i)
            print(f"\nw_{i} = {result}")
        except ValueError:
            print("Ошибка: введите целое число")
        except RecursionError:
            print("Ошибка: слишком глубокий уровень рекурсии (попробуйте меньшее число)")

    elif choice == "4":
        try:
            i = int(input("Введите номер члена последовательности: "))
            if i <= 0:
                print("Ошибка: номер должен быть положительным")
                return
            result = sequence_iterative(i)
            print(f"\nw_{i} = {result}")
        except ValueError:
            print("Ошибка: введите целое число")

    else:
        print("Ошибка: неверный выбор! Введите 1, 2, 3 или 4")


#лаба 5
@app.command()
def lab5():
    "Лабораторная №5: замыкания и декораторы"
    rprint(Panel.fit("[bold magenta]Лабораторная работа №5[/bold magenta]", border_style="magenta"))

    print("\n1. Замыкание для чтения файла")
    print("2. Декоратор для логирования")

    choice = input("\nВыберите программу (1-2): ")

    if choice == "1":
        filename = input("Введите имя файла: ")
        try:
            reader = get_file_reader(filename)
            print("\nСодержимое файла:")
            line_num = 1
            while True:
                line = reader()
                if line is None:
                    break
                print(f"  {line_num}. {line}")
                line_num += 1
            if line_num == 1:
                print("  (файл пуст)")
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден!")
        except Exception as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        @log_c
        def add(a, b):
            return a + b

        @log_c
        def greet(name, msg="Привет"):
            return f"{msg}, {name}!"

        print("\n--- Пример 1: add(10, 20) ---")
        add(10, 20)

        print("\n--- Пример 2: greet('Петр') ---")
        greet("Петр")

        print("\n--- Пример 3: greet('Анна', msg='Здравствуй') ---")
        greet("Анна", msg="Здравствуй")

    else:
        print("Ошибка: неверный выбор! Введите 1 или 2")


#лаба 6
@app.command()
def lab6():
    """Лабораторная №6: генератор простых чисел"""
    rprint(Panel.fit("[bold green]Лабораторная работа №6[/bold green]", border_style="green"))

    print("Программа: Генератор простых чисел (Решето Эратосфена)\n")

    try:
        start = int(input("Введите нижнюю границу: "))
        end = int(input("Введите верхнюю границу: "))

        if start > end:
            print(f"Ошибка: нижняя граница ({start}) больше верхней ({end})")
            return

        primes = generate_primes(start, end)

        if not primes:
            print(f"\nПростых чисел в диапазоне [{start}, {end}] не найдено")
        else:
            print(f"\nПростые числа в диапазоне [{start}, {end}]:")
            print(primes)
            print(f"\nВсего найдено: {len(primes)}")

    except ValueError:
        print("Ошибка: введите целые числа!")


#меню
@app.command()
def menu():
    """Интерактивное меню для выбора лабораторной работы"""
    table = Table(title="[bold]Выберите лабораторную работу[/bold]", title_style="bold white")
    table.add_column("№", style="cyan", justify="center")
    table.add_column("Название", style="magenta")
    table.add_column("Описание", style="green")
    table.add_column("Кол-во программ", style="yellow", justify="center")

    table.add_row("4", "Рекурсия и итерация", "Распаковка списков, последовательности", "4")
    table.add_row("5", "Замыкания и декораторы", "Чтение файлов, логирование", "2")
    table.add_row("6", "Решето Эратосфена", "Генератор простых чисел", "1")

    rprint(table)

    choice = input("\nВведите номер лабораторной работы (4-6): ")

    if choice == "4":
        lab4()
    elif choice == "5":
        lab5()
    elif choice == "6":
        lab6()
    else:
        print("Ошибка: введите 4, 5 или 6!")


#запуск
if __name__ == "__main__":
    app()
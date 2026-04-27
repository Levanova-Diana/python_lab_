import time
#внешняя функция
def log_c(logging_enabled=True, show_time=True, show_args=True):
    #- logging_enabled: включить/выключить логирование (True/False)
    #- show_time: показывать время выполнения (True/False)
    # - show_args: показывать аргументы функции (True/False)
    #средняя функция - декоратор
    def decorator(func):
        #счетчик глубины рекурсии
        recursion_depth = 0
        #внутренняя фун-ия - обертка
        def wrapper(*args, **kwargs):
            nonlocal recursion_depth
            recursion_depth += 1
            #создаем отступ для визуализации рекурсии
            indent = " " * (recursion_depth - 1)
            #логирование входа в фун-ию
            if logging_enabled:
                #если логирование включено
                current_time = time.strftime("%H:%M:%S") #включаем время
                #формируем строку с аргументами
                args_str = ""
                if show_args:
                    #проверяем, нужно ли показывать аргументы
                    args_list = []
                    #добавляем все позиционные аргументы (args)
                    for arg in args:
                        args_list.append(str(arg))
                    #добавляем все именованные аргументы (kwargs)
                    for key,value in kwargs.items():
                        args_list.append(f"{key}={value}")
                    #если список не пустой, то соединяем все эелементы через запятую
                    if args_list:
                        args_str = f'({', '.join(args_list)})'
                    else:
                        args_str = '(нет аргументов)'
                #все вместе: отступ + время + вызвана + имя функции + аргументы
                print(f"{indent}[{current_time}] Вызвана {func.__name__} {args_str}")
            #выполнение исходной функции
            #если нужно показывать время, то запоминаем время начала
            if show_time:
                start = time.time()
            else:
                start = None
            #вызываем ориг. фун-ию и именно здесь происходит рекурсивный вызов, если фун-ия рекурсивная
            result = func(*args, **kwargs)
            #если нужно показывать время, то запоминаем время окончания
            if show_time:
                end = time.time()
            else:
                end = None
            #логирование выхода из фун-ии
            if logging_enabled:
                #запоминаем время
                current_time = time.strftime("%H:%M:%S")
                #выводим результат
                if show_time and end is not None and start is not None:
                    #вычисляем время выполнения в миллисекундах
                    elapsed_ms = (end - start) * 1000
                    print(f"{indent}[{current_time}] Вернула: {result} [{elapsed_ms:.2f} мс]")
                else:
                    #eсли время показывать не нужно
                    print(f"{indent}[{current_time}] Вернула: {result}")

                #разделитель печатаем ТОЛЬКО когда вернулись из САМОГО ПЕРВОГО вызова
                #recursion_depth == 1 означает, что мы на самом верхнем уровне (не внутри рекурсии)
                if recursion_depth == 1:
                    print(f"{indent}{'-' * 40}")

            #выход из фун-ии
            #уменьшаем глубину: мы ВЫХОДИМ из функции
            recursion_depth -= 1

            #возвращаем результат исходной функции
            return result

        #обёртка wrapper готова, возвращаем её
        return wrapper

        #декоратор готов, возвращаем его
    return decorator

#ПРИМЕР 1: обычная функция с логированием

@log_c(logging_enabled=True, show_time=True, show_args=True)
def add(a, b):
    "Складывает два числа"
    return a + b

# При вызове add(5, 3):
# 1. Python видит @log_c(...) и вызывает log_c(...)
# 2. log_c возвращает decorator
# 3. decorator(add) возвращает wrapper
# 4. wrapper(5, 3) выполняется, логирует, вызывает настоящую add(5, 3)

print("Пример 1: Сложение")
result = add(5, 3)
print(f"Результат: {result}\n")

#ПРИМЕР 2: рекурсивная фун-ия

@log_c(logging_enabled=True, show_time=True, show_args=True)
def factorial(n):
    "Вычисляет факториал рекурсивно."
    "factorial(5) = 5 * 4 * 3 * 2 * 1 = 120"

    if n <= 1:
        return 1
    #рекурсивный вызов: функция вызывает сама себя
    return n * factorial(n - 1)

print("Пример 2: Рекурсивный факториал")
result = factorial(5)
print(f"Результат: {result}\n")

#ПРИМЕР 3: отключение логирования

@log_c(logging_enabled=False)
def secret_function():
    return "Я секретная!"

print("Пример 3: Логирование выключено")
result = secret_function()
print(f"Функция вернула: {result}\n")

#ПРИМЕР 4: без отображения времени

@log_c(logging_enabled=True, show_time=False, show_args=True)
def multiply(a, b):
    return a * b

print("Пример 4: Без времени (show_time=False)")
multiply(4, 7)
print()

#ПРИМЕР 5: без отображения аргументов

@log_c(logging_enabled=True, show_time=True, show_args=False)
def power(base, exp):
    return base ** exp

print("Пример 5: Без аргументов (show_args=False)")
power(2, 10)



import time
def log_calls(func):
    def wrapper(*args, **kwargs):
        current_time = time.strftime('%H:%M:%S')
        args_list = [str(arg) for arg in args]
        args_list += [f'{k} = {v}' for k,v in kwargs.items()]
        args_str = ', '.join(args_list) if args_list else 'нет аргументов'
        print(f'[{current_time}] Вызвана {func.__name__}({args_str})')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{current_time}] Вернула: {result}")
        print(f"[{current_time}] Время: {(end - start) * 1000:.2f} мс")
        print("-" * 40)
        return result
    return wrapper
@log_calls
def add(a, b):
    return a + b
@log_calls
def greet(name, msg="Привет"):
    return f"{msg}, {name}!"
if __name__ == "__main__":
    print("\n1. Сложение двух чисел:")
    add(10, 20)

    print("\n2. Приветствие (без второго аргумента):")
    greet("Петр")

    print("\n3. Приветствие (с именованным аргументом):")
    greet("Анна", msg="Здравствуй")


from itertools import product
import doctest


def count_codes():
    """"
    Возвращает количество 6-буквенных кодов.

    >>> count_codes()
    23625
    >>> isinstance(count_codes(), int)
    True
    >>> count_codes() > 0
    True
    """"
    letters = ('А', 'Н', 'Д', 'Р', 'Е', 'Й')
    valid_count = 0
    for code in product(letters, repeat=6):
        if code.count('Й') > 1:
            continue
        if 'Й' not in code:
            valid_count += 1
            continue
        y_index = code.index('Й')
        if y_index == 0:
            continue
        if y_index == 5:
            continue
        if y_index > 0 and code[y_index - 1] == 'Е':
            continue
        if y_index < 5 and code[y_index + 1] == 'Е':
            continue
        valid_count += 1
    return valid_count


def count_ones_in_expression():
    """"
    Возвращает количество единиц в двоичной записи.

    >>> count_ones_in_expression()
    5
    >>> isinstance(count_ones_in_expression(), int)
    True
    """"
    value = 8 ^ 2020 + 4 ^ 2017 + 26 - 1
    return bin(value)[2:].count('1')


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_numbers_with_orders(start, end):
    """"
    Возвращает строку с простыми числами и их порядковыми номерами.

    >>> print(get_prime_numbers_with_orders(5, 9))
    1 5
    3 7
    """"
    result_lines = []
    for num in range(start, end + 1):
        if is_prime(num):
            order = num - start + 1  #порядковый номер в последовательности
            result_lines.append(f"{order} {num}")
    return "\n".join(result_lines)


if __name__ == "__main__":
    print("Запуск doctest'ов...")
    doctest.testmod(verbose=True)
    print("\n--- Результаты выполнения задач ---")
    print(f"1. Количество кодов: {count_codes()}")
    print(f"2. Количество единиц в двоичной записи: {count_ones_in_expression()}")
    print("3. Простые числа на отрезке [245690; 245756]:")
    print(get_prime_numbers_with_orders(245690, 245756))
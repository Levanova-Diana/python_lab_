def is_prime(n):
    # Проверка, является ли число простым
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
# Возвращает строку с простыми числами и их порядковыми номерами
    result_lines = []

    for num in range(start, end + 1):
        if is_prime(num):
            order = num - start + 1
            result_lines.append(f"{order} {num}")

    return "\n".join(result_lines)

result = get_prime_numbers_with_orders(245690, 245756)
print(result)
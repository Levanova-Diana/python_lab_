import argparse
import sys
def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    is_prime = [True] * (limit+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p*p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes
def generate_primes(start, end):
    if start < 2:
        start = 2
    if end < start:
        return []
    primes_up_to_end = sieve_of_eratosthenes(end)
    result = [p for p in primes_up_to_end if p >= start]
    return result
def main():
    parser = argparse.ArgumentParser(description='Генератор простых чисел')
    parser.add_argument('end', type= int, help = 'Вверхняя граница диапазона')
    parser.add_argument('start', nargs = '?', type = int, default = 2, help = 'Нижняя граница диапазона (по умолчанию 2)')
    args = parser.parse_args()
    start = args.start
    end = args.end

    if start > end:
        print(f'Ошибка: Нижняя граница ({start}) не может быть больше верхней ({end}).')
        sys.exit(1)
    primes = gererate_primes(start, end)
    if not primes:
        print(f'Простых чисел в диапазоне [{start}, {end}] не найдено.')
    else:
        print(f'Простые числа в диапазоне [{start}, {end}]:')
        print(primes)
        print(f'Всего найдено: {len(primes)}')
if __name__ == '__main__':
    main()
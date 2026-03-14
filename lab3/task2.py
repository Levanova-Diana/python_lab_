def count():
    value = 8**2020 + 4**2017 + 26 - 1
    binary = bin(value)[2:]
    ones_count = binary.count('1')
    return ones_count
result = count()
print(result)
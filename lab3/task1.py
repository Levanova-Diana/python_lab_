from itertools import product
def count_codes():
    letters = ('А', 'Н', 'Д', 'Р', 'Е','Й')
    valid_count = 0
    for code in product(letters, repeat =  6):
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
result = count_codes()
print(result)
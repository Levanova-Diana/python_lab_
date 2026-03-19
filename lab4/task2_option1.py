def sequence_recursive(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    w_prev1 = sequence_recursive(i-1)
    w_prev2 = sequence_recursive(i-2)
    multiplier = ((i - 1)**2) / ((i + 1)**3)
    resilt = w_prev1 * w_prev2 * multiplier
    return resilt
print(sequence_recursive(1))
print(sequence_recursive(2))
print(sequence_recursive(3))
print(sequence_recursive(4))
print(sequence_recursive(5))
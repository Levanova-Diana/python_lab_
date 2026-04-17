def sequence_iterative(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    w_prev2 = 0.3
    w_prev1 = -1.5
    w_current = 0
    for n in range(3, i + 1):
        multiplier = ((n - 1)**2) / ((n + 1)**3)
        w_current = w_prev1 * w_prev2 * multiplier
        w_prev2 = w_prev1
        w_prev1 = w_current
    return w_current
print(sequence_iterative(1))
print(sequence_iterative(2))
print(sequence_iterative(3))
print(sequence_iterative(5))
print(sequence_iterative(10))
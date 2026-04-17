def unpuck_interative(data):
    result = []
    stack = [data]
    while stack:
        current = stack.pop()
        if isinstance(current, (list, tuple, set)):
            for item in reversed(list(current)):
                stack.append(item)
        elif isinstance(current, dict):
            for value in reversed(list(current.values())):
                stack.append(value)
            for key in reversed(list(current.keys())):
                stack.append(key)
        else:
            result.append(current)
    return list(result)
data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print(unpuck_interative(data))
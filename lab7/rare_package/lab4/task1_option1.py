def unpack_recursive(data):
    result = []
    for item in data:
        if isinstance(item,(list,tuple,set)):
            result.extend(unpack_recursive(item))
        elif isinstance(item,dict):
            result.extend(unpack_recursive(item.keys()))
            result.extend(unpack_recursive(item.values()))
        else:
            result.append(item)
    return result
data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print(unpack_recursive(data))

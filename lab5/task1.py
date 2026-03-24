file = open("test.txt", "w", encoding='utf-8')
file.write("Строка 1\n")
file.write("Строка 2\n")
file.write("Строка 3\n")
file.write("Строка 4\n")
file.close()
def get_file_reader(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    current = 0
    def read_next():
        nonlocal current
        if current < len(lines):
            line = lines[current]
            current += 1
            return line
        else:
            return None

    return read_next
reader = get_file_reader("test.txt")
print(reader()) # Строка 1
print(reader()) # Строка 2
print(reader()) # Строка 3
print(reader()) # Строка 4
print(reader()) # None


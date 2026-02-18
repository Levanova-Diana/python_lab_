zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1
print(f'Лев сидит в клетке - {lion_index}')
print(f'Жаворонок сидит в клетке - {lark_index}')



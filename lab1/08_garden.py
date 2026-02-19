garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

all_flowers = garden_set | meadow_set #объединение
print('Все виды цветов:', all_flowers)

everywhere = garden_set & meadow_set #пересечение
print('Цветы, которые растут и в саду, и на лугу:', everywhere)

only_garden = garden_set - meadow_set
print('Цветы, которые растут в саду, но не растут на лугу', only_garden)

only_meadow = meadow_set - garden_set
print('Цветы, которые растут на лугу, но не растут в саду', only_meadow)







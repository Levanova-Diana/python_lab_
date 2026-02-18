# Отчет
# Задание 1
## Описание задачи
### -Дан словарь sites с списком городов
### -Надо составить словарь словарей расстояний между ними
### -расстояние на координатной сетке вычисляется по формуле:
$((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 $ 

## Решение
````python
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
moscow_london = round(((sites['Moscow'][0] - sites['London'][0])**2 + (sites['Moscow'][1] - sites['London'][1])**2) ** 0.5,2)
moscow_paris = round(((sites['Moscow'][0] - sites['Paris'][0])**2 + (sites['Moscow'][1] - sites['Paris'][1])**2) ** 0.5,2)

london_moscow = round(((sites['London'][0] - sites['Moscow'][0])**2 + (sites['London'][1] - sites['Moscow'][1])**2) ** 0.5,2)
london_paris = round(((sites['London'][0] - sites['Paris'][0])**2 + (sites['London'][1] - sites['Paris'][1])**2) ** 0.5,2)

paris_moscow = round(((sites['Paris'][0] - sites['Moscow'][0])**2 + (sites['Paris'][1] - sites['Moscow'][1])**2) ** 0.5,2)
paris_london = round(((sites['Paris'][0] - sites['London'][0])**2 + (sites['Paris'][1] - sites['London'][1])**2) ** 0.5,2)

distances['Moscow'] = {
    'London' : moscow_london,
    'Paris'  : moscow_paris,
}
distances['London'] = {
    'Moscow' : london_moscow,
    'Paris'  : london_paris,
}
distances['Paris'] = {
    'Moscow' : paris_moscow,
    'London'  : paris_london,
}
print(distances)
````
# Скриншот работы программы:
![img.png](img.png)

# Задание 2
## Описание задачи
### -Есть значение радиуса круга
$ radius = 42 $
### -Надо вывести на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
#### Формула вычисления площади:
$ S= π ∗ R^2 $
### Даны координаты двух точек:
```` python
point_1 = (23, 34)
point_2 = (30, 30)
````
### Для каждой точки определить, лежит ли она внутри круга, и вывести на консоль True или False. Расстояние от точки до центра круга вычисляется по формуле:
$ d=√(x²+ y²) $
### Точка лежит внутри круга, если d ≤ R.

## Решение:
```` python
radius = 42
pi = 3.1415926
square = pi * radius * radius
print(round(square,4))

point_1 = (23, 34)
distance1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(distance1 <= radius)

point_2 = (30, 30)
distance2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(distance2 <= radius)
````
## Скриншот работы программы:
![img_1.png](img_1.png)

# Задание 3
## Описание задачи:
### Расставить знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25".
## Условия:
### -Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
### -Порядок чисел нужно сохранить.

## Решение:
```` python
result = 1 * (2 + 3) * 4 + 5
print(result)
````
## Скриншот работы программы:
![img_2.png](img_2.png)

# Задание 4
## Описание задачи:
### Есть строка с перечислением фильмов
```` python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
````
### Вывести на консоль с помощью индексации строки, последовательно:
#####   1.первый фильм
#####   2.последний
#####   3.второй
#####   4.второй с конца
## Условия:
### -Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
### -Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами, как указано в задании!

## Решение:
```` python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(my_favorite_movies[:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])
````
## Скриншот работы программы:
![img_3.png](img_3.png)

# Задание 5
## Описание задачи:
### Создать списки:
#### 1.моя семья (минимум 3 элемента)
```` python
my_family = []
````
#### 2.список списков приблизителного роста членов вашей семьи
```` python
my_family_height = [
    # ['имя', рост],
    [],
]
````
### Вывести на консоль рост отца в формате:
####   Рост отца - ХХ см
### Вывести на консоль общий рост вашей семьи как сумму ростов всех членов:
####   Общий рост моей семьи - ХХ см

## Решение:
````python
my_family = ['Венера', 'Александр', 'Диана', 'Милана', 'Галина']
my_family_height = [
    ['Венера', 163],
    ['Александр', 170],
    ['Диана', 165],
    ['Милана',145],
    ['Галина', 164]
]
print(f'Рост отца - {my_family_height[1][1]} см')
total_height = 0
for people in my_family_height:
    total_height += people[1]
print(f'Общий рост моей семьи - {total_height} см')
````
## Скриншот работы программы:
![img_4.png](img_4.png)

# Задание 6
## Описание задачи:
#### Есть список животных в зоопарке
```` python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
````
#### Посадить медведя (bear) между львом и кенгуру и вывести список на консоль
#### Добавить птиц из списка birds в последние клетки зоопарка и вывести сипсок на консоль
```` python
birds = ['rooster', 'ostrich', 'lark', ]
````
#### Убрать слона и выведите список на консоль
#### Вывести на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
#### Номера при выводе должны быть понятны простому человеку, не программисту.

## Решение задачи:
```` python
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
````

## Скришот работы программы:
![img_5.png](img_5.png)

# Задание 8
## Описание задачи:
### Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
### -Точность указывается в функции round(a, b), где a, это число которое надо округлить, а b количество знаков после запятой
```` python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
````
### Распечатать общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате:
####   Три песни звучат ХХХ.XX минут
### Обратить внимание, что делать много вычислений внутри print() - плохой стиль.Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

### Есть словарь песен группы Depeche Mode
```` python
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
````
### Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'.
### А другие три песни звучат ХХХ минут

## Решение:
```` python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
halo_time = violator_songs_list[3][1]
enjoy_time = violator_songs_list[5][1]
clean_time = violator_songs_list[8][1]

total_time = halo_time + enjoy_time + clean_time

total_time_rounded = round(total_time, 2)
print(f'Три песни звучат {total_time_rounded} минут')


violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
sweetest_time = violator_songs_dict['Sweetest Perfection']
policy_time = violator_songs_dict['Policy of Truth']
blue_time = violator_songs_dict['Blue Dress']

total_time = sweetest_time + policy_time + blue_time
total_time_rounded = round(total_time, 2)
print(f'А другие три песни звучат - {total_time_rounded} минут')
````
## Скришот работы программы:
![img_6.png](img_6.png)

# Задание 9
## Описание задачи:
### Есть зашифрованное сообщение:
```` python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
````
### Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
### Должна получиться фраза на русском языке, например: как два байта переслать.
## Ключ к расшифровке:
###   первое слово - 4-я буква
###   второе слово - буквы с 10 по 13, включительно
###   третье слово - буквы с 6 по 15, включительно, через одну
###   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
###   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
## Обратить внимание:
###   даны номера букв, а не индексы
###   срез не включает последний индекс
## Подсказки:
###   В каждом элементе списка защифровано одно слово.
###   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
###   4е и 5е слова нужно получить за 1 срез

## Решение:
```` python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
word1 = secret_message[0][3]
word2 = secret_message[1][9:13]
word3 = secret_message[2][5:15:2]
word4 = secret_message[3][12:6:-1]
word5 = secret_message[4][20:15:-1]
decoded_message = f"{word1} {word2} {word3} {word4} {word5}"

print(decoded_message)
````
## Скриншот работы программы:
![img_7.png](img_7.png)
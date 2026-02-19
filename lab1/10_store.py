goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


table_code = goods['Стол']
table_quantity_1 = store[table_code][0]['quantity']
table_price_1 = store[table_code][0]['price']
table_cost_1 = table_quantity_1 * table_price_1

table_quantity_2 = store[table_code][1]['quantity']
table_price_2 = store[table_code][1]['price']
table_cost_2 = table_quantity_2 * table_price_2

table_quantity_total = table_quantity_1 + table_quantity_2
table_cost_total = table_cost_1 + table_cost_2
print(f'Стол - {table_quantity_total} шт, стоимость {table_cost_total} руб')


divan_code = goods['Диван']
divan_quantity_1 = store[divan_code][0]['quantity']
divan_price_1 = store[divan_code][0]['price']
divan_cost_1 = divan_quantity_1 * divan_price_1

divan_quantity_2 = store[divan_code][1]['quantity']
divan_price_2 = store[divan_code][1]['price']
divan_cost_2 = divan_quantity_2 * divan_price_2

divan_quantity_total = divan_quantity_1 + divan_quantity_2
divan_cost_total = divan_cost_1 + divan_cost_2
print(f'Диван - {divan_quantity_total} шт, стоимость {divan_cost_total} руб')


chair_code = goods['Стул']
chair_quantity_1 = store[chair_code][0]['quantity']
chair_price_1 = store[chair_code][0]['price']
chair_cost_1 = chair_quantity_1 * chair_price_1

chair_quantity_2 = store[chair_code][1]['quantity']
chair_price_2 = store[chair_code][1]['price']
chair_cost_2 = chair_quantity_2 * chair_price_2

chair_quantity_3 = store[chair_code][2]['quantity']
chair_price_3 = store[chair_code][2]['price']
chair_cost_3 = chair_quantity_3 * chair_price_3

chair_quantity_total = chair_quantity_1 + chair_quantity_2 + chair_quantity_3
chair_cost_total = chair_cost_1 + chair_cost_2 + chair_cost_3
print(f'Стул - {chair_quantity_total} шт, стоимость {chair_cost_total} руб')

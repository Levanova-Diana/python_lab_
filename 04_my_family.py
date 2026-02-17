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

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
moscow_london = round(((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5,2)
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





trajecten = {'bruin', 'groen'}
traject_bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
traject_groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
print(traject_groen & traject_bruin)
print(traject_bruin ^ traject_groen)
print(traject_bruin | traject_groen)
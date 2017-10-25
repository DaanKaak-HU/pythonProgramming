def split(invoer):
    alles = invoer.split('-')

    nieuw_alles = []
    for num in alles:
        nieuw_alles.append(int(num))
    print('list van ints: ' + str(nieuw_alles))

    grootste_getal = max(alles)
    print('grootste waarde: ' + grootste_getal)

    kleinste_getal = min(alles)
    print('kleinste waarde: ' + kleinste_getal)

    aantal = str(len(alles))
    print('aantal: ' + aantal)

    som = str(sum(nieuw_alles))
    print('totaal: ' + som)

    berekening = int(som) / int(aantal)
    gemiddelde = ('gemiddelde: ' + str(berekening))

    return gemiddelde


print(split("5-9-7-1-7-8-3-2-4-8-7-9"))
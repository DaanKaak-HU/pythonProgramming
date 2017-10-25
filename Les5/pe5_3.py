def test(bestandnaam):
    file = open(bestandnaam)
    infile = file.readlines()
    file.close()
    return infile

Kaartnummers = test('Kaartnummers.txt')

print('Deze file heeft ' + str(len(Kaartnummers)) + ' regels')

hoogstenummer = 0
for huidigeregel in Kaartnummers:
    woorden = huidigeregel.split(', ')
    if int(woorden[0]) > hoogstenummer:
        hoogstenummer = int(woorden[0])

print('Het grootste Kaartnummer is: ', hoogstenummer)

print('eerste', 'tweede', sep='-', end=' ')
print('volgende')


dag = 19
maand = 9
jaar = 2017
#datum = str(dag) + '-' + str(maand) + '-' + str(jaar)

datum = 'Vandaag is het {2}-{1}-{0}'.format(dag, maand, jaar)
print(datum)

#for i in range(5):
    #print('{:2}{:4} {:6.2f}').format(i, i**i, i/3))

namen = ['Jan Janssen', 'Pieter Riksen', 'Pim vanachteren']
for name in namen:
    parts = name.split()
    print('{:10} {:12}'.format(parts)[0], parts[1])
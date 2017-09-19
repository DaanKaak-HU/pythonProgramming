print('eerste', 'tweede', sep='-', end=' ')
print('volgende')


dag = 19
maand = 9
jaar = 2017
#datum = str(dag) + '-' + str(maand) + '-' + str(jaar)

datum = 'Vandaag is het {2}-{1}-{0}'.format(dag, maand, jaar)
print(datum)
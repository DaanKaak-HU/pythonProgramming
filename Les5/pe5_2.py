outfile = open('Kaartnummers.txt', 'w')
outfile.write('325255, Jan Jansen''\n'
              '334343, Erik Materus''\n'
              '235434, Ali Ahson''\n'
              '645345, Eva Versteeg''\n'
              '534545, Jan de Wilde''\n'
              '345355, Henk de Vries')
outfile.close()

def Kaartnummers():
    infile = open('Kaartnummers.txt', 'r')
    content = infile.read()
    splits = content.splitlines()

    for i in splits:
        text = i.split(',')
        print(text[1], 'heeft het kaartnummer: ',text[0])


Kaartnummers()
import datetime
vandaag = datetime.datetime.today()

while True:
    naam = input('Wat is de naam van de hardloper:')
    s = vandaag.strftime("%a %d %b %Y %H" + ":" "%M" + ":" "%S")
    naamEnTijd = ('{}, {}'.format(s, naam))
    infile = open('hardlopers.txt', 'a')
    infile.writelines(naamEnTijd + "\n")


leeftijd = int(input('Geef je leeftijd:'))
paspoort = input('Heb je een paspoort:')

if 18 <= leeftijd and paspoort == 'ja':
        print('Gefeliciteerd, je mag stemmen!')
else:
    print('Jammer, je mang nog niet stemmen')

#if 18 > leeftijd or paspoort == 'nee':
 #   print('Jammer, je mag nog niet stemmen')
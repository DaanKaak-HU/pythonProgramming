def convert(celcius):
    Fahrenheit = celcius * 1.8 + 32
    print(Fahrenheit)

def table():
    print('{0:1},{1:5}'.format('  F', '      C', ))
    for i in range(-30, 40):
        if i %10 == 0:
            print('{0:5}{1:7}'.format(i*1.8+32.0, i+0.0))

table()

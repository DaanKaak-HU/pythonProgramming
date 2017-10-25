import random
def monopolyworp():
    worp1 = random.randrange(1,7)
    worp2 = random.randrange(1,7)
    worp3 = random.randrange(1,7)
    worp4 = random.randrange(1,7)
    worp5 = random.randrange(1,7)
    worp6 = random.randrange(1,7)
    if worp1 == worp2 and worp3 == worp4:
        print(str(worp1) + str(' +'), str(worp2), str(' ='), str(worp1 + worp2), str(' (dubbel)'))
        print(str(worp3) + str(' +'), str(worp4), str(' ='), str(worp3 + worp4), str(' (dubbel)'))
        print(str(worp5) + str(' +'), str(worp6), str(' ='), str(worp5 + worp6), str('direct naar gevangenis'))
    elif worp1 == worp2:
        print(str(worp1) + str(' +'), str(worp2), str(' ='), str(worp1 + worp2), str(' (dubbel)'))
        print(str(worp3) + str(' +'), str(worp4), str(' ='), str(worp3 + worp4))
    else:
        print(str(worp1) + str(' +'), str(worp2), str(' ='), str(worp1 + worp2))


monopolyworp()
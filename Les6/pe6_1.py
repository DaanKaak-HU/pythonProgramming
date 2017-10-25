def seizoen(maand) ->int:
    if maand >= 3 and maand < 6:
        print('lente')
    elif maand >= 6 and maand < 9:
        print('zomer')
    elif maand >= 9 and maand < 12:
        print('herfst')
    else:
        print('winter')
seizoen(9)
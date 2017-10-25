def standaardprijs(afstandKM):
    if afstandKM > 0:
        if afstandKM > 50:
            return 15 + afstandKM * 0.6
        else:
            return afstandKM * 0.8
    else:
        return 0

def ritprijs(leeftijd, weekendrit, afstandKM):
    price = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65 :
        if weekendrit == 'ja':
            return price * 0.65
        else:
            return price * 0.7
    else:
        if weekendrit == 'ja':
            return price * 0.6
        else:
            return price

ages = [11, 12, 64, 65]
switch = ["ja", "nee"]
distance = [-20, 25, 50, 75]

for age in ages:
    for afstandKM in distance:
        for weekendrit in switch:
            print("Age: " + str(age) + " Weekend: " + str(weekendrit) + " Distance: " + str(afstandKM) + " Price: " + str(ritprijs(age, weekendrit, afstandKM)))
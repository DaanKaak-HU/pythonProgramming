s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ['a', 'i', 'u', 'o', 'e',]
for letter in s:
    if letter in klinker:
        print(letter)
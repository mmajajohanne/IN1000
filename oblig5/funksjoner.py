""" OPPGAVE 1: Parametre og returverdier """


# 1.1
def adder(tall1, tall2):
    return tall1 + tall2


tall1 = adder(2, 3)
tall2 = adder(5, 3)

print("2 + 3 =", tall1)
print("5+3=10:", tall2)


# 1.2,1.3
streng = input("Skriv inn en tekststreng: ")
valgt_bokstav = input("Skriv inn en bokstav: ")


def tellForekomst(minTekst, minBokstav):
    antall = 0
    for bokstav in minTekst:
        if bokstav == minBokstav:
            antall += 1
    return antall


print(tellForekomst(streng, valgt_bokstav))

""" OPPGAVE 3: Regnefunksjoner """


# 3.1
def addisjon(a, b):
    return a + b


sum = addisjon(3, 2)
print(sum)


# 3.2
def subtraksjon(a, b):
    return a - b


assert subtraksjon(15, 5) == 10
assert subtraksjon(3, -1) == 4
assert subtraksjon(-7, -2) == -5


def divisjon(a, b):
    return a / b


assert divisjon(10, 2) == 5.0
assert divisjon(-3, 2) == -1.5
assert divisjon(-4, -2) == 2


# 3.3
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54


print(tommerTilCm(1))  # printer 2.54


# 3.4
def skrivBeregninger():
    tall1 = float(input("skriv inn første tall:"))
    tall2 = float(input("skriv inn andre tall:"))

    # bruker funskjonene
    print("addisjon:", addisjon(tall1, tall2))
    print("subtraksjon", subtraksjon(tall1, tall2))
    print("divisjon", divisjon(tall1, tall2))

    antalltommer = float(input("skriv inn tallet du ønsker å konvertere:"))
    print(antalltommer, "tommer er lik", tommerTilCm(antalltommer), "cm")


# 3.5
skrivBeregninger()

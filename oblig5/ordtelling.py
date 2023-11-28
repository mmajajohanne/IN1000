""" OPPGAVE 2: Å telle bokstaver og ord """


# 2.1
# funksjon som teller antall bokstaver i tekst-strengen
# kunne brukt len(minTekst), men valgte å gjøre det mer manuelt
def antallBokstaver(minTekst):
    antall = 0
    for bokstav in minTekst:
        if bokstav.isalpha():  # isalpha returnerer True dersom alle bokstavene er
            antall += 1
    return antall


# 2.2
def unikeOrd(setning):
    ordbok = {}
    for ord in setning.split():
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1
    return ordbok


# 2.3
setning = input("Skriv inn en setning: ")

# bruker funksjonen unikeOrd og lager en ordbok med de unike ordene i setnignen + antall
ordbok = unikeOrd(setning)
# lager en liste med nøkkelverdiene i ordboka, altså en liste med de unike ordene
keys = list(ordbok.keys())

# skriver ut antallet ord i setningen. bruker split() til å lage en liste av alle ordene, og printer lengden av denne lista
print("Det er", len(setning.split()), "ord i setningen!")

# itererer gjennom hvert element i ordboken og printer ordet og antallet ganger det fremkommer
# bruker også funksjonen antallBokstaver for å telle og printe antall bokstaver i det gjeldende ordet
for i in range(0, len(ordbok)):
    print(
        "Ordet ",
        str(keys[i]),
        " fremkommer",
        ordbok[keys[i]],
        "ganger, og har ",
        antallBokstaver(keys[i]),
        "bokstaver.",
    )

# OPPGAVE 2: Reiseplan

# 2.1, 2.2
# oppretter tre tomme lister
steder = []
klesplagg = []
avreisedatoer = []

# lar brukeren legge til 5 elementer i hver av listene
for i in range(5):
    steder.append(input("skriv inn et reisemål:"))
    klesplagg.append(input("skriv inn klesplagg:"))
    avreisedatoer.append(input("skriv inn avreisedato:"))

# 2.3
reiseplan = [
    steder,
    klesplagg,
    avreisedatoer,
]  # oppretter en liste med de tre listene fra oppgave 2.1 og 2.2
print(reiseplan)

# 2.4
# itererer gjennom og skriver ut alle elementene i reiseplan
for i in reiseplan:
    print(i)

# 2.5
# lar brukeren skrive inn en index for den nøstede listen, og så en index for listen i det valgte elementet
liste_indeks1 = int(input("skriv inn en index (heltall mellom 0 og 2"))
liste_indeks2 = int(input("skriv inn en index (heltall mellom 0 og 4"))

# sjekker om indeksene er gyldige
if 0 <= liste_indeks1 < 3 and 0 <= liste_indeks2 < 5:
    print(
        reiseplan[liste_indeks1][liste_indeks2]
    )  # hvis gyldig: skriver ut elementet på den valgte indeksen
else:
    print("ugyldig input!")

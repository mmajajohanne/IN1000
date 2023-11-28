""" OPPGAVE 2: Ordbok """

#2.1
#lager en ordbok med varene og de tilhørende prisene
ordbok = {"melk": 14.90, "brød": 24.90, "yoghurt":12.90, "pizza":39.90}
#skriver ut ordboken til terminalen
print(ordbok)

#2.2
#leser inn to varenavn og priser fra brukenavn og legger dem inn i ordboken
for i in range(2):
    vare = str(input("skriv inn varenavn:"))
    ordbok[vare]=float(input("skriv inn prisen (. istedenfor ,):"))
#skriver ut ordboken til terminalen
print(ordbok)

# OPPGAVE 3: Løkker og lister
"""Skriv et program som ved hjelp av en for-løkke lager en liste som inneholder tallene fra 0
til 9."""

#3.1
liste = [] #oppretter tom liste
i = 0
while i < 10: #while løkka kjører så lenge i er mindre enn 10
    liste.append(i) #legger til i i liste
    i += 1 #øker i med 1 for hver runde
print(liste)

#3.2
liste2 = [] #oppretter tom liste
for r in range(10): #for løkken kjører gjennom listen av tall mellom 0 og 9, laget av range() funksjonen
    liste2.append(r) #legger til i i liste2
print(liste2)

#3.3
""" a. Hvor i koden din i oppgave 3.2 er det at du i tilfelle har en samling?
 "
a. I oppgave 3.2 har vi samlingen range(10) som er en innebygd prosedyre i python som returnerer en liste med tall fra 0 til 9.
Denne listen er hva vi itererer over ved hjelp av for-løkken.

b. Og hvilke elementer (tall) inneholder denne samlingen som du bruker i din
for-løkke sammenlignet med samlingen (listen) som du lager? 

b. Samlingen som lages i for-løkken inneholder alle tallene fra 0 til 9, akkurat som list(range(10)) ville gitt. Både samlingen som lages med range() og listen som 
får elementer inni for-løkken inneholder de 
samme tallene. Forskjellen er bare hvordan de blir laget: den ene ved hjelp av en innebygd funksjon (range) og den andre ved å bruke en for-løkke til å gradvis legge til elementer 
i en eksisterende liste.

"""

#3.4
mine_tall = []  # oppretter en tom liste mine_tall
tall = 0  # variabel med starttallet

while tall < 20:  # while løkken kjører så lenge tallet er under 20
    mine_tall.append(tall)  # legger til tallet i listen
    tall += 3  # øker tallet med 3 

print(mine_tall)


#3.5
for e in mine_tall:
    print (e)

#3.6
for i in range(len(mine_tall)):
    print(i)

#3.7, 3.8
for i in range(len(mine_tall)):
    mine_tall[i] = mine_tall[i] * 10 #endrer elementet på indeksen i til originalverdien * 10
print(mine_tall)

#3.9
"""
Måtte du i oppgave 3.7 la for-løkken gå gjennom (iterere over) selve tallene i listen
mine_tall eller gå gjennom (iterere over) de gyldige indeksene for listen mine_tall?
Forklart kort hvorfor/hvorfor ikke, og inkluder følgende punkter i forklaringen:
a. Hvorfor fungerer det bare på én av måtene?
b. Hva ser man i oppgave 3.8 dersom man i oppgave 3.7 valgte feil strategi for hva
for-løkken gikk gjennom (itererte over)?

Det er riktig å la for-løkken gå gjennom de faktiske tallene i listen, og ikke bare de gyldige indeksene.
Dette er fordi oppgaven er å endre hvert tall i listen ved å multiplisere det med 10. 
Hvis man itererer over indeksene, vil man bare få tilgang til indeksene og ikke selve verdiene til elementene i lista. 
Å endre tallene ved å bruke indeksene ville kreve ekstra trinn for å hente hvert tall ved hjelp av indeksen 
før man kan utføre multiplikasjonen.

Dersom man hadde valgt feil strategi ved å la for-løkken iterere over indeksene i stedet for tallene, ville resultatet i oppgaven være at 
ingen av elementene i den originale listen mine_tall blir endret.
Dette er fordi man bare endrer en midlertidig kopi av tallene og ikke de faktiske tallene i listen. Derfor ville den opprinnelige listen inneholde 
de samme verdiene som før, mens den midlertidige varibelen eller en eventuell ny liste, ville inneholde de endrede verdiene."""
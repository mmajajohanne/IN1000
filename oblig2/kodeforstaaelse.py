""" OPPGAVE 4: Kodeforståelse og feilsøking"""
#1. Vil programmet kjøre? begrunn svaret
#   Hvorvidt programmet vil kjøre avhenger av hva brukeren taster inn i terminalen. 
#   Skriver brukren for eksempel inn et tall over 10, vil programmet kjøre uten problemer, mens hvis brukeren skriver et tall under 10, vil det oppstå feil.
#   Dette er fordi programmet har en feil i linjen inni if-setningen, og dersom brukerinputen oppfyller kriteriene til if-setningen og denne linjen kjøres, vil programmet krasje.

#2. 
#   Et problem i koden som kan føre til feil er linjen print(b + "Hei!"), inni if-setningen. 
#   Dette er en typefeil, der man prøver å legge sammen en variabel av typen heltall (int) med en streng "Hei".
#   Dette er ikke tillatt i python, da et plusstegn med heltall vil føre til addisjon, mens et plusstegn med strenger vil føre til konkatenering.
#   Man kan derfor ikke utføre en slik operasjon mellom en streng og et heltall uten å først konvertere dem til samme datatype. Programmet vil dermed krasje om denne linjen kjøres.
#   For å løse denne feilen kan man endre den aktuelle linjen slik: print(str(b) + "Hei!"). Da vil heltallet b konverteres til en streng før det konkateneres med den andre strengen "Hei!". 

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
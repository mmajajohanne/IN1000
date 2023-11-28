""" OPPGAVE 5: Temperatur """

"""Lag en funksjon som tar inn en filnavn (string). 
Funksjonen skal gå gjennom linjene i filen og dele dem i kolonner og lage en ordbok 
der nøkkelen representerer månedene (første kolonne) og verdiene er temperaturene (andre kolonne) på typen float. 
Til slutt skal ordboken returneres. Kall funksjonen med filen “max_temperatures_per_month.csv" som et argument (parameter). 
Skriv ut ordboken som funksjonen returnerer."""

fil1 = "max_temperatures_per_month.csv"
fil2 = "max_temperatures_2018.csv"


# 5.1
def fil_til_ordbok(string):
    minfil = open(string)
    ordbok = {}
    for linje in minfil:
        biter = linje.split()
        måned = biter[0]
        temperatur = biter[1]
        ordbok[måned] = temperatur
    return ordbok


print(fil_til_ordbok(fil1))

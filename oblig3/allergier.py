""" OPPGAVE 5: Allergi Oversikt Program """

"""
Lag et Python-program som kan håndtere allergiinformasjon for deltakere som melder seg på et arrangement. 
Programmet skal kunne hjelpe arrangørene med å få en oversikt over hvilken mat som bør unngås for ulike deltakere med forskjellige allergier. 
"""
# oppretter en tom liste for deltakere
deltakere = []

# prosedyre for å legge til deltakere med allergier
def legg_til_deltaker(navn, allergier):
    deltaker = {"navn": navn, "allergier": allergier}   # oppretter en ordbok for deltakeren
    deltakere.append(deltaker)                          # legger til ordboken for deltakeren i listen

# prosedyre for å sjekke hvilke deltakere som har allergi mot en matrett
def sjekk_allergier(matrett):
    deltakere_med_allergi = []      # lager en liste for deltakere som har allergi mot matretten
    for deltaker in deltakere:      # går gjennom hver deltaker i listen over deltakere                   
        if matrett in deltaker["allergier"]:          # sjekker om matretten er i listen over allergier for deltakeren
            deltakere_med_allergi.append(deltaker)    # legger til deltakeren i listen over deltakere med allergi mot matretten

    if len(deltakere_med_allergi) > 0:                  # sjekker om det er noen deltakere med allergi mot matretten
        print(f"Deltakere som bør unngå {matrett}:")    
        for deltaker in deltakere_med_allergi:          # går gjennom og skriver ut navnene til de eventuelle allergiske deltakerne
            print(deltaker["navn"])                    
    else:
        print(f"Ingen deltakere har allergi mot {matrett}.")

#TESTING
# legger til deltakere med allergier
legg_til_deltaker("Alice", ["nøtter", "melk"])
legg_til_deltaker("Bob", ["gluten"])
legg_til_deltaker("Charlie", ["fisk", "gluten"])
legg_til_deltaker("David", ["egg"])
legg_til_deltaker("Eve", ["gluten", "soya"])

# sjekker allergier for en matrett
#sjekk_allergier("melk")
sjekk_allergier("gluten")
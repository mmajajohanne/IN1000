""" OPPGAVE 4: Matplan """

#4.1
# lager en ordbok med nøkkelverdier og innholdsverdier
matplan = {
    'Kari Nordmann': ['brød', 'egg', 'pølser'],
    'Ola Nordmann': ['havregryn', 'salat', 'kylling'],
    'Per Hansen': ['pannekaker', 'sandwich', 'fisk'],
}

#4.2
# lager en prosedyre som skriver ut alle beboerne og lar brukeren velge hvem hen vil se matplanen til
def vis_matplan():
    print("Beboere:")
    #går gjennom hver nøkkelverdi i ordboken og skriver ut navnet
    for beboer in matplan.keys():
        print(beboer)
    
    # lar brukeren velge en beboer
    valgt_beboer = input("Skriv navnet til en beboer: ")
    
    # sjekker om beboeren er registrert i ordboken og skriver ut matplanen om den er det
    if valgt_beboer in matplan:
        print(f"Matplan for {valgt_beboer}:")
        print(f"Frokost: {matplan[valgt_beboer][0]}")
        print(f"Lunsj: {matplan[valgt_beboer][1]}")
        print(f"Middag: {matplan[valgt_beboer][2]}")
    else:
        print("Beboeren er ikke registrert.")

# kaller prosedyren
vis_matplan()

#4.3
"""
I alle tilfellene vil den best egnede datatypen avhenge aller mest av selve operasjonene man ønsker å utføre på dataene. For eksempel hvis man 
ønsker å sortere en samling, vil en liste være bedre egnet enn en mengde, da en mengde ikke har noen spesifikk rekkefølge.

a. Brukernavn på alle IN1000 studentene
Dersom rekkefølgen på brukernavnene ikke spiller noen rolle, og man ikke ønsker noen duplikater, vil mengder egne seg godt for dette.
Mengder i Python er nemlig nyttige for å fjerne duplikater eller for å raskt sjekke om en verdi er i en samling, noe som kan være nyttig dersom
man trenger å finne ut om et spesifikt brukernavn tilhører samlingen.
Lister vil også fungere godt i denne sammenhengen, men da vil man ikke kunne få sortert ut eventuelle duplikater på samme måte som med mengder.

b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
Her vil en ordbok (dictionary) være en god løsning, der nøkkelverdien er brukernavnet og innholdsverdien er antall poeng. Med en ordbok vil man
enkelt kunne slå opp antall poeng en gitt student har fått. 

c. Alle vinnere i Lotto siste år (kun navn)
Her vil også en liste eller mengde være egnet, avhengig av om man er interessert i hvorvidt en person har vunnet flere ganger i løpet av året. 
Dersom man er det, vil en liste være beste løsning, da den vil ta med eventuelle repetisjoner av navn blant vinnerne. En mengde vil på sin side     
kun inneholde unike navn, og vil dermed ikke kunne fortelle oss om en person har vunnet flere ganger. I tillegg vil rekkefølgen i en mengde være 
tilfeldig, mens en liste vil beholde rekkefølgen vinnerne ble lagt til i. Derfor vil en liste egne seg best om man er interessert i å vite hvem
som vant først, sist, osv.

d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen)
Her vil en mengde egne seg godt. Da kan man ungå duplikater i samlingen, og raskt kunne sjekke om en matrett er trygg for gjestene. 
"""

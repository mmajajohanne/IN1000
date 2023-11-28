""" OPPGAVE 1: Utskriftsprosedyre """

#1.2
def utskriftsfunksjon():
    #tar inn et navn og et bosted fra brukeren og lagrer det i variabler
    navn = input("skriv inn navn: ")
    bosted = input("hvor kommer du fra? ")

    #skriver ut informasjonen som er lagret i variablene
    print("Hei, " + navn + "! Du er fra " + bosted + ".")

#kaller på prosedyren 3 ganger
for i in range(0,3):        #lager en for-løkke som kjører 3 ganger  
    print("")               #printer tom linje for å få litt luft i terminalen
    utskriftsfunksjon()     #kaller på prosedyren



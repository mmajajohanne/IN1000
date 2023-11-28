""" OPPGAVE 1: Utskrift og innlesing av variabler"""

# 1.3 
# brukerinput for å finne navn
navn = input("Hva heter du? ")
print("Hei", navn)

# 1.4, 1.5
# finne differansen av to variabler med heltallsverdi
a = 6
b = 3
print("a=",a)
print("b=",b)

differanse = a-b
print("Differanse:", differanse)

# 1.6, 1.7
# ber bruker oppgi nytt navn og lager variabelen sammen
navn2 = input("Oppgi et nytt navn: ")
sammen = navn + navn2
print("Sammen:", sammen)
# endrer variabelen sammen
sammen = navn + " og " + navn2
print("Sammen:", sammen)
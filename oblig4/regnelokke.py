# OPPGAVE 1: Regning med løkker

#1.1, 1.2
liste = [] #oppretter en tom liste
while True:
    tall = float(input("Skriv inn tall:")) #henter inn et tall fra brukeren
    liste.append(tall) #legger til tallet i lista
    if tall == 0.0: #hvis tallet fra brukeren er lik 0, avsluttes while-løkken
        break

#1.3
#går gjennom og printer hvert element i lista
for e in liste:
    print(e)

#1.4
#regner ut summen av lista
minSum = 0
for e in liste:
    minSum += e #går gjennom og legger hvert element i lista til sum-variabelen
print(f"summen er {minSum}")

#1.5
#finner største element i lista
største = 0
#går gjennom hvert element i lista og tester om verdien er større enn variabelen største
#hvis ja: erstatt verdien til største med verien til elementet
for e in liste:
    if e > største: 
        største = e 
print(f"største tall er {største}")

#finner minste element i lista
#går gjennom hvert element i lista og tester om verdien er mindre enn variabelen minste
#hvis ja: erstatt verdien til minste med verien til elementet
minste = 0
for e in liste:
    if e < minste:
        minste = e
print(f"minste tall er {minste}")

""" OPPGAVE1: Lister """
#1.1
liste = [3,6,9]                 # oppretter en liste med tre tall
liste.append(12)                # legger til 12 bakerst i listen
print(liste[0], liste[2])       # skriver ut første og tredje element i listen
#hei

#1.2
#lager en tom liste
navneliste = []
#lager en for-løkke som kjører 4 ganger
for i in range(4):
    navneliste.append((input("Skriv inn et navn:").upper())) #gjør input fra brukeren til store bokstaver og legger i lista

#tester om navnet mitt ligger i listen med en if-test
if "MAJA" in navneliste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")


#1.3
#lager to variabler, en for summen og en for produktet av lista
summen = sum(liste)     #bruker funksjonen sum for å finne summen av hvert element i lista
produkt = 1
#kjører gjennom hvert element i lista og ganger dem med hverandre for å finne produktet
for i in range(0,len(liste)):
    produkt = produkt * liste[i]

#definerer en ny liste med to elementer: summen og produktet
liste2 = [summen,produkt]

#lager en ny liste som består av den originale og den nye lista
liste3 = liste + liste2 
print(liste3) #skriver ut lista til terminalen

#fjerner de to siste elementene
liste3.pop()
liste3.pop()

#skriver ut lista til terminalen
print(liste3)

""" OPPGAVE 3: Billettpris """

def billettpris():
    alder = int(input("skriv inn en alder: "))
    billettpris = 0
    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50
    
    print("Billettprisen er: ", billettpris, "kr.")

billettpris()

#prosedyren funker fint:)

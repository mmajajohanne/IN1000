""" OPPGAVE 2: Beslutninger """

# 2.1
# spør brukeren spørsmålet og lagrer svaret i en variabel svar
svar = input("Kunne du tenke deg en brus? Skriv ja eller nei: ")

# 2.2
# lager en if-løkke som sjekker variabelen svar og gir en respons basert på svaret til brukeren
if svar == "ja":
    print("Her har du en brus!")
elif svar == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")


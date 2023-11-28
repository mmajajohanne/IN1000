""" OPPGAVE 3 """

# 3.3
# spør brukeren om datoene og lagrer svarene i to variabler
print("Oppgi datoene på formen mmdd, der f.eks datoen 2 januar skrives som 0102")
dato1 = int(input("Oppgi dato 1 (mmdd): "))
dato2 = int(input("Oppgi dato 2 (mmdd): "))

# lager en if-løkke som sjekker om dato1 er mindre enn dato2
if dato1 < dato2:
    print("Riktig rekkefølge!")
# dersom dato1 er større enn dato2, er rekkefølgen feil
elif dato1 > dato2:
    print("Feil rekkefølge!")
# dersom dato1 er lik dato2, er datoene like
else:
    print("Samme dato!")




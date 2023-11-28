""" OPPGAVE 3: Problemløsning med beslutninger """
# 3.1
# spør brukeren om dato og lagrer svaret i to variabler, dag og måned
dag1 = int(input("Oppgi dag 1: "))
måned1 = int(input("Oppgi måned 1: "))

dag2 = int(input("Oppgi dag 2: "))
måned2 = int(input("Oppgi måned 2: "))

# 3.2
# lager en if-løkke som sjekker om dag1 og måned1 er mindre enn dag2 og måned2
# sjekker først om måned1 kommer før måned2
if måned1 < måned2:
    print("Riktig rekkefølge!")
# dersom månedene er like, sjekker vi om dag1 kommer før dag2
elif måned1 == måned2:
    if dag1 < dag2:
        print("Riktig rekkefølge!")
    elif dag1 == dag2:
        print("Samme dato!")
    else:
        print("Feil rekkefølge!")
# dersom måned1 kommer etter måned2, er rekkefølgen feil
else:
    print("Feil rekkefølge!")

""" OPPGAVE 5: Egen oppgave """

""" Oppgave: Rabattkalkulator med Kundelojalitet
    Lag et Python-program som tar inn følgende informasjon fra brukeren: 

    - Kjøpsbeløpet
    - Antall tidligere kjøp kunden har gjort
    - Kundens medlemsnivå: Gull, Sølv eller ingen 

    Programmet skal beregne den totale rabatten, og vise den til brukeren

    Hvis kjøpsbeløpet er:
    - under 1000 kroner = ingen rabatt.
    - mellom 1000 og 4999 kroner = 5% rabatt.
    - mellom 5000 og 9999 kroner = 10% rabatt.
    - 10000 kroner eller mer = 15% rabatt.

    Hvis kunden har gjort 5 eller flere tidligere kjøp, får de 3% ekstra rabatt uavhengig av medlemsnivå.
    - Gull-medlemmer får alltid 2% ekstra rabatt
    - Sølv-medlemmer får 1% ekstra rabatt """

#SVAR:

# henter inn input fra brukeren
beløp = float(input("Skriv inn kjøpsbeløpet: "))
antall_tidligere_kjop = int(input("Skriv inn antall tidligere kjøp hos oss: "))
medlemsniva = input("Oppgi medlemsnivået ditt (Gull, Sølv eller ingen): ")


# bruker if/else-betingelser for å beregne rabatt basert på kjøpsbeløp
if beløp < 1000:
    rabatt = 0
elif beløp < 5000:
    rabatt = 0.05 * beløp
elif beløp < 10000:
    rabatt = 0.10 * beløp
else:
    rabatt = 0.15 * beløp

# legger til ekstra rabatt for kundelojalitet og medlemsnivå  
if antall_tidligere_kjop >= 5:
    rabatt += 0.03 * beløp

if medlemsniva == "Gull":
    rabatt += 0.02 * beløp
elif medlemsniva == "Sølv":
    rabatt += 0.01 * beløp

# skriver ut rabatten til brukeren
print(f"Din totale rabatt er: {rabatt:.2f} kroner")

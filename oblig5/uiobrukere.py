""" OPPGAVE 4: UiO-brukere """


# 4.1
def lagBrukernavn(navn):
    navn = navn.split()  # deler mellom for og etternavn
    brukernavn = navn[0].lower() + navn[1][0].lower()  # setter sammen brukernavnet
    return brukernavn


# 4.6
def lagUnikeBrukernavn(navn, ordbok):
    navn = navn.split()  # deler mellom for og etternavn
    brukernavn = (
        navn[0].lower() + navn[1][0].lower()
    )  # setter sammen brukernavn, "første forsøk"
    i = 1
    while brukernavn in ordbok:  # dersom brukernavnet allerede finnes i ordboken
        brukernavn += navn[1][i]  # legg til neste bokstav i etternavnet
        i += 1
    return brukernavn


# 4.2
def lagEpost(brukernavn, suffix):
    epost = str(brukernavn) + "@" + suffix  # setter sammen eposten
    return epost


# tester funksjonen
print(lagEpost(lagBrukernavn("Kari Nordmann"), "student.matnat.uio.no"))


# 4.3
ordbok1 = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}


def skrivUtEposter(ordbok):
    for (
        brukernavn,
        suffix,
    ) in ordbok.items():  # itererer gjennom hvert av elementene i ordboken
        epost = lagEpost(
            brukernavn, suffix
        )  # bruker funksjonen lagEpost på hvert av elementene
        print(epost)


# tester funksjonen
skrivUtEposter(ordbok1)


# 4.4
navne_ordbok = {}

svar = ""
while svar != "s":  # while løkken kjører frem til brukeren taster inn "s"
    svar = str(input("skriv inn en kommando (i, p eller s):"))
    if svar == "i":
        navn = str(input("skriv inn et navn"))
        suffix = str(input("skriv inn en suffix"))
        brukernavn = lagUnikeBrukernavn(navn, navne_ordbok)  # lager først brukernavn
        navne_ordbok[
            brukernavn
        ] = suffix  # legger til i ordboken, med brukernavn som nøkkel- og suffix innholdsverdi
    elif svar == "p":
        skrivUtEposter(navne_ordbok)


# 4.5
def test_lagBrukernavn():
    # Test 1
    resultat_brukernavn = lagBrukernavn("Marie Curie")
    riktig_brukernavn = "mariec"
    assert (
        resultat_brukernavn == riktig_brukernavn
    ), f"Forventet brukernavn {riktig_brukernavn}, men fikk {resultat_brukernavn}"

    # Test 2
    resultat_brukernavn = lagBrukernavn("Rachel CARSON")
    riktig_brukernavn = "rachelc"
    assert (
        resultat_brukernavn == riktig_brukernavn
    ), f"Forventet brukernavn {riktig_brukernavn}, men fikk {resultat_brukernavn}"


def test_lagEpost():
    # Test 1
    resultat_epost = lagEpost("mariec", "eksempel.com")
    riktig_epost = "mariec@eksempel.com"
    assert (
        resultat_epost == riktig_epost
    ), f"Forventet e-post {riktig_epost}, men fikk {resultat_epost}"

    # Test 2
    resultat_epost = lagEpost("rachelc", "ifi.uio.no")
    riktig_epost = "rachelc@ifi.uio.no"
    assert (
        resultat_epost == riktig_epost
    ), f"Forventet e-post {riktig_epost}, men fikk {resultat_epost}"


# Kjører testene
test_lagBrukernavn()
test_lagEpost()

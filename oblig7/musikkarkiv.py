from sang import Sang
from spilleliste import Spilleliste


def hovedprogram():
    # oppretter tom ordbok for musikkarkivet
    mine_spillelister = {}

    # lager en spilleliste musikk og henter inn sangene fra fil
    musikk = Spilleliste("musikk")
    musikk.les_fra_fil()
    # legger inn musikk-listen i ordboken
    mine_spillelister["musikk"] = musikk

    # lager en spilleliste queen
    queen = Spilleliste("queen")
    # går gjennom hvert element i musikk-listen og henter ut sanger av artisten queen i en liste
    for sang in musikk.hent_artist_utvalg("queen"):
        queen.legg_til_sang(sang)
    # legger til queen-listen i ordboken
    mine_spillelister["queen"] = queen

    # lager en ny spilleliste study
    study = Spilleliste("study")
    # legger til 3 sanger i spillelisten ved å opprette sang-objekter
    study.legg_til_sang(Sang("Rollerblades", "Dominic Fike"))
    study.legg_til_sang(Sang("Haircut", "Ryan Beatty"))
    study.legg_til_sang(Sang("the climb", "ROLE MODEL"))
    # legger til study-listen i ordboken
    mine_spillelister["study"] = study

    # spiller alle sangene i study-spillelisten
    mine_spillelister["study"].spill_alle()

    # itererer gjennom ordboken og skriver hver av listene til sin egen fil
    for _, spilleliste in mine_spillelister.items():  # bruker _ som en ubrukt variabel
        spilleliste.skriv_til_fil()


hovedprogram()

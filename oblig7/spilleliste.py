from sang import Sang


class Spilleliste:
    def __init__(self, listenavn: str):
        self._sanger = []
        self._navn = listenavn

    # mdetode som leser inn sanger fra en fil og legger dem til i spillelisten
    def les_fra_fil(self):
        # with open sikrer at filen lukkes igjen etter bruk
        with open(self._navn + ".txt") as fil:
            for linje in fil:
                # leser inn dataen fra hver enkelt linje
                data = linje.strip().split(";")
                # oppretter et nytt Sang-objekt og legg det til i listen
                self._sanger.append(Sang(data[0], data[1]))

    # metode som legger til en oppgitt sang i spillelisten
    def legg_til_sang(self, ny_sang: Sang):
        self._sanger.append(ny_sang)

    # metode som fjerner en oppgitt sang fra spille.isten
    def fjern_sang(self, sang: Sang):
        self._sanger.remove(sang)

    # metode som spiller alle sangene i spillelisten (i terminalen)
    def spill_alle(self):
        for objekt in self._sanger:
            # bruker spill() metoden til objektet fra klassen Sang
            objekt.spill()

    # metode som finner en eventuell sang med oppgitt tittel i spillelisten
    def finn_sang_tittel(self, tittel: str):
        for objekt in self._sanger:
            # bruker sjekk_tittel() metoden fra Sang
            if objekt.sjekk_tittel(tittel) == True:
                return objekt
        return None

    # metode som henter alle sanger der artisten har ett eller flere navn fra det oppgitte navnet
    def hent_artist_utvalg(self, artistnavn: str):
        returliste = []
        for objekt in self._sanger:
            # bruker sjekk_artist() metoden fra Sang på objektet
            if objekt.sjekk_artist(artistnavn) == True:
                returliste.append(objekt)
        return returliste

    # metode som skriver spillelisten til en tekstfil med samme navn
    def skriv_til_fil(self):
        # åpner filen, med "w" fordi den skal skrives til
        with open(self._navn + ".txt", "w") as spillelistefil:
            for objekt in self._sanger:
                spillelistefil.write(objekt.streng_til_fil())
        # with open lukker automatisk filen etter bruk

    # __str__ metode som returnerer en brukervennlig streng med navnet og innholdet i spillelisten
    def __str__(self):
        streng = f"Navnet på spillelisten er {self._navn} og den besår av:\n"
        for objekt in self._sanger:
            streng += str(objekt) + "\n"
        return streng

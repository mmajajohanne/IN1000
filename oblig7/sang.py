class Sang:
    # konstruktør som lagrer sangens tittel og artist
    def __init__(self, tittel: str, artist: str):
        self._tittel = tittel
        self._artist = artist

    # metode som printer sangen som spilles i terminalen
    def spill(self):
        print(f"Nå spilles {self._tittel} med {self._artist}")

    # metode som sjekker om hele eller deler av navnet oppgitt er i navnet til sangens artist
    def sjekk_artist(self, navn: str):
        navnliste = (
            navn.lower().split()
        )  # bruker metoden .lower() for å gjøre alle bokstavene små
        artistliste = self._artist.lower().split()
        # itererer gjennom navnene i navnliste og gjør sjekken
        for delnavn in navnliste:
            if delnavn in artistliste:
                return True
            else:
                return False

    # metode som sjekker om titelen oppgitt og tittelen på sangen er den samme
    def sjekk_tittel(self, tittel: str):
        return self._tittel.lower() == tittel.lower()

    # metode som sjekker om tittelen og hele eller deler av artistnavnet oppgitt er den samme som de lagrede navnene
    def sjekk_artist_og_tittel(self, artist: str, tittel: str):
        return self.sjekk_tittel(tittel) and self.sjekk_artist(artist)

    # metode som returnerer en streng med objektets innhold på filinnhold-form, avsluttet med linjeskift
    def streng_til_fil(self):
        return f"{self._tittel};{self._artist}\n"

    # metode som returnerer en streng med objektets innhold på format: "Sang med Artist"
    def __str__(self):
        return f"{self._tittel} med {self._artist}"

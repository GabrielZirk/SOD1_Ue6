import abc
from typing import List, Dict

class Fluessigkeit:
    def __init__(self, name: str, menge: float, alkohol_prozent: float):
        self.name = name
        self.menge = menge
        self.alkohol_prozent = alkohol_prozent

class Brennbar(abc.ABC):

    @abc.abstractmethod
    def brennt(self) -> bool:
        pass

class Getraenk(Brennbar):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    @abc.abstractmethod
    def get_anzahl_zutaten(self) -> int:
        pass

    @abc.abstractmethod
    def beinhaltet_alkohol(self) -> bool:
        pass

    @abc.abstractmethod
    def menge_in_ml(self) -> float:
        pass

class SimplesGetraenk(Getraenk):
    def __init__(self, name, bestandteil: Fluessigkeit):
        super().__init__(name)
        self.name = name
        self.bestandteil = bestandteil

    def get_anzahl_zutaten(self) -> int:
        return 1

    def beinhaltet_alkohol(self):
        if self.bestandteil.alkohol_prozent > 0:
            return True
        elif self.bestandteil.alkohol_prozent == 0:
            return False

    def menge_in_ml(self):
        return self.bestandteil.menge

    def brennt(self):
        if self.bestandteil.alkohol_prozent >= 30:
            return True
        else:
            return False

class Longdrink(Getraenk):
    def __init__(self, name, spirituose: Fluessigkeit, filler: Fluessigkeit):
        super().__init__(name)
        self.name = name
        self.spirituose = spirituose
        self.filler = filler

    def get_anzahl_zutaten(self) -> int:
        return 2

    def menge_in_ml(self) -> float:
        return self.spirituose.menge + self.filler.menge

    def brennt(self):
        if self.spirituose.alkohol_prozent >= 30:
            return True
        else:
            return False

    def beinhaltet_alkohol(self):
        if self.spirituose.alkohol_prozent > 0:
            return True
        elif self.spirituose.alkohol_prozent == 0:
            return False

class Cocktail(Getraenk):
    def __init__(self, name: str, bestandteile: List[Fluessigkeit]):
        super().__init__(name)
        self.name = name
        self.bestandteile = bestandteile

    def get_anzahl_zutaten(self):
        return len(self.bestandteile)

    def menge_in_ml(self):
        menge = 0
        for fl in self.bestandteile:
            menge += fl.menge
        return menge

    def brennt(self) -> bool:
        for fl in self.bestandteile:
            if fl.alkohol_prozent > 30:
                return True
        return False

    def beinhaltet_alkohol(self) -> bool:
        for fl in self.bestandteile:
            if fl.alkohol_prozent > 0:
                return True
        return False

class Registrierkasse:
    def __init__(self):
        self.__getraenkeliste = []
        self.__verkaufte_getraenke = 0

    def verkauft(self, g: Getraenk):
        self.__getraenkeliste.append(g)
        self.__verkaufte_getraenke += 1

    def printGetraenkeSortiertNachAnzahlZutaten(self):
        return sorted(self.__getraenkeliste, key = lambda g: g.get_anzahl_zutaten(), reverse = True) # keine Ahnung was eine "Comparator Klasse" ist, deshalb hab ichs so gelöst

    def get_getraenke_aufgeteilt_nach_zutaten(self) -> Dict[int, List[Getraenk]]:
        dict_getraenke = dict()
        set_getraenkeliste = set(self.__getraenkeliste)

        for getr in set_getraenkeliste:
            if getr not in dict_getraenke:
                zutatenanzahl = getr.get_anzahl_zutaten()
                if zutatenanzahl not in dict_getraenke.keys():
                    dict_getraenke[zutatenanzahl] = []
                dict_getraenke[zutatenanzahl].append(getr)
        return dict_getraenke

if __name__ == '__main__':
    Cola = Fluessigkeit("Cola", 100.0, 0.0)
    Rum = Fluessigkeit("Rum", 20.0, 50.0)
    Colapur = SimplesGetraenk("Colapur", Cola)
    Soda = Fluessigkeit("Soda", 250.0, 0.0)
    Sodapur = SimplesGetraenk("Soda", Soda)
    ColaRum = Longdrink("ColaRum", Rum, Cola)
    ZitronenSft = Fluessigkeit("Zitronensaft", 20, 0.0)
    Havanarum = Fluessigkeit("Havanarum", 20.0, 40.0)
    Schnaps = Fluessigkeit("Schnaps", 40.0, 60.0)
    SoZi = Longdrink("Soda Zitrone", Soda, ZitronenSft)

    LIIT = Cocktail("Long Island Ice Tea", [Cola, Rum, ZitronenSft, Havanarum, Schnaps])

    print(LIIT.brennt())
    print(LIIT.beinhaltet_alkohol())
    print(LIIT.get_anzahl_zutaten())

    Kasse = Registrierkasse()
    Kasse.verkauft(Colapur)
    Kasse.verkauft(ColaRum)
    Kasse.verkauft(LIIT)
    Kasse.verkauft(ColaRum)
    Kasse.verkauft(Colapur)
    Kasse.verkauft(SoZi)
    Kasse.verkauft(Sodapur)

    print(Kasse.printGetraenkeSortiertNachAnzahlZutaten())
    print(Kasse.get_getraenke_aufgeteilt_nach_zutaten())

    print(Colapur.beinhaltet_alkohol())
    print(Colapur.brennt())

    print(ColaRum.brennt())
    print(ColaRum.beinhaltet_alkohol())
    print(ColaRum.menge_in_ml())




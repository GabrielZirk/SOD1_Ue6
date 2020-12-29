import abc
from typing import List

class Ente(abc.ABC):
    def __init__(self, name: str, gewicht: int):
        self._name = name
        self._gewicht = gewicht

    @property
    def name(self):
        return self._name

    @property
    def gewicht(self):
        return self._gewicht

    @abc.abstractmethod
    def get_full_weight(self) -> int:
        pass

    @abc.abstractmethod
    def make_noise(self):
        pass

class FlugEnte(Ente):
    species = "Flugente"

    def __init__(self, name: str, gewicht: int, gewicht_federn: int):
        super().__init__(name, gewicht)
        self._name = name
        self._gewicht = gewicht
        self._gewicht_federn = gewicht_federn

    def __repr__(self):
        return f"Flugentenname: {self._name}, Gewicht: {self._gewicht}, Gewicht Federn: {self._gewicht_federn}"

    def get_full_weight(self):
        fullweight = self._gewicht + self._gewicht_federn
        return fullweight

    def make_noise(self):
        print("Quaki quaki")

class BadeEnte(Ente):
    species = "Badeente"

    def __init__(self, name: str, gewicht: int, gewicht_wasser: int):
        super().__init__(name, gewicht)
        self._name = name
        self._gewicht = gewicht
        self._gewicht_wasser = gewicht_wasser

    def __repr__(self):
        return f"Badeentenname: {self._name}, Gewicht: {self._gewicht}, Gewicht Wasser: {self._gewicht_wasser}"

    def get_full_weight(self):
        fullweight = self._gewicht + self._gewicht_wasser
        return fullweight

    def make_noise(self):
        print("BlUbB bLuBb")

class Entenhausen:
    def __init__(self):
        self.__einwohner = []

    def add(self, duckname: Ente):
        self.__einwohner.append(duckname)

    def get_gruppierte_enten(self) -> {int: List[Ente]}:
        entensteuer = {100: [],
        200: [],
        300: []}

        for duck in range(len(self.__einwohner)):
            if (self.__einwohner[duck].get_full_weight() <= 100):
                entensteuer[100].append(self.__einwohner[duck]._name)
            elif (self.__einwohner[duck].get_full_weight() > 100) and (self.__einwohner[duck].get_full_weight() <= 200):
                entensteuer[200].append(self.__einwohner[duck]._name)
            elif (self.__einwohner[duck].get_full_weight() > 200) and (self.__einwohner[duck].get_full_weight() <= 300):
                entensteuer[300].append(self.__einwohner[duck]._name)

        return entensteuer

if __name__ == '__main__':
    Flugente1 = FlugEnte("Josef", 40, 50)
    Flugente2 = FlugEnte("Johann", 225, 10)
    Flugente3 = FlugEnte("Jonathan", 295, 5)
    Flugente4 = FlugEnte("Jesus", 75, 100)
    Badeente1 = BadeEnte("Tauchi", 100, 150)
    Badeente2 = BadeEnte("Plantschi", 75, 100)
    Badeente3 = BadeEnte("Blubbär", 150, 25)

    Entenmanager = Entenhausen()
    Entenmanager.add(Flugente1)
    Entenmanager.add(Flugente2)
    Entenmanager.add(Flugente3)
    Entenmanager.add(Flugente4)
    Entenmanager.add(Badeente1)
    Entenmanager.add(Badeente2)
    Entenmanager.add(Badeente3)

    print(Entenmanager.get_gruppierte_enten())
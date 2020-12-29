import unittest
from Beispiele.Beispiel1 import FlugEnte


class FlugEnteTest(unittest.TestCase):

    def setUp(self) -> None:
        self.flugente = FlugEnte("Testi1", 100, 50)

    def test_fullweight1(self):
        fullweight_flugente = self.flugente.get_full_weight()
        self.assertEqual(fullweight_flugente, 150)

    def test_fullweight2(self):
        fullweight_flugente = self.flugente.get_full_weight()
        self.assertTrue(fullweight_flugente == 150)


if __name__ == '__main__':
    unittest.main()

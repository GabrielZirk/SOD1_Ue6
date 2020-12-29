import unittest
from Beispiele.Beispiel1 import BadeEnte


class BadeEnteTest(unittest.TestCase):
    def setUp(self):
        self.badeente = BadeEnte("Testi2", 100, 150)

    def test_fullweight3(self):
        fullweight_badeente = self.badeente.get_full_weight()
        self.assertEqual(fullweight_badeente, 250)


if __name__ == '__main__':
    unittest.main()

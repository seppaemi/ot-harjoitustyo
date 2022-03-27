import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
      self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
      self.maksukortti.lataa_rahaa(290)
      self.assertEqual(str(self.maksukortti), "saldo: 3.0")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
      self.maksukortti.ota_rahaa(3)
      self.assertEqual(str(self.maksukortti), "saldo: 0.07")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
      self.maksukortti.ota_rahaa(20)
      self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true_jos_rahat_riittaa(self):
      self.assertEqual(self.maksukortti.ota_rahaa(11), False)
      self.assertEqual(self.maksukortti.ota_rahaa(10), True)
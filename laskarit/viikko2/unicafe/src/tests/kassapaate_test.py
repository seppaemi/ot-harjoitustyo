import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()
    self.maksukortti = Maksukortti(1000)

#Testataan kassapäätteen alustus on ok
  def test_luotu_kassapaate_alustaa_rahan_oikein(self):
    self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

  def test_luotu_kassapaate_alustaa_maukkaat_oikein(self):
    self.assertEqual(self.kassapaate.maukkaat,0)
  
  def test_luotu_kassapaate_alustaa_edulliset_oikein(self):
    self.assertEqual(self.kassapaate.edulliset,0)


#Testataan käteisnoston toimivuuttasekä edullisten että maukkaiden lounaiden osalta
  def test_jos_maksu_riittaa_vaihtoraha_ok_maukas(self):
    self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)

  def test_jos_maksu_riittaa_kassan_saldo_ok_maukas(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

  def test_jos_maksu_riittaa_vaihtoraha_ok_edullinen(self):
    self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300),60)

  def test_jos_maksu_riittaa_kassan_saldo_ok_edullinen(self):
    self.kassapaate.syo_edullisesti_kateisella(300)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

  def test_jos_maksu_riittaa_myydyt_lounaat_kasvaa_maukas(self):
    self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(self.kassapaate.maukkaat,1)

  def test_jos_maksu_riittaa_myydyt_lounaat_kasvaa_edullinen(self):
    self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(self.kassapaate.edulliset,1)

#Testataan tilanteita käteismaksussa jossa maksu ei ole riittävä
  
  def test_jos_maksu_ei_riita_kassan_saldo_ei_muutu_maukas(self):
    self.kassapaate.syo_maukkaasti_kateisella(300)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_jos_maksu_ei_riita_vaihtoraha_palautetaan_kokonaan_maukas(self):
    self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

  def test_jos_maksu_ei_riita_kassan_saldo_ei_muutu_edullinen(self):
    self.kassapaate.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_jos_maksu_ei_riita_vaihtoraha_palautetaan_kokonaan_edullinen(self):
    self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

  def test_jos_maksu_ei_riita_myydyt_lounaat_ei_kasva_maukas(self):
    self.kassapaate.syo_maukkaasti_kateisella(300)
    self.assertEqual(self.kassapaate.maukkaat, 0)
  
  def test_jos_maksu_ei_riita_myydyt_lounaat_ei_kasva_edullinen(self):
    self.kassapaate.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassapaate.edulliset, 0)

#Testataan, että korttiostot toimii sekä edullisten että maukkaiden lounaiden osalta
  def test_jos_kortilla_tarpeeksi_rahaa_veloitetaan_summa_maukas(self):
    self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    self.assertEqual(str(self.maksukortti), "saldo: 6.0")
   
  def test_jos_kortilla_tarpeeksi_rahaa_veloitetaan_summa_edullinen(self):
    self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    self.assertEqual(str(self.maksukortti), "saldo: 7.6")

  def test_jos_kortilla_tarpeeksi_rahaa_myydyt_lounaat_kasvaa_maukas(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.maukkaat,1)
  
  def test_jos_kortilla_tarpeeksi_rahaa_myydyt_lounaat_kasvaa_edullinen(self):
    self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.edulliset,1)

#Testataan jos korttimaksussa kortin saldo ei ole riittävä
  def test_jos_kortilla_ei_riita_rahat_kortin_saldo_pysyy_maukas(self):
    kortti = Maksukortti(200)
    self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    self.assertEqual(str(kortti), "saldo: 2.0")

  def test_jos_kortilla_ei_riita_rahat_kortin_saldo_pysyy_edullinen(self):
    kortti = Maksukortti(200)
    self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    self.assertEqual(str(kortti), "saldo: 2.0")

  def test_jos_kortilla_ei_riita_rahat_myydyt_lounaat_ei_kasva_maukas(self):
    kortti = Maksukortti(200)
    self.kassapaate.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(self.kassapaate.maukkaat,0)

  def test_jos_kortilla_ei_riita_rahat_myydyt_lounaat_ei_kasva_edullinen(self):
    kortti = Maksukortti(200)
    self.kassapaate.syo_edullisesti_kortilla(kortti)
    self.assertEqual(self.kassapaate.edulliset,0)

#Testataan että rahamäärä ei muutu kortilla ostaessa
  def test_jos_maksaa_kortilla_kassan_rahamaara_pysyy_samana_maukas(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  
  def test_jos_maksaa_kortilla_kassan_rahamaara_pysyy_samana_edullinen(self):
    self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
# Testataan, että kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
  def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
    self.assertEqual(str(self.maksukortti), "saldo: 15.0")
  
  def test_kortille_rahaa_ladattaessa_kassa_kasvaa(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

#Testataan , että kun ladataan kortille rahaa negatiivisella summalla niin kassan arvo ei muutu eikä kortin saldo
  def test_kortille_ladatattaessa_negatiivinen_summa_ei_muutoksia(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(self.maksukortti), "saldo: 10.0")
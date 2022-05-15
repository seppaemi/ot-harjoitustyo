# Testausdokumentti

Sovellusta on testattu unittestillä sekä käyttöliittymää käsin tapahtuvalla järjestelmätestauksella.

## Yksikkö- sekä integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikan luokkia <code>Service</code>testataan testiluokilla <code>TesService</code>.
Luokille injektoidaan testeissä päätietokannan sijaan testitietokanta.

### Repositorio-luokat

Luokkia <code>UserRepository</code> ja <code>ItemRepository</code> testataan testiluokilla <code>TestUserRepository</code> sekä <code>TestPasswordRepository</code>.
Luokille injektoidaan testeissä päätietokannan sijaan testitietokanta.

## Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 86%

![Coverage report](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testikattavuus.png)

Testaamatta jäi tietokannan alustuksesta vastaava luokka <code>initialize_database.py</code>

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

## Sovellukseen jääneet laatuongelmat

- Tuotteiden lisäyksessä ei ole asetettu ylärajaa inputeille
- Uuden käyttäjän luomisen onnistumisesta ei ilmoiteta käyttäjälle

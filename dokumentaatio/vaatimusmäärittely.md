# Vaatimusmäärittely, kauppalistasovellus
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjällä on mahdollista pitää yllä tietoa siitä, mitä hänen tulee ostaa seuraavalla kerralla kaupasta. Käyttäjä voi lisätä itse tarvitsemansa ostokset listaan rekisteröityneenä käyttäjänä. Useampi käyttäjä voi käyttää sovellusta omalla käyttäjätunnuksellaan.
## Käyttäjät
Sovellukseen voi kirjautua käyttäjätunnuksella ja salasanalla. TEHTY
## Käyttöliittymä
Käyttöliittymässä on kolme näkymää:
1. *Kirjautumissivu*, jossa on kirjoiusalue käyttäjätunnukselle ja salasanalle, sekä kohta josta voi luoda uuden käyttäjätunnuksen. TEHTY
2. *Tunnuksenluonti-ikkuna*, johon käyttäjä keksii itselleen uniikin tunnuksen ja salasanan, joilla myöhemmin voi kirjautua sisään TEHTY
3. *Kauppalista,* jossa näkyy tehtävät ostokset listana ja johon käyttäjä voi lisätä uusia ostoksia.
## Perusversio sisältää
### Kirjautuessa
- Käyttäjä voi luoda järjestelmään uniikin tunnuksen ja salasanan TEHTY
- Käyttäjä voi kirjautua järjestelmään tunnuksellaan. Mikäli tämä epäonnistuu, järjestelmä antaa virheilmoituksen TEHTY
### Kirjautumisen jälkeen
- Käyttäjä pääsee näkemään oman kauppalistansa
- Käyttäjä voi lisätä uuden ostoksen, joka näkyy vain hänelle 
- Käyttäjä voi merkitä ostoksen tehdyksi, jolloin se häviää kauppalistasta TEHTY
- Käyttäjä voi kirjautua ulos TEHTY
## Jatkokehitysideoita
Perusversioon voitaisiiin lisätä seuraavat toiminnallisuudet:
- Käyttäjä voi luoda yhteiskauppalistan johon myös muut ruokakunnan jäsenet voivat lisätä ostoksia
- Käyttäjä voi tarkastella aiempia ostoksiaan
- Käyttäjä voi lisätä ostoksille hinnan ja tarkastella ostosten yhteissummaa
- Käyttäjä voi luoda useampia eri kauppalistoja
- Käyttäjä voi poistaa kokonaisen kauppalistan

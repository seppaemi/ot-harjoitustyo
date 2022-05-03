# Käyttöohje

### Sovelluksen käynnistäminen
Ohje olettaa, että käyttäjällä on koneellaan poetry valmiiksi asennettuna.

#### Riippuvuuksien asennus
`poetry install`

#### Ohjelman ajaminen
`poetry run invoke start`

#### Testien ajaminen
`poetry run invoke test`

#### Testikattavuusraportti
`poetry run invoke coverage-report`

Komento muodostaa kansion "htmlcov", jonka sisältä löytyy tiedosto "index.html". Avaamalla tiedoston selaimella näkee kattavuusraportin.

### Sovellus

Sovellus aukeaa kirjautumisnäkymään. Käyttäjä voi kirjautua järjestelmään luomallaan käyttäjällä.

Rekisteröitymissivulla käyttäjä voi luoda järjestelmään uuden tunnuksen ja cancel-napilla käyttäjä pääsee takaisin kirjautumissivulle.

Käyttäjän kirjautuessa sisään oikeala käyttäjällä, näytetään käyttäjän oma sivu ja logout-napilla käyttäjä kirjataan ulos.

Käyttäjän omalta sivulta käyttäjä pääsee tuotteiden lisäyssivulle ja cancel-napilla käyttäjä ohjataan takaisin omalle sivulle.
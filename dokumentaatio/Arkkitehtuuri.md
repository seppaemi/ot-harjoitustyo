# rakenne
![image](https://user-images.githubusercontent.com/99639312/163024288-ce210d9e-92cd-49ec-b05c-d528cb6d0cff.png)
Pakkaus ui sisältää käyttöliittymään liittyvän koodin, repositories tietokannan kanssa keskustelevan koodin,
services sovelluslogiikan koodin, sekä entities sovellukseen liittyvät tietokohteet.

# sovelluslogiikka
Ohjelman pohjan muodostavat User ja Item luokat, jotka kuvaavat käyttäjää ja hänen lisäämiään tuotteita. Toiminnallisista kokonaisuuksista vastaa Service:n luokka ItemService. Luokassa on kaikille toiminnoille oma metodi, kuten login(username, password), find_items_by_user(user) sekä delete_items(item_id).

ItemService-luokkaan pääsee repositories kansiossa olevien luokkien UserRepository ja ItemRepository avulla käsiksi käyttäjiin ja tuotteisiin.

Käyttöliittymä sisältää 4 näkymää:
  - Kirjautuminen
  - Uuden käyttäjän luominen
  - Käyttäjän näkymä
  - Uusien tuotteiden lisäys
 Jokainen näistä on yksitellen avoinna ja näkymän vaihtamisesta vastaa UI-luokka.
 
# tiedon pysyväistalletus
ansion repositories luokka UserRepository pitää huolta käyttäjiin liittyvien tietojen tallennuksesta ja tallettaa ne SQLite-tietokantaan. Kansion repositories luokka ItemRepository Pitää huolta tuotteisiin liittyvien tietojen tallettamisesta ja tallettaa nekin SQLite-tietokantaan.

# Tietokannat
Käyttäjät tallennetaan SQLite-tietokantaan Users, joka alustetaan initialize_database.py-tiedostossa. Käyttäjien lisäämät tuotteet tallennetaan SQLite-tietokantaan Items,  joka alustetaan initialize_database.py-tiedostossa.


# käyttöliittymä
![image](https://user-images.githubusercontent.com/99639312/165266927-133d537a-323c-43fc-8018-501284bef6b1.png)
## sisäänkirjaus
Kun käyttäjä kirjautuu sisään, tulee hänen kirjoittaa näytöllä oleviin username- ja password-kenttiin käyttäjätunnuksensa ja salasanansa. Käyttäjä painaa login-painiketta, jonka myötä tapahtumankäsittelijä kutsuu Serviceä ja sitä kautta userRepositorya, tarkastaaseen että tunnus ja salasana täsmäävät. Jos ne täsmäävät, kirjautuminen onnistuu ja käyttäjä pääsee ItemViewiin. 

## tunnuksen luominen
Mikäli käyttäjä haluaa luoda uuden tunnuksen, painaa hän ensin sisäänkirjausnäytöllä olevaa painiketta joka johtaa käyttäjänluomissivulle. Siellä käyttäjä kirjoittaa näytöllä oleviin username- ja password-kenttiin haluamasna käyttäjätunnuksensa ja salasanansa. Käyttäjä painaa create-painiketta, jonka myötä tapahtumankäsittelijä kutsuu Serviceä ja sitä kautta userRepositorya, tarkastaaseen että käyttäjätunnus ei ole jo käytössä. Mikäli se on, tulee virheilmoitus, että tulee luoda uusi käyttäjä. Mikäli ei ole, tunnuksen luominen onnistuu ja käyttäjä saa kirjautua sisään. 

## Käyttäjän näkymä
Käyttäjän näkymässä on TreeView käyttäjän tuotteista, logout-nappi, add item-nappi ja remove item-nappi. Logout napilla käyttäjä kirjataan ulos Servicen avulla. Add itemissa siirrytään tapahtumakäsittelijän avulla tuotteen lisäämiseen ja remove itemilla voi poistaa tuotteen listalta väliaikaisesti. 

## tuotteen lisääminen
Tuotteen lisäämiseen pääsee etusivulta kohdasta "add item". Täällä käyttäjä täyttää kenttiin tuotteensa kategorian, määrän ja itse tuotteen. Servicen ja itemRepositoryn kautta ne lisätään tietokantatauluun, kun käyttäjä painaa udelleen "add item". Sitten tulee infolaatikko onnistuneesta lisäyksestä. Käyttäjä painaa vielä cancel päästäkseen takaisin etusivulle. Lopuksi uusi tuote päivitetään TreeViewiin nähtäväksi.

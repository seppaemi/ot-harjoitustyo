# rakenne
![image](https://user-images.githubusercontent.com/99639312/163024288-ce210d9e-92cd-49ec-b05c-d528cb6d0cff.png)
Pakkaus ui sisältää käyttöliittymään liittyvän koodin, repositories tietokannan kanssa keskustelevan koodin,
services sovelluslogiikan koodin, sekä entities sovellukseen liittyvät tietokohteet.

# käyttöliittymä
![image](https://user-images.githubusercontent.com/99639312/165266927-133d537a-323c-43fc-8018-501284bef6b1.png)

Käyttöliittymä sisältää 4 näkymää:
  - Kirjautuminen
  - Uuden käyttäjän luominen
  - Käyttäjän näkymä
  - Uusien salasanojen lisäys

# sovelluslogiikka
Sovellukseen tallennetaan käyttäjiä, jotka voivat tallentaa tuotteita. Molemmat lisätään joko User- tai Item-olioina

Sovelluksen sovelluslogiikasta vastaavat luokat UserService sekä ItemService.

# tietojen tallennus
Sovelluksen tiedot talletetaan SQLite-tietokantaan. Tietokanta sisältää taulut Users ja Items.

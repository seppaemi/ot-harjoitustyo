# Ohjelmistotkeniikan harjoitustyö ja sen tehtäviä
## Kauppalistasovellus
Sovelluksen avulla käyttjä voi tallettaa tietoon, mitä hänen tulee ostaa seuraavalla kauppareissullaan. SOvellusta voi käyttää samanaikaisesti useampi käyttäjä, joilla kaikilla on oma kauppalistansa. 
## Dokumentaatio
[vaatimusmäärittely](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[työaikakirjanpito](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/Ty%C3%B6aikakirjanpito.md)

[changelog](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri] (https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md)


### **Asennusohjeet**

1. Aloita asentamalla riippuvuudet koneella, ajamalla seuraava komento koneen terminaalissa:

```bash
poetry install
```

2. Sovelluksen voit käynnistää ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke start
```

### **Testaaminen**

Aloita testaaminen ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke test
```

### **Testikattavuus**

Tutki testikattavuutta ajamalla seuraava komento koneen terminaalissa:

```bash
poetry run invoke coverage-report
```
Tämän jälkeen htmlcov-kansiosta löytyy testikattavuusraportti index.html-tiedostosta.

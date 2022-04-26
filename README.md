# Ohjelmistotkeniikan harjoitustyö ja sen tehtäviä
## Kauppalistasovellus
Sovelluksen avulla käyttjä voi tallettaa tietoon, mitä hänen tulee ostaa seuraavalla kauppareissullaan. SOvellusta voi käyttää samanaikaisesti useampi käyttäjä, joilla kaikilla on oma kauppalistansa. 
## Dokumentaatio
[vaatimusmäärittely](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[työaikakirjanpito](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/Ty%C3%B6aikakirjanpito.md)

[changelog](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/seppaemi/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc  määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

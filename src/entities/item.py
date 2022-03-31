#tämän avulla voi lisätä uuden tuotteen kauppalistaan

#item on tuote jonka käyttäjä haluaa lisätä kauppalistaansa
#buy on boolean-arvo joka kertoo onko käyttäjä merkannut tuotteen hankituksi
#user on olio joka kuvastaa käyttäjää

class Item:
    def __init__(self, item=str, buy=False, user=None):
        self.item=item
        self.buy=buy
        self.user=user
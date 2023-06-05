# Créer la classe Book avec 5 à 10 attributs
# Créer le méthode net_price() price * 1.05

class Book:

    def __init__(self, id: str, title:str, price: float, type: str="", lang: str="fr-FR", nb_page:int=0):
        self.id = id
        self.title = title
        self.type = type
        self.nb_page = nb_page
        self.price = price
        self.lang = lang

    def get_net_price(self):
        return self.price * 1.05

b1 = Book("1","Python pour les nuls",10,nb_page=99)
print(b1.get_net_price())

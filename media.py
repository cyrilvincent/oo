import datetime

class Book:

# Créer le constructeur, les attributs
# net_price = price * 1.055
# tester

    def __init__(self, id: str, title: str, price: float,  date: datetime.datetime = datetime.datetime.now(), nb_page: int = 0):
        self.id = id
        self.title = title
        self.price = price
        self.date = date
        self.nb_page = nb_page

    def net_price(self):
        return self.price * 1.055

b1 = Book("001", "Python", 10)
print(f"Book price: {b1.net_price():.2f}")






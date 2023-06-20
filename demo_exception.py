import datetime

try:
    s = input("Année de naissance: ")
    year = int(s)
    age = datetime.datetime.now().year - year
    print(age)
except ValueError as ve:
    print(f"Erreur {ve}")
from typing import Tuple


def toto() -> Tuple[int, str]:
    return 0, "titi"

x, y = toto()
print(x, y)

dico = {"007" : "James Bond",
        "008" : "Cyril Vincent"}

for x in dico.values():
    print(x)
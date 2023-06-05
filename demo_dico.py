dico = {"007": "James Bond", "006": "Cyril Vincent", "005": "Toto"}
print(dico)
dico["001"] = "??"
print(dico)
for k in dico.keys():
    print(k, dico[k])
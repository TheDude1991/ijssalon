naw = {"voornaam" : "Harry",
       "Achternaam" : "van Winkel",
       "Geboortedatum" : "27-3-1939"
       }
for k, v in naw.items():
    print(k, v)
print(naw["voornaam"])
naw.update({"voornaam" : "Henrikus"})
for k, v in naw.items():
    print(k, v)
    
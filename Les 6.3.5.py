mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "Registratienummer" : "AA18891"
}
mijn_dictionary.pop("Geboortedatum")
print()
for k, v in mijn_dictionary.items():
    print(k, v)

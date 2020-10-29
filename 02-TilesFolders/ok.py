import os

huidige_map = os.getcwd()

alle_bestanden = os.scandir(huidige_map)

print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:
    print(bestand.name)

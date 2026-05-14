import math

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

    
def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag aan fooi per persoon is: {bedrag_pp} euro."
        
def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append("=" * len(tekst))
    return uit

def som(naam):
    v = naam.values()
    uitvoer = sum(v)
    return uitvoer
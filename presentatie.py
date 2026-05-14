def presenteer(naam, totaal):
    for item, bedrag in naam.items():
        print(f"{item} : {bedrag} euro")
    print("=" * 20)
    print(f"totaal : {totaal} euro")
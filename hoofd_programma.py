from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")

uitvoer.append("Aardbijenijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for x in uitvoer:
    print(x)
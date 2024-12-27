# Maak een dictionary Prijzen:
prijzen = {"aardbei" : 3,
           "vanille" : 4,
           "chocolade": 5}

# Voeg een variabele met naam "aanbieding" toe (0.8 van prijzen voor aardbei)
aanbieding = prijzen["aardbei"]*0.8

# Reclame tekst
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}"

# Reclame tekst 2 - waarbij decimalen in aanbieding worden gereduceerd
reclame_tekst2 = reclame_tekst[:62]

# Reclame tekst 3 - alles in hoofdletters
reclame_tekst3 = reclame_tekst2.upper()

# Reclame tekst 4 - list
reclame_tekst4 = reclame_tekst3.split()

# Alle woorden onder elkaar - enkel 5 letter of meer hoofdletters rest kleine letters
for e1 in reclame_tekst4:
    if len(e1)>=5:
        print(e1.upper())
    else: 
        print(e1.lower())
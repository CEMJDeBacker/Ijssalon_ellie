from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs - (prijs*korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = 0

    for a in inkomsten:
        totaal_inkomsten += a
    
    btw_bedrag = totaal_inkomsten * float(btw)

    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    
    hoogste_waarde = max(mijn_lijst) # Vind de hoogste waarde in de lijst
    laagste_waarde = min(mijn_lijst) # Vind de laagste waarde in de lijst

    return [hoogste_waarde, laagste_waarde]

def gemiddelde(mijn_lijst):
    
    totaal_inkomsten = 0
    for a in mijn_lijst:
        totaal_inkomsten += a
    
    aantal_bedragen = len(mijn_lijst)

    gemiddelde_inkomsten = totaal_inkomsten/aantal_bedragen

    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])

    return uitvoer
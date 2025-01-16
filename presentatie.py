def presenteer(dictionary, totaal):
        for k, v in dictionary.items():
            print(f"{k} : {v} euro")
        
        lengte = 26
        print(lengte *"=")
        totaal = 0
        totaal = sum(dictionary.values())
        print(f"Totaal : {totaal} euro")
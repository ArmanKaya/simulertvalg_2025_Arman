import random
import sys

partiene = [
    ["Arbeiderpartiet", 0, "Rød-Grønn", 0],
    ["Fremskrittspartiet", 0, "Rød-Grønn", 0],
    ["Høyre", 14.6, 0, "Blå", 0],
    ["Sosialistisk Venstreparti", 0, "Rød-Grønn", 0], 
    ["Senterpartiet", 0, "Rød-Grønn", 0],
    ["Rødt", 0, "Rød-Grønn", 0], 
    ["Miljøpartiet De Grønne", 0, "Rød-Grønn", 0],
    ["Kristelig Folkeparti", 0, "Blå", 0],
    ["Blankstemme", 0]
]



halvparti = len(partiene) // 2 # brukt til å senere skille halveis så det ikke blir en lang liste.

limit = 300 #max antall stemmer

stemmerresultat = [] #for å lagre stemmene og vise resultatene, brukte ls istedet for dic for at når jeg runner coden mer en enn gang om gangen så kan den vise forskjellige resultater.


def logstemmene(partiene):
    with open("ikkeibruk.txt", "a") as f:
        f.write(str(partiene))


def simstemme():
    antallstemt = 0
    while antallstemt < limit:
        randomvalg = round(random.uniform(1, 100),1)
        if randomvalg >= 1 and randomvalg <= 28:
            partiene[0][1] += 1
            antallstemt += 1
        elif randomvalg >= 28 and randomvalg <= 51.8:
            partiene[1][1] += 1
            antallstemt += 1
        elif randomvalg >= 51.8 and randomvalg <= 66.4:
            partiene[2][1] += 1
            antallstemt += 1   
        elif randomvalg >= 66.4 and randomvalg <= 72:
            partiene[3][1] += 1
            antallstemt += 1
        elif randomvalg >= 72 and randomvalg <= 77.6:
            partiene[4][1] += 1
            antallstemt += 1  
        elif randomvalg >= 77.6 and randomvalg <= 82.9:
            partiene[5][1] += 1
            antallstemt += 1   
        elif randomvalg >= 82.9 and randomvalg <= 87.6:
            partiene[6][1] += 1
            antallstemt += 1
        elif randomvalg >= 87.6 and randomvalg <= 91.8:
            partiene[7][1] += 1
            antallstemt += 1         
        elif randomvalg >= 91.8 and randomvalg <= 92.8:
            partiene[8][1] += 1
            antallstemt += 1  
    logstemmene(partiene)
                  
    resultatene = sorted(partiene, key=lambda x: x[1], reverse=True)   
    for i in resultatene:
        print(f"{i[0]}: {i[1]} stemmer")            






def preformvalget():
    print("") ## bruker tomme print for å gjøre outputtet mer brukervenlig.
    print("Hei, velkommen til valget 2025.")
    hvaslaks = input("press 1 hvis du vill lage ditt eget valg med dine eller vennene dine sine stemmer (10 stemmer), eller press 2 hvis du vill ha et simulert valg med 1000 stemmer.?:    ")

    if hvaslaks == "1":
        egenvalg()
    elif hvaslaks == "2":
        simstemme()
    else: 
        print("det er ikke et gyldig ett gyldig valg!")

        
preformvalget()



#alternativ solution med oddsene fra listen
"""
    ["Arbeiderpartiet", 28, 0, "Rød-Grønn"],
    ["Fremskrittspartiet", 23.8, 0, "Rød-Grønn"],
    ["Høyre", 14.6, 0, "Blå"],
    ["Sosialistisk Venstreparti", 5.6, 0, "Rød-Grønn"], 
    ["Senterpartiet", 5.6, 0, "Rød-Grønn"],
    ["Rødt", 5.3, 0, "Rød-Grønn"], 
    ["Miljøpartiet De Grønne", 4.7, 0, "Rød-Grønn"],
    ["Kristelig Folkeparti", 4.2, 0, "Blå"],
    ["Blankstemme", 0.1, 0]
"""
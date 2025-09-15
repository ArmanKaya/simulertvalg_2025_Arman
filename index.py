import random
import sys

partiene = [
    ["Arbeiderpartiet", 0],
    ["Fremskrittspartiet", 0],
    ["Høyre", 0],
    ["Sosialistisk Venstreparti", 0], 
    ["Senterpartiet", 0],
    ["Rødt", 0], 
    ["Miljøpartiet De Grønne", 0],
    ["Kristelig Folkeparti", 0],
    ["Blankstemme", 0],
    ["Andre partier", 0]
]
 

Blå = 0
Rød_Grønn = 0



halvparti = len(partiene) // 2 # brukt til å senere skille halveis så det ikke blir en lang liste.



print("Hei, velkommen til valget 2025.")
print("") #for mer bruker vennlighet





def simstemme(Blå, Rød_Grønn):
    antallstemt = 0
    simlimit = int(input("Hvor mange stemmer vil du simulere?   "))
    
    while antallstemt < simlimit:
        randomvalg = round(random.uniform(1, 100), 1)  #random uniform for å lage en float(desimaltall) mellom 1 og 100 med 1 desimal

        match randomvalg:
            case x if 1 <= x <= 28:
                partiene[0][1] += 1
                antallstemt += 1
                Rød_Grønn += 1
            case x if 28 < x <= 51.8:
                partiene[1][1] += 1
                antallstemt += 1
                Blå += 1
            case x if 51.8 < x <= 66.4:
                partiene[2][1] += 1
                antallstemt += 1
                Blå += 1
            case x if 66.4 < x <= 72:
                partiene[3][1] += 1
                antallstemt += 1
                Rød_Grønn += 1
            case x if 72 < x <= 77.6:
                partiene[4][1] += 1
                antallstemt += 1
                Rød_Grønn += 1
            case x if 77.6 < x <= 82.9:
                partiene[5][1] += 1
                antallstemt += 1
                Rød_Grønn += 1
            case x if 82.9 < x <= 87.6:
                partiene[6][1] += 1
                antallstemt += 1
                Rød_Grønn += 1
            case x if 87.6 < x <= 91.8:
                partiene[7][1] += 1
                antallstemt += 1
                Blå += 1
            case x if 91.8 < x <= 92.8:
                partiene[8][1] += 1
                antallstemt += 1
            case x if 92.8 < x <= 100:
                partiene[9][1] += 1
                antallstemt += 1


    print("Valget er ferdig, her er resultatene:    ") 
  

    print("")# igjen for bruker vennlighet
    
            
    def beregnmandater():
        antall_mandater = 169
        
        for navn, stemmer in partiene:
            prosentpoeng = stemmer / simlimit * 100 #formelen for regne prosent poeng
            mandater = round(stemmer / simlimit * antall_mandater) #formel for fordeling mandater
            
            if navn in ["Blankstemme", "Andre partier"]:
                print(f"{navn}: | {prosentpoeng:.2f}% prosentpoeng | stemmer: {stemmer}")  #dersom navnet er lik blankstemme eller andre partier printer den ikke mandater
                
            else:
                print(f"{navn}: {mandater} mandater | {prosentpoeng:.2f}% prosentpoeng | stemmer: {stemmer}") #printer prosentpoeng med 2 desimaler

        



        
    
    if Blå > Rød_Grønn:
            print(f"Det ble blå seier med {Blå} stemmer totalt, mens det ble tap på Rød Grønn side med {Rød_Grønn}  stemmer.")
    elif Rød_Grønn > Blå:
            print(f"Det ble rød-grønn seier med {Rød_Grønn} stemmer totalt, mens det ble tap på Blå med {Blå} stemmer.")

    beregnmandater()
    
    def logstemmene(partiene, Rød_Grønn, Blå):
        with open("logs.txt", "a") as f:
            f.write(str(partiene)) #log partiene
            f.write(f"\n Rød-Grønn: {Rød_Grønn}, Blå: {Blå}\n") #log hvilken side som fikk mest stemmer
    logstemmene(partiene, Rød_Grønn, Blå)            

simstemme(Blå, Rød_Grønn)

 



#alternativ solution med oddsene fra listen ikke i bruk i denne koden
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

"""  dersom jeg senere implementerer ett valg der man kan inputte egne stemmer istedet for simulert valg

def preformvalget():
    print("") 
    print("Hei, velkommen til valget 2025.")
    hvaslaks = input("press 1 hvis du vill lage ditt eget valg med dine eller vennene dine sine stemmer (10 stemmer), eller press 2 hvis du vill ha et simulert valg der du kan velge antall stemmer?:    ")

    if hvaslaks == "1":
        print("ikke klar")
    elif hvaslaks == "2":
        simstemme(Blå, Rød_Grønn)
    else: 
        print("det er ikke et gyldig ett gyldig valg!")
        preformvalget()

        
preformvalget()
"""
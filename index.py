import random


partiene = [
    ["1. Arbeiderpartiet", 0],
    ["2. Fremskrittspartiet", 0],
    ["3. Høyre", 0],
    ["4. Sosialistisk Venstreparti", 0], 
    ["5. Senterpartiet", 0],
    ["6. Rødt", 0], 
    ["7. Miljøpartiet De Grønne", 0],
    ["8. Kristelig Folkeparti", 0],
    ["9. Blankstemme", 0],
    ["10. Andre partier", 0]
]
 


# legg på nummerering



Blå = 0
Rød_Grønn = 0



halvparti = len(partiene) // 2 # brukt til å senere skille halveis så det ikke blir en lang liste.





def logstemmene(partiene, Rød_Grønn, Blå):
    with open("logs.txt", "a") as f:
        f.write(str(partiene)) #log partiene
        f.write(f"\n Rød-Grønn: {Rød_Grønn}, Blå: {Blå}\n") #log hvilken side som fikk mest stemmer
logstemmene(partiene, Rød_Grønn, Blå)            


def simstemme(Blå, Rød_Grønn):
    antallstemt = 0
    simlimit = int(input("Hvor mange stemmer vil du simulere?   "))
    
    while antallstemt < simlimit:
        randomvalg = round(random.uniform(1, 100), 1)  #random uniform for å lage en float(desimaltall) mellom 1 og 100 med 1 desimal

        #match case er brukt for å slippe å repetere elif og er visuelt bedre og man slipper å skrive variabel navn og blir generelt ryddigere.
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
    
               
    #beregner mandater og prosenten  
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

    with open("logs.txt", "a") as f:
        f.write("dette er et bruker styrt valg \n")
    logstemmene(partiene, Blå, Rød_Grønn)

    

#egen valg hvor brukeren eller flere mennesker stemmer
def egenvalg(partiene, Blå,Rød_Grønn):
    antallstmt = 0
    antlstmr = int(input("hvor mange er dere som skal stemme?   "))
    print("")
    print(partiene[:halvparti])
    print(partiene[halvparti:])

    

    #under her er der selve valget skjed
    while antallstmt < antlstmr:
        velgparti = int(input("Vennligst skriv tallet ved siden av navnet til partiet du vill stemme.   "))
        print("")
        
        if 1 <= velgparti <= 10:
                print("stemme registrert \n")
                print(partiene[:halvparti])
                print(partiene[halvparti:])
                partiene[velgparti - 1][1] += 1 #basert på valg legger den til i den indeksen
                antallstmt += 1
        elif velgparti > 10 or velgparti < 1:
                print("dette er ett ugyldig tall vennligst velg ett tall fra listen")

        #sjekker om det er blått eller rødt-grønt parti
        if velgparti == 2 or velgparti == 3 or velgparti == 8:
            Blå += 1
        elif velgparti == 1 or velgparti > 3 and velgparti < 8:
            Rød_Grønn += 1  

    if Blå > Rød_Grønn:
        print(f"Det ble blå seier med {Blå} stemmer totalt, mens det ble tap på Rød Grønn side med {Rød_Grønn}  stemmer.")
    elif Rød_Grønn > Blå:
        print(f"Det ble rød-grønn seier med {Rød_Grønn} stemmer totalt, mens det ble tap på Blå med {Blå} stemmer.")

  

    #for å holde litt orden i logsene
    with open("logs.txt", "a") as f:
        f.write("dette er et bruker styrt valg \n")
    logstemmene(partiene, Rød_Grønn, Blå)


    #beregner mandater og prosenten
    def beregnegenmandater():
        antall_mandater = 169
        for navn, stemmer in partiene:
            prosentpoeng = stemmer / antlstmr * 100 #formelen for regne prosent poeng
            mandater = round(stemmer / antlstmr * antall_mandater) #formel for fordeling mandater

            if navn in ["Blankstemme", "Andre partier"]:
                print(f"{navn}: | {prosentpoeng:.2f}% prosentpoeng | stemmer: {stemmer}")  #dersom navnet er lik blankstemme eller andre partier printer den ikke mandater
                
            else:
                print(f"{navn}: {mandater} mandater | {prosentpoeng:.2f}% prosentpoeng | stemmer: {stemmer}") #printer prosentpoeng med 2 desimaler
    beregnegenmandater()
   

#gjennomføre valget sånn at brukeren kan velge om de skal ha simulert eller brukertstyrt valg.
def preformvalget():
    print("") 
    print("Hei, velkommen til valget 2025.")
    hvaslaks = input("press 1 hvis du vill lage ditt eget valg med dine eller vennene dine hvor du styrer hvor mange som skal stemme, eller press 2 hvis du vill ha et simulert valg der du kan velge antall stemmer?:    ")

    if hvaslaks == "1":
        egenvalg(partiene, Blå, Rød_Grønn)
    elif hvaslaks == "2":
        simstemme(Blå, Rød_Grønn)
    else: 
        print("det er ikke et gyldig ett gyldig valg!")
        hvaslaks = input("press 1 hvis du vill lage ditt eget valg med dine eller vennene dine sine stemmer (10 stemmer), eller press 2 hvis du vill ha et simulert valg der du kan velge antall stemmer?:    ")
        if hvaslaks == "1":
            egenvalg(partiene, Blå, Rød_Grønn)
        elif hvaslaks == "2":
            simstemme(Blå, Rød_Grønn)
        

preformvalget()

 



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


preformvalget()
"""

partinavn = ["1. Arbeiderpartiet", "2. fremskrittspartiet", "3. høyre", "4. sosialistisk venstreparti \n", 
             "5. Senterpartiet", "6. Rødt", "7. Miljø parti de grønne", "8. Kristelig Folkeparti"]









def stemme():
    with open("stemmer.txt", "a") as f:
        stemmernavn = input("Hva heter du?  ")
        valg = input("hvem vill du stemme:  ") 
        f.write(valg + "\n")

def valgresultat():
    with open("stemmer.txt", "r") as file:
        stemmersum = file.read()
        print(stemmersum)


stemme()
valgresultat()
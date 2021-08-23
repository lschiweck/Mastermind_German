#main-Spiel | Lennart Schiweck | Hoschschule Reutlingen | Endabgabe
import itertools
import random

steck_platze = 4

def farben_checker(a,b):
    a = list(a)
    b = list(b)
    richtige_stelle = 0
    richtige_farbe = 0
    #Berechnung der richtigen farben und stellen 
    for i in range(steck_platze):                                                                                      
        if(a[i] == b[i]):                                                                            
            richtige_stelle +=1                                                                                             
        if(a[i] in b and a[i]!=b[i]):           #if Zahl in b ist aber nicht in der selben stelle von b
            if(a.count(a[i])<=b.count(a[i])):   #wird uberpruft ob mehr von der Zahl in a oder b ist
                richtige_farbe+=1               
            elif(a.count(a[i])>b.count(a[i])):  #falls in a mehr sind wird diese Zahl aus der temp liste rausgeloscht
                a[i] = 0
    return richtige_farbe,richtige_stelle

def variante_1():
    
    farben_auswahl = list(itertools.product(range(1,9), repeat = 4))
    farbe = random.choice(farben_auswahl)
    #Dictionary der Farben
    farb_code = {1:"Rot", 2:"Gelb", 3:"Blau", 4:"Schwarz", 5:"Weis", 6:"Pink", 7: "Orange", 8:"Lila"}
    pc_farben = []
    runde = 1
    print(farbe) #Zum Testen ansonsten, falls man wirklich spielen moechte entfernen
    for i in range(steck_platze):
        pc_farben.append(farb_code[farbe[i]])

    while(runde<13):

        auswahl = []
        print("\n#########################################")
        print("\t\trunde:",runde)
        print("#########################################")
        print("\n[1=Rot | 2=Gelb | 3=Blau | 4=Schwarz | 5=Weis | 6=Pink | 7=Orange | 8=Lila]")
        
        #es wird solange der Name abgefragt bis er korrekt eingegeben wurde
        running = True
        while running:                                                                                              
            try:                                                                                                
                auswahl = list(map(int,input("\nGib deine 4 farben ein : ").strip().split()))[:4]                                                                                                             
                if(len(auswahl)!=4 or max(auswahl)>8 or min(auswahl)<1):                                           
                    raise ValueError         
            #es entsteht ein Valuerror Eingabe muss wiederholt werden.                                                                      
            except:
                print("Fehlerhafte Eingabe! Bitte gib 4 Zahlen zwischen 1 und 8 ein. Getrennt mit einem Leerzeichen.")            
            else:
                running = False                                                                                           

        echte_farbe = []   #ist die Farbe die der Spieler ausgewahlt hat in rihtigen Farben
        for i in range(steck_platze):                                                                                      
            echte_farbe.append(farb_code[auswahl[i]])
        #gewinnbedinnung dann revanche                                                                          
        if(auswahl==list(farbe)):
            print("#########################################")
            print("\t!!!DU HAST GEWONNEN!!!")
            print("#########################################")
            print("\nDie farben sind",*pc_farben, sep=" | ", end=" | ")
            revanche()
        #uberpruefung richtiger Farben und ausgabe von Farbwerten.
        richtige = farben_checker(auswahl,farbe)
        print("Deine Eingabe: ",*echte_farbe, sep=" | ", end=" |\n")
        print(f"\nrichtige farben an der Falschen Position: {richtige[0]} \nrichtige farben an der richtigen Position: {richtige[1]}\n")
        
        runde +=1
    #12 Runden vorbei Spieler verliert dann revanche
    print("\nDu hast leider verloren :( ")
    print("\nDie farben sind",*pc_farben, sep=" | ", end=" | ")
    revanche()        
    
def variante_2():
    
        farben_moglichkeiten = list(itertools.product(range(1,9), repeat = 4))
        runde = 1

        print("\n#########################################")
        print("\n[1=Rot | 2=Gelb | 3=Blau | 4=Schwarz | 5=Weis | 6=Pink | 7=Orange | 8=Lila]")
        print("\nDer Computer wird deine farben Kombination erraten ;)\nRS = Richtige Stelle | RF = Richtige Farbe")
        #selbe wie bei Variante1 nur das dies das Suchfeld ist
        running = True
        while running:                                                                                              
            try:                                                                                                
                auswahl = list(map(int,input("\nGib deine 4 farben ein : ").strip().split()))[:4]                                                                                                             
                if(len(auswahl)!=4 or max(auswahl)>8 or min(auswahl)<1):                                           
                    raise ValueError                                                                               
            except:
                print("Fehlerhafte Eingabe! Bitte gib 4 Zahlen zwischen 1 und 8 ein.")            
            else:
                running = False 
                
        while(runde<12):
            
            rnd = []   
                     
            if(runde==1):
                rnd = random.sample(range(1,9),steck_platze)
            else:
                rnd = random.choice(farben_moglichkeiten)
            
            ubereinstimmung = farben_checker(rnd,auswahl)
            print(f'runde: {runde}  Moeglichkeiten: {len(farben_moglichkeiten)}')
            print("Ich glaube es ist: ", *rnd,)
            print(f'RS: {ubereinstimmung[0]} RF: {ubereinstimmung[1]}\n')
            #Listenreduktionsfunktion, vergleicht jede Moglichkeit mit den Richtig-Werten des Echten ergebnis und der Listenmoglichkeiten
            farben_moglichkeiten = [moglichkeit for moglichkeit in farben_moglichkeiten if farben_checker(rnd, moglichkeit) == ubereinstimmung]  
            #Gewinnbedingung rnd ist aber keine liste,deshalb kann es nur mit list() verglichen werden                          
            if(auswahl==list(rnd)):
                print("Die farben sind",*rnd)
                revanche() 
            runde+=1
            
def revanche():
    #Eingabe mit j/n ob Revanche, wenn eingabe nicht wenigsten J/j oder N/n, ruft es sich nochmal auf
    nochmal = input("\nrevanche? (J/N):")                                                                   
    if(not(nochmal.lower()=="j" or nochmal.lower()=="n")):                                                       
        print("Bitte nochmal eingeben(nur J/N)\n")
        revanche()
        
    if(nochmal.lower() == "j"):
        print("\n" * 100)                                                                                        
        main()
    elif(nochmal.lower() == "n"):
        print("Vielen danke furs mainen!")
        quit()

def main():      
    
    print("\tStarting...Mastermind")
    print("#########################################")
    #abfrage welche Variante, bei Fehlern wiederholung
    running = True
    while(running):
        try:
            variant = int(input("\nMoechtest du entweder 1. farben erraten oder 2. farben waehlen:"))
            if(not(variant==1 or variant==2)):
                raise ValueError
        except:
            print("Fehlerhafte Eingabe! Bitte einer der Beiden variantn waehlen (1|2)")
        else:
            running = False
    if(variant==1):
        variante_1()
    elif(variant==2):
        variante_2()
        
if __name__ == "__main__":
    main()  
from random import randint
from random import random
import re
while True:
    otazka=input("Vítáme vás. Zadejte 1 pro validátor, 2 pro generátor ")
    if otazka == "1" or otazka == "2":
        break
    else:
        print("Zadejte prosím buď 1 pro velidátor, nebo 2 pro generátor")
        
if otazka=="2":
    pismena = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
               "o","p","q","r","s","t","u","v","w","x","y","z"]
    velka_pismena = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    znaky = ["%", "&", "+", "/" , "-", "*", "|", "$" , "^", "_","!", "?"]
    cislo = ["1","2","3","4","5","6","7","8","9","0"]
    dohromady = [pismena, velka_pismena, cislo , znaky]
    final = []
    pocet_mist = int(input("Zadejte počet míst: "))
    heslo =  pocet_mist * [" "]
    otazky = ["Přejte si zakomponovat malá písmena?(Ano/Ne): ", "Přejete si zakomponovat velká pismena?(Ano/Ne) ","Přejete si zakomponovat cisla?(Ano/Ne):", "Přejete si zakomponovat znaky?(Ano/Ne): "]
    vstupy = ["vstup_pismena" , "vstup_velka_pismena" , "vstup_cisla" , "vstup_znaky"]
    bez = ["písmen" , "velkých písmen" , "čísel" , "znaků"]
    
    for i in range (4):
        vstupy[i] = input(otazky[i])
        if vstupy[i] == "Ano":
            final.append(dohromady[i])
        else:
            print("Bez " + bez[i] )
            
    if vstupy[0] == "Ne" and vstupy[1] =="Ne" and vstupy[2] =="Ne" and vstupy[3] =="Ne":
        print("Musíš zadat alespoň jednou ano!")
        exit()
        
    for i in range (pocet_mist):
        r = randint(0,len(final)-1)
        seznam = final[r]
        heslo[i] = seznam[randint(0,len(seznam)-1)]        
    print("".join(heslo))
else:
    while True:
        validace = input("Zadejte vaše heslo: ")
        delka_validace=len(validace)
        if delka_validace <5:
            print("Heslo příliš krátké!\nZadejte delší!")
        else:
            break
        
    search_obj=re.search(r'[a-zA-Z0-9]+[% & + / - * | $ ^ _! ?]',validace)
    if search_obj:
        print("Gratulujeme, vaše heslo je dostatečně silné.")
    else:
        print("Vaše heslo je příliž slabé... Pro posílení použijte kombinaci velkých i malých písmen, čísla, nebo speciální znaky.")

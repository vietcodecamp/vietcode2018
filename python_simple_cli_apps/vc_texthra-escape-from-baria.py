import random
import time

def konec_hry():
    print("GAME OVER\n")
    ukonceni = input("Přeješ si ukončit hru? ANO/NE \n").upper()
    while True:
        if ukonceni == "ANO":
            quit()
        elif ukonceni == "NE":
            ridici_mistnost()

def ridici_mistnost():
    global zivoty
    zivoty = 3
    global inventar
    inventar.clear()
    print("Tvoje lokace: řídící místnost.\n")
    time.sleep(1)
    print("Vidíš před sebou 2 východy. Jeden vede na východ a jeden na západ. Směrem na východ víš, že se nachází zbrojnice a směrem na západ skladiště.\n")
    print("Pokud chceš jít na východ zadej: VÝCHOD pokud na západ zadej: ZÁPAD.\n")
    otazka="Zadej instrukci: ZÁPAD/VÝCHOD: "
    moznosti=["ZÁPAD","VÝCHOD"]
    jmena_funkci=[mistnost_a, mistnost_b]
    ziskej_vstup_a_vyber_moznost(otazka,moznosti,jmena_funkci)

def mistnost_a(): #skladiště
    print("Tvoje lokace: skladiště.\n")
    time.sleep(1)
    print("Západní chodba tě dovedla přímo do skladiště. V místnosti vidíš brnění, ale v cestě k němu na tebe mohou čekat četná nebezpečí.\n")
    odpoved=input("Chceš se vydat pro brnění? ANO/NE: ").upper()
    global inventar
    if odpoved == "ANO":
        print("\nMístnost jsi přešel bez jakékoliv úhony a získal jsi brnění, toto brnění ti pomůže na tvé cestě za svobodou. ")
        time.sleep(2)
        print("Brnění snižuje šanci nepřítele tě zasáhnout.\n")
        inventar.append("brnění")
        print("Máš u sebe: "+ ", ".join(inventar))
    else:
        print("\nRozvážně ses rozhodl pokračovat ve své cestě.\n")
    time.sleep(1)
    print("Nyní máš možnost jít do ubytovacích prostorů nebo na hlavní palubu.\n")
    otazka="Zadej instrukci: UBYTOVNA/PALUBA: "
    moznosti=["UBYTOVNA","PALUBA"]
    jmena_funkci=[mistnost_g, mistnost_h]
    ziskej_vstup_a_vyber_moznost(otazka,moznosti,jmena_funkci)

def mistnost_g(): #ubytovna
    print("Tvoje lokace: ubytovna.\n")
    time.sleep(1)
    print("Vidíš stůl s občerstvením, můžeš se najíst a doplnit sílu nebo pokračovat v cestě.\n")
    odpoved=input("Chceš se najíst? ANO/NE: ").upper()
    global zivoty
    if odpoved == "ANO":
        sance = random.random()
        if sance > 0.5:
            zivoty+=1
            print(f"Snědl jsi závitky, které ti zvýšily výdrž. Počet životů: {zivoty}")
        else:
            zivoty-=1
            if zivoty < 1:
                konec_hry()
            print(f"Bohužel jídlo bylo otrávené, pozvracel ses a tvoje výdrž značně utrpěla. Počet životů: {zivoty}")
    else:
        print("\nRozhodl ses hladovět.\n")
    print("Pokračuješ ve své cestě.\n")
    time.sleep(1)
    mistnost_i()

def mistnost_h(): #paluba
    print("Tvoje lokace: hlavní paluba.\n")
    time.sleep(1)
    print("Ocitl ses na hlavní palubě lodi. Všímáš si, že na palubě je světelný shuriken, ale je rozbitý.\n")
    odpoved=input("Chceš ho opravit? ANO/NE: ").upper()
    global inventar
    if odpoved == "ANO":
        sance=random.random()
        if sance < 0.4:
            print("Jsi šikovný, opravil jsi shuriken. Zvyšuje šanci zasáhnout nepřítele.\n")
            inventar.append("SHURIKEN")
            print("Máš u sebe: "+ ", ".join(inventar))
        else:
            print("Jsi nešika, nenávratně jsi poškodil shuriken.\n")            
    print("\nPokračuješ dále do knihovny\n")
    time.sleep(1)
    mistnost_i()

def mistnost_i(): #knihovna
    global zivoty
    global inventar
    print("\nTvoje lokace: knihovna\n")
    time.sleep(1)
    print("Vešel jsi do knihovny. Všímáš si, že tu nejsi sám, před tebou stojí mudrc rasy Uchiha, nezdá se, že by ti umožnil průchod.")
    print("Tvá jediná možnost na přežití je souboj! Zvol si svoji taktiku boje.\n")
    instrukce="Zadej instrukci: TAIJUTSU/DÝKA/OKO/SHURIKEN "
    enemy_zivoty = 4
    vyhra = souboj(enemy_zivoty,zbrane_moznosti,instrukce,sance) #Zavola funkci souboj, da do funkce zivoty nepritele, vsechny zbrane, instrukci a sance jednotlivych zbrani
    if vyhra == False: #Zkontroluje jestli hrac prohral
        konec_hry()
    print("Víš, že Uchiha má velice mocné oko, chceš se pokusit jeho schopnost přivlastnit?")
    odpoved=input("Chceš se o to pokusit? ANO/NE: ").upper()
    if odpoved == "ANO":
        random_oko=random.random()
        if random_oko < 0.15:
            print("Jsi talentovaný rytíř a přivlastnil sis schopnosti Uchihy. Oko ti dá neuvěřitelné schopnosti.\n")
            inventar.append("OKO")
            print("Máš u sebe: "+ ", ".join(inventar))
            time.sleep(2)
        else:
            print("Nepodařilo se ti oko vyjmout bez poškození a ztratil jsi svoji příležitost.")
            zivoty-=1
            print(f"Byl jsi proklet. Počet životů: {zivoty}")
            time.sleep(2)
            if zivoty < 1:
                konec_hry()
    print("\nJsi skoro na konci cesty a pokračuješ dál\n")
    time.sleep(1)
    mistnost_e()

def ziskej_vstup_a_vyber_moznost(otazka, moznosti, jmena_funkci):
    #otazka = Zadej instrukci...
    #moznosti = ZBROJNICE/STROJÍRNA etc.
    #jmena_funkci = mistnost_c etc.
    while True:
        smer = input(otazka).upper() #Opakuje se dokud neni spravna odpoved
        if smer in moznosti:
            index = moznosti.index(smer) #Zjisti index odpovedi uzivatele v listu moznosti
            jmena_funkci[index]() #Zavola funkci
        else:
            print("\nNeplatná instrukce.")

def souboj(enemy_zivoty,zbrane_moznosti,instrukce,sance):
    global inventar
    global zivoty
    global fraze_zbrane
    index=0
    while True: #opakuje se dokud uzivatel nezada styl souboje ktery je dostupny
        zbran=input(instrukce).upper()
        if zbran in inventar:
            index = zbrane_moznosti.index(zbran) #Zjisti index zbrane ktery si uzivatel vybral
            pravdepodobnost = sance[index] #Pravdepodobnost zbrane[0] je sance[0] ...
            break
        elif zbran == "TAIJUTSU":
            pravdepodobnost = sance[0]
            break
        else:
            print("Tento předmět/schopnost nemáš k dispozici")
    if "brnění" in inventar: #Zkonstroluje zda je brneni v inventari
        pravdepodobnost -= 0.1
        print("Máš na sobě brnění, je menší šance, že te nepřítel fatálně zasáhne.\n")
    print(fraze_zbrane[index]) #Napise frazi zbrane
    while True: #Souboj probiha dokud nezemre bud hrac nebo nepritel
            sance = random.random()
            if sance > 0.5:
                enemy_zivoty -= 1
                time.sleep(2)
                print(f"Zasáhl jsi, nepříteli zbývá {enemy_zivoty} životů\n")
            if sance < pravdepodobnost:
                zivoty -= 1
                time.sleep(2)
                print(f"Utrpěl jsi zásah, zbývá ti {zivoty} životů\n")
            if zivoty < 1:
                vyhra = False
                return vyhra #Vrati false pokud zemre hrac
            elif enemy_zivoty < 1:
                vyhra = True
                return vyhra #Vrati true pokud zemre nepritel      
    

def mistnost_b(): #východní chodba
    print("Tvoje lokace: východní chodba.\n")
    time.sleep(1)
    print("V chodbě jsi si všimnul otevřeného poklopu, který vede do strojírny - slyšíš podivné zvuky.\n")
    print("Můžeš se rozhoudnout zda-li chceš pokračovat do zbrojnice, prozkoumat strojírnu nebo se vrátit.\n")
    otazka="Zadej instrukci: ZBROJNICE/STROJÍRNA/VRÁTIT SE: "
    moznosti=["ZBROJNICE","STROJÍRNA","VRÁTIT SE"]
    jmena_funkci=[mistnost_d, mistnost_c, ridici_mistnost]
    ziskej_vstup_a_vyber_moznost(otazka,moznosti,jmena_funkci)

def mistnost_c(): #strojírna
    print("Tvoje lokace: strojírna.\n")
    time.sleep(1)
    print("Ve strojírně na tebe zaútočil Uchiha.\n")
    sance = random.random()
    if sance < 0.75:
        print("Uchiha tě zabil pomocí amaterasu.\n")
        konec_hry()
    else:
        print("Tvé schopnosti tě zachánily, unikl jsi ze strojírny zpátky do chodby.\n")
        time.sleep(3)
        mistnost_b()

def mistnost_d(): #zbrojnice
    print("Tvoje lokace: zbrojnice.\n")
    time.sleep(1)
    print("Nacházíš zraněného, infikovaného vojáka, který u sebe může mít užitečný předmět. Můžeš ho prohledat, ale hrozí riziko nákazy.\n")
    odpoved=input("Chceš prohledat vojáka? ANO/NE: ").upper()
    if odpoved == "ANO":
        print("\nProhledal jsi vojáka a našel jsi zbraň. Zvyšuje šanci na zasáhnutí nepřítele.\n")
        global zivoty #Umožňuje práci s globální proměnnou
        sance_nakazy = random.random()
        if sance_nakazy < 0.4:
            zivoty-=1
            print(f"Byl jsi infikován, nakáza ti ubrala 1 život. Počet životů: {zivoty}")
        else:
            print(f"Nenakazil ses. Počet životů: {zivoty}")
        if zivoty < 1:
            konec_hry()
        inventar.append("DÝKA")
        print("Máš u sebe: "+ ", ".join(inventar))
    print("\nNyní máš dvě možnosti, vydat se směrem doleva šachtou nebo pokračovat rovně chodbou.\n")
    otazka="Zadej instrukci: DOLEVA/ROVNĚ: "
    moznosti=["DOLEVA","ROVNĚ"]
    jmena_funkci=[mistnost_h
                  , mistnost_e]
    ziskej_vstup_a_vyber_moznost(otazka,moznosti,jmena_funkci)

def mistnost_e(): #hangár
    print("Tvoje lokace: hangár\n")
    time.sleep(1)
    print("Vcházíš do místnosti a okamžitě se za tebou zavřou dveře, před tebou se objeví vůdce Uchiha rasy, který brání ke vstupu do modulu.\n")
    print("Vyber jak a s čím budeš bojovat.")
    instrukce="Zadej instrukci: TAIJUTSU/DÝKA/OKO/SHURIKEN "
    enemy_zivoty = 5
    vyhra = souboj(enemy_zivoty,zbrane_moznosti,instrukce,sance) #Zavola funkci souboj, da do funkce zivoty nepritele, vsechny zbrane, instrukci a sance jednotlivych zbrani
    if vyhra == True: #Vyhra je boolean, ktery se ziska z funkce souboj
        win()
    else:
        konec_hry()
    

def win(): #pokud uzivatel vyhraje
    print("Dostal jsi se k modulu a úspěšně jsi unikl.")
    print(f"Gratulujeme k výhře {jmeno}!")
    time.sleep(3)
    ukonceni = input("Chceš hrát znova? Zadej: ANO/NE ").upper()
    while True:
        if ukonceni == "NE":
            quit()
        elif ukonceni == "ANO":
            ridici_mistnost()
     

def kontrola_itemu(item, mistnost):#kontrola zda jsou predmety k dispozici #mistnost = jakou funkci znova zavolat pokud je spatna instrukce
    try:
        return inventar.index(item)
    except ValueError:
        print(f"\n{item} není k dispozici.\n")
        time.sleep(2)
        mistnost()

def main():# zacatek
    zahajeni_hry=input("Pro zahájení hry zadej START: ").upper()
    if zahajeni_hry=="START":
        jmeno=input("Zadej své jméno uživateli: ")
        print(f"Vítej ve hře: Escape from Baria, {jmeno}!\n")
    else:
        print("Konec hry")
        quit()
    #Začátek příběhu
    time.sleep(2)
    print(f"V nedaleké galaxii se hvězdný rytíř {jmeno} nachází na vesmírné lodi Baria, která byla právě napadena krvežíznivou rasou Uchiha.")
    print("Jediná možnost jak přežít je dostat se do hangáru s únikovým modulem. Tvá startovní pozice je v řídící místnosti.\n")
    time.sleep(5)
    print(f"Počet životů: {zivoty}")
    print("Máš u sebe: "+ ", ".join(inventar))
    ridici_mistnost() #Vyvolá 1. místnost
inventar=[]
zbrane_moznosti=["TAIJUTSU","DÝKA","OKO","SHURIKEN"]
sance=[0.4,0.3,0.1,0.2]
fraze_zbrane=["\nRozbíháš se a připravuješ se na svůj mocný úder.\n","\nRozbíháš se a připravuješ se na seknutí.\n","\nTvoje nové oko ti umožní uvolnit neuvěřitelnou sílu!\n","\nZaměřuješ svého nepřítele\n"]
zivoty=3
jmeno=""
if __name__ == "__main__":
    main()

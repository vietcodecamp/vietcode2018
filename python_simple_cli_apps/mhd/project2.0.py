#import časových funkcí
import time
#import ASCII mapy ze souboru (verze lite)
import mapa
#import souboru s jízdními řády
import jizdnirady
#import funkcí pro manipulaci s obrázky(full verze), je třeba nainstalovat Pillow library!
from PIL import Image
import easteregg

#DEFINICE FCÍ:

def ziskat_zastavky(seznam_linek):
    vsechny_zastavky = []
    for zastavky in seznam_linek.values():
        for stop in zastavky.keys():
            vsechny_zastavky.append(stop)
    return vsechny_zastavky
    #vyhodí seznam zastávek na všech linkách

def zastavky_v_lince(linka):
    zastavky_v_lince = []
    for zastavky in linka.keys():
        zastavky_v_lince.append(zastavky)
    return zastavky_v_lince
    #vyhodi seznam zastávek na jedné lince

def prevod_na_minuty(cas):
    #kontrolujeme správný formát zadaného času
    if ":"in cas:
        cas=cas.split(":")
    else:
        return False
    if cas[0].isdigit()==False or cas[1].isdigit()==False:
        return False
    if int(cas[0])<24 and int(cas[1])<60:
        pocet_minut=int(cas[0])*60+int(cas[1])
        return pocet_minut
    else:
        return False
    #pokud jsou všechny podmínky splněné převede zadaný čas ve formátu HH:MM na počet minut
    
def najit_prime_spoje(odkud,kam):
    nalezle_prime_spoje=[]
    destinace=[]
    prime_spoje=[]
    destinace2=[]
    boolean=False
    #prohledává linky
    for linka, zastavky in jizdnirady.seznam_linek.items():
        #pokud je jak zastavka odkud, tak zastavka kam na lince
        if odkud in zastavky and kam in zastavky:
            #vytvoříme seznam zastávek na lince, aby každá zastávka měla index, který můžeme porovnávat
            seznam_zastavek = zastavky_v_lince(zastavky)
            #porovnáváme index zastávky odkud a kam pro urceni směru
            if seznam_zastavek.index(odkud) < seznam_zastavek.index(kam):
                #vkládáme do seznamu odjezdů a seznamu příjezdů vhodné spoje
                for x in range(len(zastavky[odkud])):
                    #pokud je spoj pozdější než zadaný čas, uloží se do seznamu nelezle_prime_spoje
                    if prevod_na_minuty(zastavky[odkud][x])>v_kolik:
                        nalezle_prime_spoje.append([f"{linka} ve směru {seznam_zastavek[-1]}:\nodjezd z {odkud}: ",zastavky[odkud][x]])                  
                        destinace.append([f"příjezd na zastávku {kam}: ",zastavky[kam][x]])
                        boolean=True
                    destinace2.append([f"příjezd na zastávku {kam}: ",zastavky[kam][x]])
                    prime_spoje.append([f"{linka} ve směru {seznam_zastavek[-1]}:\nodjezd z {odkud}: ",zastavky[odkud][x]])
    return boolean,nalezle_prime_spoje,prime_spoje,destinace,destinace2
    #fuknce vyhodí boolean, zda existují spoje pozdější než zadaný čas, pokud ano, uloží tyto spoje do seznamu: nalezle_prime_spoje a destinace
    #dále vytvoří seznam veškerých spojů-odjezdů(prime_spoje) a příjezdů do destinace(destinace2)
     

def trideni_tisk_linek(spoje,destinace):
    nalezle_prime_spoje.sort(key=lambda x: x[1])
    destinace.sort(key=lambda x: x[1])
    for index in range(len(spoje)):
        odjezd=" ".join(spoje[index])
        prijezd=" ".join(destinace[index])
        print(f"{odjezd}")
        print(f"{prijezd}\n")       
    #chronologicky seřadí časy, ve kterých bude linka na zastávce odkud a kdy přijede na zastávku kam, a vytiskne spoje
#-----------------------------------------------------------------------------------------------------------#
verze=input("Přejete si zobrazit a)plnou či b)lite verzi? ")
while True:
    if verze.lower()=="a":
        mapa=Image.open("mapa.jpg")#testovaci obrazek, mapa ještě není hotová
        mapa.show()
        break
    elif verze.lower()=="b":
        print(mapa.CHEPRANOJ)
        break
    else:
        verze=input("Zadejte a pro plnou verzi, b pro lite verzi: ") 
odkud = input("Zadej odkud (bez diakritiky): ")
odkud=odkud.upper()
kam = input("Zadej kam (bez diakritiky): ")
kam=kam.upper()
v_kolik=input("Zadejte čas odjezdu (TEĎ nebo čas ve formátu HH:MM): ")
#vytvorime si seznam vsech zastavek
vsechny_zastavky = ziskat_zastavky(jizdnirady.seznam_linek)
while True:
    easteregg.easteregg(odkud,kam,v_kolik)
    if odkud not in vsechny_zastavky:
         odkud = input(f"Zastávka '{odkud}' neexistuje, zadejte jinou: ").upper()
         continue
    if kam not in vsechny_zastavky:
         kam = input(f"Zastávka '{kam}' neexistuje, zadejte jinou: ").upper()
         continue
    if v_kolik.upper()=="TEĎ" or v_kolik.upper()=="TED":
         cas=time.localtime()
         v_kolik=cas.tm_hour*60+cas.tm_min
    elif prevod_na_minuty(v_kolik)==False:
         v_kolik=input("Zadejte správný formát času!(TEĎ nebo čas ve formátu HH:MM): ")
         continue
    else:
        v_kolik=prevod_na_minuty(v_kolik)
    boolean,nalezle_prime_spoje,prime_spoje,destinace,destinace2=najit_prime_spoje(odkud,kam)
    if nalezle_prime_spoje != []or prime_spoje!=[]:
        if boolean==False:
            print("Existují jen spoje na následující den!\n")
            trideni_tisk_linek(prime_spoje,destinace2)
            break
        else:
            trideni_tisk_linek(nalezle_prime_spoje,destinace)
            break
    else:
        print("Neexistuje přímý spoj!")
        break
       
        




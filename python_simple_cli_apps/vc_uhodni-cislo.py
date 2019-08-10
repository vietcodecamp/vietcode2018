from random import randint
import math
import os



def gamble(penize, rnd_cislo, porovnavani, krok, hadaci_cislo):
    while True:
        os.system(sys_clr)
        print(f"máš \x1B[32m{penize}\x1B[0m dongů a číslo je \x1B[34m{porovnavani}\x1B[0m než \x1B[32m{hadaci_cislo}\x1B[0m")
        print(f"Hádáš mezi \x1B[32m{min} až \x1B[32m{max}\x1B[0m")
        hadaci_cislo = int(input("Hádej číslo: "))
        krok += 1
        if rnd_cislo == hadaci_cislo:
            max_vyhra = 100
            while krok - 1 != 0:
                max_vyhra = max_vyhra / 2
                krok -= 1
            vyhra = int(max_vyhra)
            penize += vyhra
            print(f"\x1B[31mvyhrál jsi \x1B[32m{vyhra}\x1B[31m dongů!! máš \x1B[32m{penize}\x1B[31m dongů pokračuj zmáčknutím \x1B[34m\"ENTER\" \x1B[0m")
            input()
            return(penize)
            break
        else:
            if rnd_cislo < hadaci_cislo:
                porovnavani = "míň"
            else:
                porovnavani = "víc"
            penize -= 10
        if penize < 0:
            return(penize)



sys_clr = 'cls' if os.name == 'nt' else 'clear'                                                     #zjistí jesli to je windows NT
mensi = ["m", "menší", "mensi"]
vetsi = ["v", "větší", "vetsi"]
rovno = ["r", "rovno"]
min = 0
max = 0
krok = 0
mod = 0
porovnavani = "míň/víc"
hadaci_cislo = "cislo"

while mod < 1 or mod > 3:                                                                           #vybrání modu
    os.system(sys_clr)
    print("\x1B[32m1\x1B[0m člověk hádá číslo\n\x1B[32m2\x1B[0m počítač hádá číslo\n\x1B[32m3\x1B[0m gambling hádání čísla")
    mod = int(input("Jaký mód chceš hrát: "))

x = int(input("\nZadej minimum: "))                                                                 #zadání minima

if min != x:
    min = x


while True:                                                                                         #zadání maxima
    x = int(input("\nZadej maximum: "))
    if x > min:
        max = x
        break
    print(f"číslo musí být větší než \x1B[32m{min}\x1B[0m")
    
rozsah = max - min
rnd_cislo = randint(min, max)
os.system(sys_clr)


if mod == 1:                                                                                         #mod 1
    while True:
        os.system(sys_clr)
        print(f"\x1B[34m{porovnavani}\x1B[0m než \x1B[32m{hadaci_cislo}\x1B[0m")
        print(f"Hádáš mezi \x1B[32m{min} až \x1B[32m{max}\x1B[0m")
        hadaci_cislo = int(input("Hádej číslo: "))
        krok += 1
        if rnd_cislo == hadaci_cislo:
            print(f"\n\nJo!!! Uhádl jsi to za \x1B[32m{krok}\x1B[0m kroků")
            break
        else:
            if rnd_cislo < hadaci_cislo:
                porovnavani = "míň"
            else:
                porovnavani = "víc"

if mod == 2:                                                                                        #mod 2
    while True:
        pulka = int(rozsah / 2 + min)
        krok += 1
        os.system(sys_clr)
        print(f"Je to \x1B[32m{pulka}\x1B[0m ?")
        porovnavani = input("\nvětší(\x1B[33mv\x1B[0m)\nmenší(\x1B[33mm\x1B[0m)\nrovno(\x1B[33mr\x1B[0m)\n\nje to: ")
        porovnavani = porovnavani.lower()
        if porovnavani in mensi:
            max = pulka

        elif porovnavani in vetsi:
            min = pulka

        elif porovnavani in rovno:
            os.system(sys_clr)
            print(f"\npočítač to uhodl po \x1B[32m{krok}\x1B[0m krocích, a uhádl \x1B[32m{pulka}\x1B[0m")
            break
        else:
            krok -= 1
        rozsah = max - min

if mod == 3:                                                                                    #mod 3
    penize = 100
    while True:
        penize = gamble(penize, rnd_cislo, porovnavani, krok, hadaci_cislo)
        rnd_cislo = randint(min, max)
        if penize <= 0:
            break

    print("\n\x1B[31mJsi v mínusu, vyprovodí tě exekutoři !!!\x1B[0m")
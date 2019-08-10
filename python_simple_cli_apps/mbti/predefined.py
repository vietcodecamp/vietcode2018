import sys
import time

#Predefined ====================================================================
#caption------------------------------------------------------------------------
caption = '''
____          ____      ____________      ____________________     ___
|   \        /   |     |   ______   \    |_______     ________|   |   |
|    \      /    |     |   |      \   \          |   |            |   |
|     \    /     |     |   |      /   /          |   |            |   |
|      \  /      |     |   |_____/   /           |   |            |   |
|       \/       |     |   _______  \            |   |            |   |
|   |\      /|   |     |   |     \   \           |   |            |   |
|   | \____/ |   |     |   |      \   \          |   |            |   |
|   |        |   |     |   |______/   /          |   |            |   |
|___|        |___|     |____________/            |___|            |___|

                        MYERS-BRIGGS TYPE INDICATOR
'''
#Explanations-------------------------------------------------------------------
explanations = '''
Myers-Briggs Type Indicator je osobnostní test navržený pro určení osobnostních typů.
Zaměřuje se na to, jak různí lidé vnímají svět a činí svá rozhodnutí.
Tento test spoléhá na čtyři klíče k určení typu (a proto jich je dohromady 16):

      1. JAK VNÍMÁTE OKOLNÍ PROSTŘEDÍ (INTROVERT   |   EXTROVERT)
      2. ZÍSKÁVÁNÍ INFORMACÍ          (SENSING     |   INTUITION)
      3. ZPRACOVÁNÍ INFORMACÍ         (FEELING     |   THINKING)
      4. ŽIVOTNÍ STYL                 (PROSPECTING |   JUDGING)

Vzhledem k možné předpojatosti, nebudeme vám říkati, co každý faktor znamená.
Pro přesné výsledky, prosím vyplňte test poctivě.
Otázky prosím odpovídejte od 1 do 5, kde 1 je nejméně souhlasím, 5 nejvíce a 3 neutrální.

'''
questionsFor1 = (("Komunikace s lidmi vám dělá značné potíže.",
 "Obvykle sami od sebe nezačínáte rozhovor.",
 "Zajímavá kniha nebo videohra je mnohdy lepší než společenská událost.",
 "Jste poměrně rezervovaný a tichý člověk.",
 "V plné místnosti se držíte blíže u zdi a vyhýbáte se jejímu středu."),
("Netrvá dlouho, než se na novém pracovišti zapojíte do společenského dění.",
"Rádi chodíte na společenská setkání s převleky a hraním rolí.",
"Cítíte, že po setkání se skupinou lidí máte více energie.",
"Ve společnosti často přebíráte iniciativu.",
"Radši byste strávili čas mezi lidi než doma."))

questionsFor2 = (("Obecně se dá říct, že se spoléháte spíše na své zkušenosti než představivost.",
 "Nepovažujete se za snílka.",
 "Máte radši prakci než teorii.",
 "Vaše sny se týkají spíše reálného světa a jeho dění.",
 "Považujete se více za praktického než kreativního."),
("Často se zamyslíte tak hluboce, že ignorujete své okolí či na něj zapomenete.",
"Na procházce přírodou se často ztratíte v myšlenkách.",
"Často trávíte čas přemýšlením nad nereálnými, neproveditelnými, ale přesto zajímavými nápady.",
"Často přemýšlíte nad smyslem lidské existence.",
"Vždy vás zajímaly neotřelé a nejednoznačné věci (například v knihách, výtvarném umění nebo filmech)." ))

questionsFor3 = (("Myslíte si, že je třeba respektovat názory všech bez ohledu na to, zda jsou podloženy fakty či nikoliv.",
 "Zvítězit v debatě je pro vás méně důležité, než aby nebyl nikdo vyveden z míry.",
 "Jako rodič byste byli raději, kdyby z vašeho dítěte vyrostl laskavý spíše než chytrý člověk.",
 "Kamarádovi, který je z něčeho smutný, nabídnete spíše emoční podporu, než abyste mu navrhli praktické způsoby, jak problém vyřešit.",
 "Ve vlastní firmě by pro vás bylo hodně těžké propustit věrné, ale málo výkonné zaměstnance."),
("V diskuzi by pravda měla být důležitější než ohleduplnost vůči druhým.",
"Nedovolíte druhým, aby ovlivnili vaše jednání.",
"Pravda by měla vždy vítězit.",
"V hádce je důležitější pravda než jsou emoce. ",
"Logika je při důležitém rozhodování obvykle důležitější než srdce." ))

questionsFor4 = (("Mít věci dobře uspořádané je pro vás důležitější než se umět přizpůsobit.",
 "Své cestovní plány obvykle dobře promýšlíte.",
 "Doma i v práci máte vcelku pořádek.",
 "Na e-mailové zprávy se snažíte odpovědět co nejdříve a nesnášíte, když máte v příchozích zprávách nepořádek.",
 "Málokdy něco uděláte z čisté zvědavosti."),
("Raději improvizujete, než abyste si připravili podrobný plán.",
"Dokážete zachovat klid a soustředit se i pod určitým tlakem.",
"Váš pracovní styl se podobá spíše nahodilým výbojům energie než metodickému a organizovanému přístupu.",
"Připravit plán a pak podle něj postupovat není nejdůležitější částí každého projektu.",
"Jste spíše rodilý improvizátor než pečlivý plánovač." ))
questions = [questionsFor1, questionsFor2, questionsFor3, questionsFor4]

def printing(text, delay, pause):
    for letter in text:
        time.sleep(delay)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(pause)

#KeyFactors=====================================================================
possibleAnswers = ("1","2","3", "4", "5")

initialI ='''

IIIIIIIIIIII
IIIIIIIIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
   IIIIII
IIIIIIIIIIII
IIIIIIIIIIII
'''
initialE ='''

EEEEEEEEEEEE
EEEEEEEEEEEE
EEE
EEE
EEE
EEE
EEE
EEEEEEEEEEEE
EEEEEEEEEEEE
EEE
EEE
EEE
EEE
EEEEEEEEEEEE
EEEEEEEEEEEE
'''
initialS ='''
   SSSSSSSS
SSSSSSSSSSSSSS
SSSS       SSS
 SSSS       SS
  SSS
   SSS
    SSS
     SSS
      SSS
       SSSS
        SSSS
         SSSS
SSS       SSSS
  SSS  SSSSSS
   SSSSSSSS
'''
initialN ='''
NNNN         NNN
NNNNN        NNN
NNNNNN       NNN
NNN NNN      NNN
NNN  NNN     NNN
NNN   NNN    NNN
NNN    NNN   NNN
NNN     NNN  NNN
NNN      NNNNNNN
NNN       NNNNNN
NNN        NNNNN
NNN         NNNN
NNN         NNNN
NNN         NNNN
'''

initialF ='''
FFFFFFFFFFFFFFFFF
FFFFFFFFFFFFFFFF
FFFF
FFFF
FFFF
FFFFFFFFFFF
FFFFFFFFFFF
FFFF
FFFF
FFFF
FFFF
FFFF
FFFF
FFFF
FFFF
'''
initialT ='''
TTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
      TTTTT
'''
initialJ ='''
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
       JJJJJ
 JJ    JJJJJ
 JJJ   JJJJ
 JJJJJ JJJ
   JJJJJ
'''
initialP = '''
PPPPPPPPPPPPP
PPPPPPPPPPPPPPP
PPPP       PPPP
PPPP       PPPP
PPPP       PPPP
PPPPPPPPPPPPPPP
PPPPPPPPPPPPP
PPPP
PPPP
PPPP
PPPP
PPPP
PPPP
PPPP
PPPP
'''


initials = ((initialI, initialE), (initialS, initialN), (initialF, initialT), (initialP, initialJ))
factors = (("Introverze","Extraverze"), ("Smysly","Intuice"), ("Cítění","Myšlení"), ("Vnímání","Usuzování"))
shortcuts = (('i', 'e'), ('s', 'n'), ('f', 't'), ('p', 'j'))

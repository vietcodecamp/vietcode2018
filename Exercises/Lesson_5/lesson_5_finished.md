# Exercises - Finished

## Average from input
* Předtím jsme vytvořili skript, který se uživatele zeptá na počet lidí a pak ve for smyčce získá hodnoty. Změňte for smyčku za `while` smyčku s tím, že bude skript sbírat data dokud nebude na vstupu `"STOP"`. Po zadání stop se spočítá průměr jako předtím.

```python
soucet_velikosti_bot = 0
pocet_student = 0

while True:
    vstup = input("Zadej velikost bot nebo \"STOP\" pro spočítání průměru: ")
    if vstup == "STOP":
        break
    else:
        soucet_velikosti_bot += float(vstup))
        pocet_studentu += 1
prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je " + str(prumer))
```

## Dacos casino
In 10 years, Dacos realizes teaching students programming is not profitable so he decides to open a casino instead.
There will a game, in which you play dices against Dacos himself. The rules are simple.

*Each of you rolls 3 dices and the greater sum wins (you can also extend the rules by adding bonuses for same-number combos).*
*A buy-in for each round is 10CZK. You take all your savings (100CZK) and face the owner with one goal - you either leave the casino with double of your savings, or with no money left*
*Run your script several times. Did you rip Dacos off, or did he rip you? How many rounds did you have to play?*

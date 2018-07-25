# Exercises - Finished

## Warm-up

## Food list
* Create a list of your favorite foods, for example: `jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]`
* print the list of foods in the following format:

```
1. bun cha
2. knedlo vepro zelo
3. pho
4. gulas
```

```python
jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]  # Uloz do pole svoje oblibena jidla podle tvych priorit.

#
poradi = 1
for jidlo in jidla:
    print(str(poradi) + ". " + jidlo)
    poradi = poradi + 1

# 2 způsob - Použití enumerated
for (index, prvek) in enumerate(jidla):
    print(str(index + 1) + ". " + prvek)
```

## Input in for loop
* Get 5 favourite foods from a user using a loop
 * Hint: `for i in range(5):`, `jidla.append(input("Zadejte jídlo: "))`, `', '.join(jidla)`,

```python
jidla = []
for i in range(1, 6):
  jidla.append(input("Zadej tvoje " + str(i) + ". nejoblíbenější jídlo: "))

print("Tvoje nejoblíbenější jídla jsou: " + ', '.join(jidla))  
```

# Hard Exercises

## Accumulation
* Given an array of numbers `cisla = [4.5, 1.5, 1.2, 8.9, 2.3]` calculate the **sum** of the numbers
  * Note: without using `sum()`
  * Hints: calculate the sum using a for loop and save the result to a variable

```python
cisla = [ 4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
  soucet = soucet + cislo

print("Součet čísel je: " + str(soucet))
```

## Average
* Improve the above code so that it also prints the **average** of the numbers

```python
cisla = [ 4.5, 1.5, 1.2, 8.9, 2.3]
soucet = 0
for cislo in cisla:
  soucet += cislo

prumer = soucet / len(cisla)
print("Součet čísel je: " + str(soucet))
print("Průměr čísel je: " + str(prumer))
```  
## Average from input
* Calculate the average shoe size in your class. First ask for the number of students, then get all of their sizes. Then sum and divide them to get the average

```python
soucet_velikosti_bot = 0
pocet_studentu = int(input("Zadej počet studentů: "))
for i in range(pocet_studentu):
  soucet_velikosti_bot += float(input("Zadej velikost bot {}. studenta: ".format(i + 1)))

prumer = soucet_velikosti_bot / pocet_studentu
print("Průměrná velikost bot je " + str(prumer))  
```

# Extra exercises for fast campers

## Class division
* Lets say we a class students stored in a list `trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]` and we need to divide the class into two halves. We want to have every odd member in one list and every even member in a second list. The result should look like this: `trida_a = ["Honza", "Tue", "Vojta"]` and `trida_b = ["Kevin", "Radek", "Adéla"]`

```python
trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]
trida_a = []
trida_b = []

for index in range(0, len(trida), 2):
  kemper = trida[index]
  trida_a.append(kemper)

for index in range(1, len(trida), 2):
  kemper = trida[index]
  trida_b.append(kemper)  

print(", ".join(trida_a))
print(", ".join(trida_b))
```

Solution 2:

```python
trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]
trida_a = []
trida_b = []

for index in range(len(trida)):
  kemper = trida[index]
  if index % 2 == 0: # if index is even
    trida_b.append(kemper)
  else:
    trida_a.append(kemper)  

print(", ".join(trida_a))
print(", ".join(trida_b))
```

## Priority sorting
* Given a list `jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]` and priorities of the food `priority = [4, 2, 1, 3]
` This means that "bun cha" has priotity `4`, "pho" has priority `1` and so on. Create a new list with the same food as in `jidla` but in a order defined in `priority` variable. For this example, the expected output would be `["pho", "knedlo vepro zelo", "gulas", "bun cha"]`.

```python
jidla = ["bun cha", "knedlo vepro zelo", "pho", "gulas"]
priority = [3, 1, 0, 2]
serazena_jidla = ["", "", "", ""] # len(jidla) * [""] vytvoří ten samý list

for i in range(len(jidla)):
    jidlo = jidla[i]
    priorita_jidla = priority[i]
    serazena_jidla[priorita_jidla] = jidlo

print(", ".join(serazena_jidla))
```

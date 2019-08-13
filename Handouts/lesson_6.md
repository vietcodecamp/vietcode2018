# Lesson 6
**Lesson goal:** After this lesson the learner will be able to reuse code by defining functions and using them.

# Outline
1. What is a function?
2. Definition of your own functions

# What is a function?
**Problem:** I want to calculate average of a list in multiple parts of my code. I don't want to write the same code again

**Solution:** We can extract this code for average calculation into a subroutine called function and then we can reuse this function in multiple parts of my code.

**Example:**
* I want to calculate the average height, weight of the students in class.

A solution, that you would propably do:
```python
vysky = [1.51, 1.65, 1.75, 1.8, 1.49]
soucet_vysek = 0
for vyska in vysky:
  soucet_vysek = prumerna_vyska + vyska

prumerna_vyska = soucet_vysek/len(vysky)

print("Pruměrná výška třídy je " + str(prumerna_vyska) + " m.")


hmotnosti = [50, 60, 65, 70, 45]
soucet_hmotnosti = 0

for hmotnost in hmotnosti:
  soucet_hmotnosti = soucet_hmotnosti + hmotnost

prumerna_hmotnost = soucet_hmotnosti/len(hmotnost)  

print("Pruměrná hmotnost třídy je: " + str(prumerna_hmotnost) + " kg.")

```

A solution using a function:
```python
def prumer(seznam_cisel):
  soucet = 0
  for cislo in seznam_cisel:
    soucet = soucet + cislo
  prumer = soucet/len(seznam_cisel)
  return prumer

vysky = [1.51, 1.65, 1.75, 1.8, 1.49]
prumerna_vyska = prumer(vysky)
print("Pruměrná výška třídy je " + str(prumerna_vyska) + " m.")

hmotnosti = [50, 60, 65, 70, 45]
prumerna_hmotnost = prumer(hmotnosti)
print("Pruměrná hmotnost třídy je " + str(prumerna_hmotnost) + " kg.")

```

## Exercises
* [Files](../Exercises/Lesson_6)
* [Start](../Exercises/Lesson_6/lesson_6_start.md)
* [Finished](../Exercises/Lesson_6/lesson_6_finished.md)

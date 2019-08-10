import predefined                                        #it doesn't feel right doing this and the constant use of predefined. is also tiring,
print(predefined.caption)                                #but due to the amount of text, this is much more pleasant to the eye
predefined.printing(predefined.explanations, 0.05, 1)   #important to read, hence moving slow - so the reader doesn't get ahead of himself
results = [0]*4
typeIndicator = []
typeIndicatorLetter = []
counter = 0
for questionIndex in range(len(predefined.questionsFor1[0])):                #this is a veryvery awkward and inefficiend way of looping,
    for questionPair in range(0, 2):                                         #but the 'test' would be better of, if weren't completely 'chronological',
        for questionType in range(len(predefined.factors)):                  #meaning asking for each section, which could also lead to realization of the mechanism of the test
            predefined.printing((predefined.questions[questionType][questionPair][questionIndex]+" "), 0.005, 0.01)
            while True:
                answer = input()
                if answer not in predefined.possibleAnswers:
                    print("Prosím zadejte číslo od 1 do 5 jako odpověď na předchozí otázku.")
                else:
                    break
            if(questionPair == 0):
                results[questionType] += int(answer)                        #not int-ing the input straightaway is because it wouldn't work if the input would happen to be a diff type?
            else:
                results[questionType] -= int(answer)
for factor in results:
    if factor >= 0: #why even when its = 0? When one cannot decide between certain attribute, it means that most likely, it is the one that would result from this (apparently so by psychologists)
        indicator = 0
    else:
        indicator = 1
    typeIndicator.append(predefined.shortcuts[counter][indicator])
    typeIndicatorLetter.append(predefined.initials[counter][indicator])
    counter +=1
for letter in typeIndicatorLetter:
    print(letter)

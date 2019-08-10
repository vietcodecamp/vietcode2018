#Variables
lecturers = ["Dagy!", "Dacos!", "Franta!", "the hard skill lecturer Jana!",
             "the soft skill lecturer Jana!", "Nitka!", "Milan!"]
question_result = [] #To decide who the person is
bonus_question_result = [] #Also to decide who the person is
loop = 0 #For while loop and question to work properly
ask = 0 #For Questions in while loop
bonus_ask = 0 #For Bonus questions in while loop
random_ask = 0 #For Random question in while loop
bonus_random_ask = 0 #For Bonus random question in while loop
permission = True

#Questions
Q1 = "Does the person play the quitar? "
Q2 = "Does the person do martial art? "
Q3 = "Does the person have siblings? "
Q4 = "Does the person wear glasses? "
Q = [Q1, Q2, Q3, Q4]

#Bonus questions
q1 = "Does the person play on any other instrument? " 
q2 = "Does or did the person do any other sport? "
q3 = "Does the person teach soft skills? "
q4 = "Was the person a host in VietCode? "
q = [q1, q2, q3, q4]

#Random questions that don't influence the result
rQ1 = "Is the person attractive? "
rQ2 = "Would you like to hang out with this person? "
rQ3 = "Does the person remind you of a goat? "
rQ4 = "Does the person walk like a frog? "
rQ = [rQ1, rQ2, rQ3, rQ4]

#Bonus random questions
rq1 = "Is the person muscular? "
rq2 = "What about a date? "
rq3 = "Would you eat him/her? "
rq4 = "Is the person THICC? "
rq = [rq1, rq2, rq3, rq4]

#Lecturers' individual results by answers
Dagy_result = [[0, 1, 0, 0], [2, 1, 2, 0], [0, 1, 2, 0], [2, 1, 0, 0]]
Dagy_bonus_result = [[0, 1, 0, 0], [2, 1, 0, 0], [0, 2, 0, 0], [2, 2, 0, 0]]
Dacos_result = [[1, 0, 1, 1], [1, 2, 2, 1], [1, 2, 1, 1], [1, 0, 2, 1]]
Dacos_bonus_result = [[1, 0, 0, 1], [2, 2, 0, 1], [2, 0, 0, 1], [1, 2, 0, 1]]
Franta_result = [[1, 0, 1, 0], [2, 0, 2, 0], [2, 0, 1, 0], [1, 0, 2, 0]]
Franta_bonus_result = [[0, 1, 0, 0], [2, 2, 0, 0], [2, 1, 0, 0], [0, 2, 0, 0]]
Jana_result = [[0, 0, 1, 1], [0, 2, 2, 1], [0, 2, 1, 1], [0, 0, 2, 1]]
Jana_bonus_result = [[1, 1, 0, 0], [2, 2, 0, 0], [2, 1, 0, 0], [1, 2, 0, 0]]
Janina_result = [[0, 0, 1, 0], [2, 0, 2, 0], [0, 0, 2, 0], [2, 0, 1, 0]]
Janina_bonus_result = [[1, 1, 1, 0], [2, 2, 1, 0], [2, 1, 1, 0], [1, 2, 1, 0]]
Nitka_result = [[0, 0, 1, 1], [2, 0, 2, 1], [2, 0, 1, 1], [0, 0, 2, 1]]
Nitka_bonus_result = [[0, 1, 1, 0], [2, 2, 1, 0], [2, 1, 1, 0], [0, 2, 1, 0]]
Milan_result = [[1, 0, 1, 1], [2, 2, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]]
Milan_bonus_result = [[0, 1, 0, 0], [2, 2, 0, 0], [2, 1, 0, 0], [0, 2, 0, 0]]

#Defining functions
def questions(result):
    global answer
    if answer.lower() == "yes":
        result.append(1)
    if answer.lower() == "no":
        result.append(0)
    if answer.lower() == "idk":
        result.append(2)
    
def VietKinator():
    global loop
    global ask
    global bonus_ask
    global random_ask
    global bonus_random_ask
    global answer
    while loop < len(Q):
        #Main question
        if ask == bonus_ask and ask == random_ask and ask == bonus_random_ask:
            answer = input(Q[ask])
            if answer.lower() == "yes" or answer.lower() == "no" or answer.lower() == "idk":
                questions(question_result)
                ask = ask + 1
                print("")
            else:
                print("Invalid answer.")
                print("")
                continue
        #Bonus question
        if ask > bonus_ask:
            answer = input(q[bonus_ask])    
            if answer.lower() == "yes" or answer.lower() == "no" or answer.lower() == "idk":
                questions(bonus_question_result)
                bonus_ask = bonus_ask + 1
                print("")
            else:
                print("Invalid answer.")
                print("")
                continue
        #Random question
        if bonus_ask > random_ask:
            answer = input(rQ[random_ask])    
            if answer.lower() == "yes" or answer.lower() == "no" or answer.lower() == "idk":
                random_ask = random_ask + 1
                print("")
            else:
                print("Invalid answer.")
                print("")
                continue
        #Bonus random question
        if random_ask > bonus_random_ask:
            answer = input(rq[bonus_random_ask])    
            if answer.lower() == "yes" or answer.lower() == "no" or answer.lower() == "idk":
                bonus_random_ask = bonus_random_ask + 1
                print("")
            else:
                print("Invalid answer.")
                print("")
                continue
        loop = loop + 1

def VietKinator_results():
    if question_result in Dagy_result and bonus_question_result in Dagy_bonus_result:
         print("It's " + lecturers[0])
    elif question_result in Dacos_result and bonus_question_result in Dacos_bonus_result:
         print("It's " + lecturers[1])
    elif question_result in Franta_result and bonus_question_result in Franta_bonus_result:
         print("It's " + lecturers[2])
    elif question_result in Jana_result and bonus_question_result in Jana_bonus_result:
         print("It's " + lecturers[3])
    elif question_result in Janina_result and bonus_question_result in Janina_bonus_result:
         print("It's " + lecturers[4])
    elif question_result in Nitka_result and bonus_question_result in Nitka_bonus_result:
         print("It's " + lecturers[5])
    elif question_result in Milan_result and bonus_question_result in Milan_bonus_result:
         print("It's " + lecturers[6])
    else:
         print("There is no such lecturer or there is not enough information.")
    print("")

        
#Running the programme
print("\nWelcome to VietKinator.")
print("Answer the questions and I will guess which lecturer you are thinking about.")
print("Only answer 'yes', 'no' or 'idk'.\n")
while True:
    if permission == True:
        VietKinator()
        VietKinator_results()
        print("Would you like me to guess another lecturer?\n")
    restart = input("Write 'yes' to continue and 'no' to exit: ")
    if restart.lower() == "yes":
        question_result.clear()
        bonus_question_result.clear()
        loop = 0
        ask = 0 
        bonus_ask = 0 
        random_ask = 0
        bonus_random_ask = 0
        permission = True
        print("")
        continue
    elif restart.lower() == "no":
        exit(1)
    else:
        permission = False
        print("Invalid answer.")
        print("")
        

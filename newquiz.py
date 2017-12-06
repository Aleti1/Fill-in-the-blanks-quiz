difficulty = ["easy", "medium", "hard"]                     #difficulty choices.
easy_chance_min = 5
easy_chance_max = 10                                         # Here are the chances
easy = [easy_chance_min, easy_chance_max]                    # u get for every
medium_chance_min = 3                                        # difficulty level.
medium_chance_max = 7
medium = [medium_chance_min, medium_chance_max]
hard_chance_min = 1
hard_chance_max = 3
hard = [hard_chance_min, hard_chance_max]
answer_hint_min = 0                                          #it will display the first character from answer
answer_hint_max = 4                                          #it will display the 4th character from answer
questionsem = ["What is the result of: 25 + 76 = _____ .",   #Easymode questions.
               "What is the result  of 36 * 75 = _____ .",
               "What is the result  of 81 * 55 = _____ .",
               "What is the result  of 99363339 / 3 = _____ .",
               "What is the result  of 2 ** 2 ** 5 ** 4 = _____ ."]
answersem = ["101",                                      #Easymode answers.
             "2700",
             "4455",
             "33121113",
             "340282366920938463463374607431768211456"]
#----- https://www.toprankers.com/exams/ibps-po-fill-in-the-blanks-questions-with-answers-pdf-download/ This is the link from where i copyed the next questions.
questionsmm = ["Though India does not have comprehensive laws that _____ companies\n polluting the environment, companies in India have\n become conscious of their roles and are taking necessary\n steps to conserve environment and minimize damage.",    # Sry for the long post.Here is a potato 0. Mediummode questions.
               "Baldwin-s brilliant The Fire Next Time is both so eloquent in its\n passion and so searching in its candour that it is\n bound to _____ any reader.",
               "They swiveled their seats away from the curved wall panels\n to give themselves more space as the flight\n attendant brought drinks from the gallery which was\n _____ with familys favorite snacks and beverages.",
               "We didn't really want that particular hotel, _____ it was\n a case of Hobson's choice.We booked very late and\n there was nothing else left.",
               "_____ the situation infuriated him he did his best to hide his anger."]
answersmm = ["restrict",                                 #Mediummode answers.
             "unsettle",
             "stocked",
             "but",
             "Though"]
#----- Next set of questions are quotes known from Albert Einstein.
questionshm = ["Imagination is more important than knowledge.\n _____ is limited. Imagination encircles the world.",                                    #Hardmode questions.
               "Great spirits have always encountered violent\n opposition from _____ minds.",
               "Everybody is a genius. But if you judge a fish\n by its ability to climb a tree, it will live\n its whole life _____ that it is stupid.",
               "Not everything that can be counted counts,\n and not everything that _____ can be counted.",
               "Unthinking _____ for authority is the greatest enemy of truth."]
answershm = ["Knowledge",                               #Hardmode answers.
             "mediocre",
             "believing",
             "counts",
             "respect"]

#----------------------------------------------------------------------
'''This function determines if user needs help with the answer of a certain question
    :inputs: the variables answer and difficulty that have been
    used to keep track of the correct answer at the specific question
    :outputs: the return will show to user the first 4 letters of the current answer
    as long as game is not in hard mode. '''
def helping(answer, difficulty):
    if difficulty == "hard":
        return "In this mode you don't have a help option available!"
    else:
        return answer[answer_hint_min:answer_hint_max]

#----------------------------------------------------------------------
'''This function will replace the blank spaces in questions with the correct answer
    :inputs: the variables question and answer that are used to keep
    track of the correct answer at the specific question
    :outputs:the current question with blank replaced by the correct answer'''
def fill_blanks(question, answer):
    blank = "_____"
    print "Correct answer: " + question.replace(blank, answer)

#----------------------------------------------------------------------
'''This function will let the user choose how many lives he can
   have while in a specific difficulty.
   :input:the variable difficulty that the game will run:
   :outputs:show the user how many lives he can choose in a specific difficulty'''
def life_left(difficulty):
    lives_chosen = 0
    if difficulty == "easy":
        print "In this mode you can always ask for hints just by writing <help>"
        while lives_chosen < easy_chance_min or lives_chosen > easy_chance_max:
            print "In " + difficulty + " mode you can choose to have from " + str(easy_chance_min) + " to " + str(easy_chance_max) + " wrong guesses!"
            lives_chosen = int(raw_input("Enter number of lives: "))
    elif difficulty == "medium":
        print "In this mode you can always ask for hints just by writing <help>"
        while lives_chosen < medium_chance_min or lives_chosen > medium_chance_max:
            print "In " + difficulty + " mode you can choose to have from " + str(medium_chance_min) + " to " + str(medium_chance_max) + " wrong guesses!"
            lives_chosen = int(raw_input("Enter number of lives: "))
    else:
        while lives_chosen < hard_chance_min or lives_chosen > hard_chance_max:
            print "In " + difficulty + " mode you can choose to have from " + str(hard_chance_min) + " to " + str(hard_chance_max) + " wrong guesses!"
            lives_chosen = int(raw_input("Enter number of lives: "))
    print "You have selected " + str(difficulty) + " mode and you have " + str(lives_chosen) + " chances to get the right answer!"
    return lives_chosen
#--------------------------------------------------------------------
'''This function will run the game as long as the user have more then 0 lives
   and the last question is not answered.If last question is answered corectly
   the game will start again.
   :inputs:It takes as inputs the variables of lives_chosen, questions, answers
   and difficulty
   :outputs:will show the question and after it will be dealt with will show the
   next question until the game is completed.Will olso display hints for help command
   as long as the game runs in easy or mediu mode.'''
def play_game(lives_chosen, questions, answers, difficulty):
    index = 0
    while lives_chosen > 0:
        user_input = user_choice(questions[index])
        if user_input == "help":
            print "HINT: " + helping(answers[index], difficulty) + "\n"
            continue
        if check_correct_answer(questions[index], answers[index], user_input, lives_chosen):
            index = index + 1
            if index == len(questions) and index == len(answers):
                print "Congratulations! You have finished the game!"
                running_game()
        else:
            lives_chosen = lives_chosen - 1
            if lives_chosen == 0:
                print "END GAME"
                running_game()


#--------------------------------------------------------------------
'''This function will check if the user responses with a corect answer
   and calls the function fill_blanks.
   :inputs:it takes the question, answer, user input and lives as variable inputs
   and checks if answer is corect.
   :output:a boolean saying if the answer is corect or wrong. '''
def check_correct_answer(question, answer, user_input, lives):
    if user_input == answer:
        fill_blanks(question, answer)         #here is called the fillin blanks function.
        print " --- Nice job --- \n"
        return True
    else:
        print "Sorry the answer is wrong! Lives left: " +str(lives - 1)
        if lives - 1 != 0:
            print "Try again!\n"
        return False



#--------------------------------------------------------------------
''':input: the question
   :outputs:the answer input by the user'''
def user_choice(question):
    user_input = raw_input("This is your question:\n" + question + "\nThis is your answer: ")
    return user_input

#--------------------------------------------------------------------
'''This function has the role to make the user choose a
   level difficulty.
   :inputs: has no input!
   :outputs:the difficulty the game will run on.'''
def chosen_difficulty():
    dif = ""
    while not (dif == "easy" or dif == "medium" or dif == "hard"):          #this is necessary so that player can choose only from this set of difficulty
        dif = raw_input("Type in a difficulty: Your choices are: Easy, Medium or Hard:\n")
    return dif
#--------------------------------------------------------------------
'''This function will know which difficulty to run on the game
   and with set of questions and answers to outputs
   :input:it takes as input lives and difficulty and chooses the
   corect game settings.
   :outputs: Has no outputs!'''
def starting_game(lives, difficulty):
    if difficulty == "easy":
        play_game(lives, questionsem, answersem, difficulty)              #here the code will know
    elif difficulty == "medium":                                       #what questions and
        play_game(lives, questionsmm, answersmm, difficulty)              #answers to print back
    elif difficulty == "hard":                                         #depanding on the difficulty
        play_game(lives, questionshm, answershm, difficulty)
#--------------------------------------------------------------------
'''This function will keep the right order for the calling
   of functions
   It has no outputs or inputs.'''
def running_game():
    difficulty = chosen_difficulty()
    lives = life_left(difficulty)
    starting_game(lives, difficulty)

running_game()

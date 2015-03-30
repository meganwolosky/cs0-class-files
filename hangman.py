import random 

def getDrawing(wrongGuesses):

    hangmanPics = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========''']

    return hangmanPics[wrongGuesses]
    
def loadWord():
    persons = ['Beyonce', 'MikeKane', 'KimKardashian', 'RobinWilliams', 'CharlieSheen', 'HannahMontana', 'NorthWest', 'EllenDeGeneres', 'BarackObama', 'JustinBieber']
    places = ['NewYork', 'Alaska', 'Florida', 'Ocala', 'Manhattan', 'Chicago', 'Colorado', 'LosAngeles', 'Nebraska', 'Brooklyn']
    things = ['Pencil', 'Ipad', 'Car', 'Computer', 'SwimSuit', 'Airplane', 'Floaties', 'Rubberduck', 'Basketball', 'Volleyball']
    lists = [persons, places, things] 
    listChosen = random.choice(lists)
    secretWord = random.choice(listChosen)
    hint = ''
    if listChosen == persons:
        hint = 'person'
    elif listChosen == things:
        hint = 'thing'
    else:
        hint = 'place'
    
    
    
    return (secretWord,hint)
    
def isWordGuessed(secretWord, lettersGuessed):
    
   for letter in secretWord:
       if letter not in lettersGuessed:
           return False
   return True
            
def getGuessedWord(secretWord, lettersGuessed):
    printedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            printedWord += letter + ' '
        else:
            printedWord += '_ '
    return printedWord      
    
def getAvailableLetters(lettersGuessed):
    availableLetters = ''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter + ' '
    return availableLetters
    

        

def hangman():
    
    #DECLARING NECESSARY VARIABLES
    loaded = loadWord()
    secretWord = loaded[0].lower()
    hint = loaded[1]
    wrongGuesses = 0
    lettersGuessed = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    print "I am thinking of a" + ' ' + hint 
    while wrongGuesses < 6:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "You Won!"
        else:
            print getAvailableLetters(lettersGuessed)
            guess = raw_input("Please pick a letter:     ")
            guess = guess.lower()
            
            while len(guess) != 1 or guess not in alphabet or guess in lettersGuessed:
                print getAvailableLetters(lettersGuessed)
                guess = raw_input("Invalid choice! Please pick a valid letter:     ")
        
        
            lettersGuessed.append(guess)
            
            if guess not in secretWord:
                wrongGuesses += 1
                print "Sorry--incorrect!"
            else:
                print "Good guess!"
            
            print getGuessedWord(secretWord,lettersGuessed)
        print getDrawing(wrongGuesses)
    print "The secret word was" + ' ' + secretWord
    return "HANGMAN!  You lose!"  
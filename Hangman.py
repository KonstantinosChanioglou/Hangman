import os
#Initialize viriables
allowedTries = 6
tries = 0
guessedLetters = [] 
guessedLetter = ''
wordFound = False

#Clear console
os.system('cls')

try:
    #Dynamic input and validation
    wordToGuess = input("Player1 enter a word to guess Player2:")
    while not wordToGuess.isalpha():
        wordToGuess = input("Your input was not valid! Enter a valid word:")
    wordToGuess = list(wordToGuess.lower())
    progress = ['_' for i in range(0,len(wordToGuess))] #a list depicting the users' progress filled with _

    #Clear Cosnsole and time for Player2 to guess the word
    os.system('cls')
    print("The game is starting now! Player2 is your time to shine!")

    while tries < allowedTries and not wordFound:

        #Print Informaion that user need to know
        print("You have " + str(allowedTries - tries) + " tries left")
        print("Used letters:", end = " ")
        print(*guessedLetters, sep = ",")
        print("Word:", end = " ") #instead of "\n" end the line woth " "
        print(*progress) #print all the elements of the list in one line
        guessedLetter = str(input("Guess a letter:")).lower() #


        #Validate that the input has len 1 and is letter
        while len(guessedLetter) != 1 or not guessedLetter.isalpha():
            print("Your input was not valid! Enter a valid input!")
            guessedLetter = str(input("Guess a letter:")).lower()


        #Check if the guessed letter have been guessed in the past
        if guessedLetter in guessedLetters:
            os.system('cls')
            print("***You have already guessed this letter!***")
            continue
        else:
            guessedLetters.append(guessedLetter)

        for index,letter in enumerate(wordToGuess):# take the index and the value for each element of wordToGuess list
            if letter == guessedLetter:
                indixes = [i for i, x in enumerate(wordToGuess) if x == guessedLetter] #Find all the occurrences of the guessedLetter in the word
                for i in indixes:
                    progress[i] = letter #Replace found occurrences of the guessedLetter in the word with the guessedLetter
                
                wordFound = False if '_' in progress else True #If there is no _ in the progress then the user found all the missing letters
                break #if the guessedLetter was found we dont need to compare the rest of the letters
            elif index == len(wordToGuess) - 1 : #if the loop is in the last iteration and the leter is not guessed right the tries++
                tries += 1

        os.system('cls')

    if wordFound:
        print("You're on fire!:D You guessed the word:", end = " ")
        print(*progress, sep ="", end = "!\n")
    else:
        print("You had one job :P", end = " "), 
        print("The word you had to guess was:", end = " ")
        print(*wordToGuess, sep = "", end = "!")

except:
	print("An exception has occured")

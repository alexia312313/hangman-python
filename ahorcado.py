##################################
#       Hangman in Python        #
#     Made by Jose and Alex      #
#          version: 11           #
##################################


# main function where the hangman game will be executed
def main(failures=0, turn=0, vocal="AEIOU", word=list, letter=str, word_to_str=str):
    # import os for the execution of the command cls in cmd
    import os

    check = False
    # Input of key word with a check
    while not check:
        word = list(input("Please write a word: ").upper())
        # convert the variable word from list to str, also capitalizing it
        word_to_str = (''.join(word)).capitalize()
        if word_to_str.isalpha():
            check = True
        else:
            print("Only letters are allowed!!")

    # clear cmd, so that the player does not know the word to guess
    os.system("cls")

    # Calculate the number of bars based on the numbers of letter of the word
    bar = list(len(word) * "_")

    # variable inputLetters where all the letters inputted will go
    input_letters = list()

    # the variable hangman that it will show the failures that the player has
    hangman = [
        ' _____    \n |        \n |        \n |        \n |        \n_|_______\n',
        ' _____    \n |   |    \n |        \n |        \n |        \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |        \n |        \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |   |    \n |        \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |  /|    \n |        \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |  /|\   \n |        \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |  /|\   \n |  /     \n_|_______\n',
        ' _____    \n |   |    \n |   O    \n |  /|\   \n |  / \   \n_|_______\n'
    ]

    # the main loop where the player will lose or win
    while failures != len(hangman) - 1:

        # try, to avoid crashes
        try:
            turn += 1
            check = False
            fail = True

            # print the variable bar as string
            print(' '.join(bar))

            # check if the turn is odd or even
            if turn < 7:
                while not check:
                    # If the turn is odd the player will have to write a vocal
                    if turn % 2 == 0:
                        while not check:
                            letter = input("Please write a vocal: ").upper()
                            if letter.isalpha():
                                check = True
                        check = False
                        if letter[0] in vocal and letter[0] not in input_letters:
                            check = True
                        elif letter[0] in vocal and letter[0] in input_letters:
                            print("You have already entered the letter previously")
                        else:
                            print("Only vowels are allowed!!")
                    # If the turn is even the player will have to write a consonant
                    else:
                        while not check:
                            letter = input("Please write a consonant: ").upper()
                            if letter.isalpha():
                                check = True
                        check = False
                        if letter[0] not in vocal and letter[0] not in input_letters:
                            check = True
                        elif letter[0] not in vocal and letter[0] in input_letters:
                            print("You have already entered the letter previously")
                        else:
                            print("Only consonants are allowed!!")
                input_letters += letter[0]
            else:
                while not check:
                    while not check:
                        letter = input("Please write a letter: ").upper()
                        if letter.isalpha():
                            check = True
                        else:
                            print("Only letters are allowed!!")
                    check = False
                    if letter[0] not in input_letters:
                        check = True
                    else:
                        print("You have already entered the letter previously")
                input_letters += letter[0]

            # loop to check if the player failed or successful
            for i in range(0, len(word)):
                # if true the letter will replace the "i" position of the variable bar
                if word[i] == letter:
                    bar[i] = letter
                    fail = False

            # fails count
            if fail:
                failures += 1

            # win execution
            if bar == word:
                os.system("cls")
                print("The word is: " + word_to_str)
                print("Congratulations, you Win!")
                break

            # print the hangman variable
            print(hangman[failures])

        except ValueError:
            print("Oops! Try it again...")
    else:
        os.system("cls")
        print(hangman[failures])
        print("The word was: " + word_to_str)
        print("GAME OVER")


# Call the function main
main()

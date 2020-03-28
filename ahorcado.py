##################################
#       Hangman in python        #
#     Made by Jose and Alex      #
#        version: beta 7         #
##################################


# main function where the hangman game will be executed
def main(failures=0, turn=0, vocal="AEIOU", letter=str, word=list):
    # import os for the execution of the command cls in cmd
    import os

    check = False
    # Input of key word
    while not check:
        word = list(input("Please write a word: ").upper())
        wordStr = ''.join(map(str, word))
        if wordStr.isalpha():
            check = True

    # clear cmd, so that the player does not know the word to guess
    os.system("cls")

    # Calculate the number of bars based on the numbers of letter of the word
    bar = list(len(word) * "_")

    inputLetters = list()

    # variable hangman that it will show the failures that the player has
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

    # main loop where the player will lose or win
    while failures != len(hangman) - 1:

        # try, to avoid crashes
        try:
            turn += 1
            check = False
            fail = True

            # print the variable bar as string
            print(' '.join(map(str, bar)))

            # check if the turn is odd or even
            if turn < 7:
                while not check:
                    # If the turn is odd the player will have to write a vocal
                    if turn % 2 == 0:
                        letter = input("Please write a vocal: ").upper()
                        if letter[0] in vocal and letter[0] not in inputLetters:
                            check = True
                        elif not letter.isalpha() or letter[0] not in vocal:
                            print("Only vowels are allowed!!")
                        elif letter[0] in vocal and letter[0] in inputLetters:
                            print("You have already entered the letter previously")
                    # If the turn is even the player will have to write a consonant
                    else:
                        letter = input("Please write a consonant: ").upper()
                        if letter[0] not in vocal and letter[0] not in inputLetters and letter[0].isalpha():
                            check = True
                        elif not letter.isalpha() or letter[0] in vocal:
                            print("Only consonants are allowed!!")
                        elif letter[0] not in vocal and letter[0] in inputLetters:
                            print("You have already entered the letter previously")
                inputLetters += letter[0]
            else:
                while not check:
                    letter = input("Please write a letter: ").upper()
                    if letter[0] not in inputLetters and letter[0].isalpha():
                        check = True
                    elif not letter.isalpha():
                        print("Only letters are allowed!!")
                    elif letter[0] in inputLetters:
                        print("You have already entered the letter previously")
                inputLetters += letter[0]

            # loop to check if the player failed or successful
            for i in range(0, len(word)):
                # if true the letter will be replace the i position of the variable bar
                if word[i] == letter:
                    bar[i] = letter
                    fail = False

            # fails count
            if fail:
                failures += 1

            # win execution
            if bar == word:
                os.system("cls")
                print("The word is: " + (''.join(map(str, word))).capitalize())
                print("Congratulations, you Win!")
                break

            # print the hangman variable
            print(hangman[failures])

        except ValueError:
            print("Oops! Try it again...")
    else:
        os.system("cls")
        print(hangman[failures])
        print("The word was: " + (''.join(map(str, word))).capitalize())
        print("GAME OVER")


# Call the function main
main()

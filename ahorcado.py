#####################################
# Ahorzado en python version 1-beta #
#     Hecha por jose y alex         #
#####################################

AHORCADO = ['''






    =========''', '''

          |
          |
          |
          |
          |
    =========''', '''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
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

palabra = input("Escribre una palabra: ")
win = list(palabra)
lenword = len(palabra)
numletras = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ "]

if lenword == 2:
    numletras = ["_ ", "_ "]
elif lenword == 3:
    numletras = ["_ ", "_ ", "_ "]
elif lenword == 4:
    numletras = ["_ ", "_ ", "_ ", "_ "]
elif lenword == 5:
    numletras = ["_ ", "_ ", "_ ", "_ ", "_ "]
elif lenword == 6:
    numletras = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
elif lenword == 7:
    numletras = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
elif lenword == 8:
    numletras = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
elif lenword == 9:
    numletras = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]


def printwin():
    if lenword == 2:
        print(numletras[0], numletras[1])
    elif lenword == 3:
        print(numletras[0], numletras[1], numletras[2])
    elif lenword == 4:
        print(numletras[0], numletras[1], numletras[2], numletras[3])
    elif lenword == 5:
        print(numletras[0], numletras[1], numletras[2], numletras[3], numletras[4])
    elif lenword == 6:
        print(numletras[0], numletras[1], numletras[2], numletras[3], numletras[4], numletras[5])
    elif lenword == 7:
        print(numletras[0], numletras[1], numletras[2], numletras[3], numletras[4], numletras[5], numletras[6])
    elif lenword == 8:
        print(numletras[0], numletras[1], numletras[2], numletras[3], numletras[4], numletras[5], numletras[6], numletras[7])
    elif lenword == 9:
        print(numletras[0], numletras[1], numletras[2], numletras[3], numletras[4], numletras[5], numletras[6], numletras[7], numletras[8])
    return


printwin()
fallos = 0

while not numletras == win and not fallos == 9:
    try:
        letra = input("Escribe una letra: ")
        if palabra[0] == letra:
            numletras[0] = letra
            printwin()
        elif len(palabra) >= 2 and palabra[1] == letra:
            numletras[1] = letra
            printwin()
        elif len(palabra) >= 3 and palabra[2] == letra:
            numletras[2] = letra
            printwin()
        elif len(palabra) >= 4 and palabra[3] == letra:
            numletras[3] = letra
            printwin()
        elif len(palabra) >= 5 and palabra[4] == letra:
            numletras[4] = letra
            printwin()
        elif len(palabra) >= 6 and palabra[5] == letra:
            numletras[5] = letra
            printwin()
        elif len(palabra) >= 7 and palabra[6] == letra:
            numletras[6] = letra
            printwin()
        else:
            fallos += 1
            if fallos == 1:
                print(AHORCADO[1])
            elif fallos == 2:
                print(AHORCADO[2])
            elif fallos == 3:
                print(AHORCADO[3])
            elif fallos == 4:
                print(AHORCADO[4])
            elif fallos == 5:
                print(AHORCADO[5])
            elif fallos == 6:
                print(AHORCADO[6])
            elif fallos == 7:
                print(AHORCADO[7])
            elif fallos == 8:
                print(AHORCADO[8])
            elif fallos == 9:
                print(AHORCADO[9])

    except ValueError:
        print("Oops! Intentelo de nuevo...")

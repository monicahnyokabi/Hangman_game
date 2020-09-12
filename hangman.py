import random
from time import sleep
def hangman():
    print("_________")
    sleep(.7)
    print("|   |  ")
    sleep(.7)
    print("|   O  ")
    sleep(.7)
    print("|  \|/ ")
    sleep(.7)
    print("|   |  ")
    sleep(.7)
    print("|  / \ ")
    sleep(.7)
    print("|________")
    sleep(.7)
    print("\nHANGMAN\n")
    sleep(.7)
def hangman1():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|      ")
    print("|      ")
    print("|      ")
    print("|________")
def hangman2():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|   |  ")
    print("|   |  ")
    print("|      ")
    print("|________")
def hangman3():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|  \|  ")
    print("|   |  ")
    print("|      ")
    print("|________")
def hangman4():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|  \|/ ")
    print("|   |  ")
    print("|      ")
    print("|________")
def hangman5():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|  \|/ ")
    print("|   |  ")
    print("|  /   ")
    print("|________")
def hangman6():
    print("_________")
    print("|   |  ")
    print("|   O  ")
    print("|  \|/ ")
    print("|   |  ")
    print("|  / \ ")
    print("|________")
words = ['MOTTO', 'EDUCATION', 'AUTOMOBILE', 'EVACUATION', 'REMUNERATION', 'REGULATION', 'MISBEHAVIOUR',
         'AUTHORITIES', 'AUTHORIZE', 'AUTHENTICATION', 'PRECAUTION', 'MIRACULOUSNESS', 'MISDEMEANOUR',
         'PREAMBULATION', 'AURIFEROUS', 'MENSURATION', 'TAMBOURINE', 'UNOSTENTATIOUS', 'UNOBJECTIONABLE',
         'MULTIMILLIONAIRE', 'CONSEQUENTIAL', 'PRECARIOUS']
def intro():
    print("WELCOME TO HANGMAN\n")
    sleep(.7)
    print("ARE YOU READY TO GUESS SOME WORDS\n")
    sleep(.7)
    hangman()
intro()
def game_word_edits():
    global game_word
    global edit5
    game_word = random.choice(words)
    edit1 = game_word.replace("A","_")
    edit2 = edit1.replace("E","_")
    edit3 = edit2.replace("I","_")
    edit4 = edit3.replace("O","_")
    edit5 = edit4.replace("U","_")
    print()
    print("Your word to guess - ",edit5)
def game_word_list():
    global word_list_1
    global word_list_2
    space = " "
    word_space1 = space.join(game_word)
    word_space2 = space.join(edit5)
    word_list_1 = word_space1.split()
    word_list_2 = word_space2.split()
def list_combine():
    global user_edit
    user_edit = ""
    for i in word_list_2:
        user_edit += i
    print("Your word to guess - ",user_edit)
def letter_indexs():
    index = []
    for i in word_list_1:
        if i == letter:
            ai = word_list_1.index(letter)
            index.append(ai)
            word_list_1[ai] = "_"
    for a in index:
        word_list_2[a] = letter
mistake = 0
def game_play():
    global letter
    global mistake
    user_input_string = ""
    user_input = input("\nHey! enter the letter here - ").upper()
    print("\n\n")
    user_input_string += user_input
    if user_input == "A" and "A" in game_word:
        letter = "A"
        if game_word.count("A") == 1:
            an = word_list_1.index("A")
            word_list_2[an] = "A"
            list_combine()
        elif game_word.count("A") > 1:
            letter_indexs()
            list_combine()
    elif user_input == "E" and "E" in game_word:
        letter = "E"
        if game_word.count("E") == 1:
            an = word_list_1.index("E")
            word_list_2[an] = "E"
            list_combine()
        elif game_word.count("E") > 1:
            letter_indexs()
            list_combine()
    elif user_input == "I" and "I" in game_word:
        letter = "I"
        if game_word.count("I") == 1:
            an = word_list_1.index("I")
            word_list_2[an] = "I"
            list_combine()
        elif game_word.count("I") > 1:
            letter_indexs()
            list_combine()
    elif user_input == "O" and "O" in game_word:
        letter = "O"
        if game_word.count("O") == 1:
            an = word_list_1.index("O")
            word_list_2[an] = "O"
            list_combine()
        elif game_word.count("O") > 1:
            letter_indexs()
            list_combine()
    elif user_input == "U" and "U" in game_word:
        letter = "U"
        if game_word.count("U") == 1:
            an = word_list_1.index("U")
            word_list_2[an] = "U"
            list_combine()
        elif game_word.count("U") > 1:
            letter_indexs()
            list_combine()
    elif user_input not in game_word:
        mistake += 1
        if mistake == 1:
            hangman1()
            print()
            print("Oops! That's not correct")
            print()
            list_combine()
        elif mistake == 2:
            hangman2()
            print()
            print("Oops! That's not correct")
            print()
            list_combine()
        elif mistake == 3:
            hangman3()
            print()
            print("Oops! That's not correct")
            print()
            list_combine()
        elif mistake == 4:
            hangman4()
            print()
            print("Oops! That's not correct")
            print()
            list_combine()
        elif mistake == 5:
            hangman5()
            print()
            print("Oops! That's not correct")
            print()
            list_combine()
        elif mistake == 6:
            hangman6()
            print()
            print("Oops! That's not correct")
            print()
            print("THE WORD IS - ",game_word)
            print("\nGAME OVER\n")
            return
    new_word()
    if mistake == 6:
        return
    else:
        game_play()
def new_word():
    if game_word == user_edit and mistake != 6:
        print("\n\nCONGRATULATIONS!!! YOU GUESSED IT \n\n")
        hangman()
        print("YOUR NEW WORD TO GUESS\n\n ")
        if __name__ == "__main__":
            game_word_edits()
            game_word_list()
            game_play()
    elif mistake == 6:
        return
def replay():
    ui = input("Do you want to play again (y/n)- ").upper()
    while ui not in ["Y","N","YES","NO"]:
        ui = input("Do you want to play again (y/n)- ").upper()
    if ui == "Y" or ui == "YES":
        global mistake
        mistake = 0
        if __name__ == "__main__":
            game_word_edits()
            game_word_list()
            game_play()
    elif ui == "N" or "NO":
        print("\nTHANK YOU FOR PLAYING\n ")
        quit()
    else:
        print("\nTHANK YOU FOR PLAYING\n ")
        quit()
if __name__ == "__main__":
    game_word_edits()
    game_word_list()
    game_play()
    hangman()
    while True:
        replay()
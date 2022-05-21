import sys
import random

game_level= input("Wybierz poziom trudności (łatwy/średni/trudny)")

if game_level== "łatwy":
    no_of_tries= 6
    print("Ilość prób: ", no_of_tries)
elif game_level== "średni":
    no_of_tries= 4
    print("Ilość prób: ", no_of_tries)
elif game_level== "trudny":
    no_of_tries= 2
    print("Ilość prób: ", no_of_tries)
else:
    print("Wprowadzono nieprawidłowe dane, spróbuj jeszcze raz")
    print()
    sys.exit(0)
    


wor= ["jak wytresować smoka", "shrek", "kot w butach", "barbie", "toystory", "hotel transylwania", "rybki z ferajny", "droga do el dorado"]
word=random.choice(wor)
used_letters= []

user_word= []

def find_indexes(word, letter):
    indexes= []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)


    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery:", used_letters)
    print()

for _ in word:
    user_word.append("_")

while True:
    letter= input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes= find_indexes(word, letter)

    if len(found_indexes) == 0:
        if used_letters.count(letter)>1:
            print("Już próbowano tę literę i dalej nie ma takiej litery.")
            print()
        else:
            print("Nie ma takiej litery.")
            print()
            no_of_tries -= 1

        if no_of_tries== 0:
            print("Koniec gry")
            sys.exit(0)
    
    else:
        for index in found_indexes:
            user_word[index]= letter

        if "".join(user_word)== word:
            print("Brawo! Słowo zostało odgadnięte!")
            print()
            print("Hasło: ", word)

            sys.exit(0)



    show_state_of_game()

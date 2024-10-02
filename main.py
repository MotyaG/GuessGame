import os
from random_word import RandomWords

randomWord = RandomWords().get_random_word()
randomWord2 = list(str(randomWord))
guessed = [False] * len(randomWord2)

def get_len_list():
    for i in range(len(randomWord2)):
        if guessed[i]:
            print(randomWord2[i], end=" ")
            os.system("clear")
        else:
            print("_", end=" ")
            os.system("clear")

get_len_list()

while True:
    character = input("\nEnter character: ")
    for i in range(len(randomWord2)):
        if randomWord2[i] == character:
            guessed[i] = True
    get_len_list()
    if all(guessed):
        print("\nCongratulations, you've guessed the word!")
        break

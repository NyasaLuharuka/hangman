from words import words
import random


def random_word(words):
    choice = random.choice(words)
    print(choice)
    return choice


def start():
    strike = 0
    choice = random_word(words)
    length = len(choice)
    user_gui = "_" * length
    print(user_gui)
    loop(choice, user_gui, length, strike)


def loop(choice, user_gui, length, strike):
    letter = user_input()
    print(check(choice, user_gui, length, letter, strike))
    loop(choice, user_gui, length, strike)


def user_input():
    letter = input("Enter a letter: ")
    if len(letter) == 1 and letter.isalpha():
        letter = letter.lower()
        return letter
    else:
        print("I'm sorry, please choose one uppercase letter...")
        user_input()


def check(choice, user_gui, length, letter, strike):
    correct = 0
    list_user_gui = list(user_gui)
    for i in range(length):
        if choice[i] == letter:
            list_user_gui[i] = letter
            correct += 1

    user_gui = ""
    for j in list_user_gui:
        user_gui = user_gui + j

    if correct == 0:
        strike += 1

    if strike >= 6:
        return f"You lost! The word was {choice.upper()}!"

    return user_gui


start()

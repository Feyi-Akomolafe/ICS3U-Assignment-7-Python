#!/usr/bin/env python3

# Created by: Feyi Akomolafe
# Created on: Dec 2022
# This program generates a random number and the user has to guess it

import random


def guess_number(user_guess, random_number):
    while True:
        try:
            if user_guess == random_number:
                return "Congratulations, you guessed the number!"
            else:
                return "Incorrect guess, please try again."
        except ValueError:
            return "Invalid Input."


def main():
    user_input = input("Guess the number between 1 and 25: ")
    user_guess = int(user_input)
    random_number = random.randint(1, 25)
    result = guess_number(user_guess, random_number)
    print(result)
    print("\nDone.")


if __name__ == "__main__":
    main()

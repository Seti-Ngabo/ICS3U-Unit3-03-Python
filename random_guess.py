#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program guesses a random number

import random


def main():
    # this function checks if the random number is correct
    number = random.randint(0, 50)
    # a number between 0 and 50
    
    # input
    guessed_number = int(input("Enter the number between 0 and 50: "))
    print("")

    # process and output
    if guessed_number == number:
        print("Correct")
    else:
        print("wrong, try again.")
        print("")
        print("Done")


if __name__ == "__main__":
    main()

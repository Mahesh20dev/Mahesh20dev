import random
from typing import List

name=input("enter your name")
print("good luck!", name)
l = ["lion","tiger","cheetah","elephant","dinosour","peacock"]
word = random.choice(l)
print("guess the characters")
guesess = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesess:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("you win")
        print("the word is", word)
        break
    print()
    guess = input("guess the character")
    guesess += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have",+turns,"only")
        if turns == 0:
            print("you loose")
from random import randint


class NumberGuesser:
    def __init__(self):
        self.number = randint(1, 100)
        self.still_guessing = True

    def guess_number(self):
        print("Welcome to the number guessing game! ")

        while self.still_guessing:
            guess = int(input("\nPlease enter your guess: "))
            if guess < self.number:
                print("Sorry your guess was too low..")
            elif guess > self.number:
                print("Sorry your guess was too high..")
            else:
                print("Congratulations you guessed the correct number!")
                self.still_guessing = False


NumberGuesser().guess_number()

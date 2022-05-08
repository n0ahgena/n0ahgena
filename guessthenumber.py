from random import randrange

def print_description():
    print("Welcome to Guess the Number")
    print("I have selected a secret number in the range 1...100")
    print("You must guess the number within 10 tries.")
    print("I will tell you if you are high or low, and")
    print("I will tell you if you are hot or cold.")

def get_guess(guess_number):
    prompt = "(" + str(guess_number) + ") Enter your guess:"
    guess = input(prompt)
    guess = int(guess)
    return guess

def print_hints(secret, guess):
    if guess > 100 or guess < 1:
        print ("out of range")
    else:
        if guess > secret:
            print("too high")
        if guess < secret:
            print("too low")

    if guess < secret - 10 or guess > secret + 10:
        print("cold")
    elif guess < secret - 5 or guess > secret + 5:
        print("warmer")
    else:
        print("on fire")



def main ():
    print_description()
    secret = randrange(1,100)
    current_guess = get_guess(1)

    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(2)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(3)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(4)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(5)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(6)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(7)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(8)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(9)
    if current_guess != secret:
        print_hints(secret, current_guess)
        current_guess = get_guess(10)


    if current_guess == secret:
        print("Congratulations, you win!")

    else:
        print("Please play again,")

    print("The secret number was", secret)


main()

import random


def play():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play()
    
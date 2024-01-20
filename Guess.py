import random
import time

def print_slow(text, delay=0.05, color=None):
    for char in text:
        if color:
            print(f"\033[{color}m{char}\033[0m", end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_colorful_text(text, colors):
    words = text.split()
    for i, color in enumerate(colors):
        print(f"\033[{color}m{words[i]}\033[0m", end=' ')
    print()

def guess_the_number():
    print_slow("Welcome to the Guess the Number game!", delay=0.05, color="1;32")  # Green color
    print_colorful_text("Author: Adarsh Singh Rajput", ["1;31", "1;33", "1;35"])  # Red, Yellow, Magenta
    print_slow("I have selected a random number between 1 and 100. Can you guess it?", delay=0.05, color="1;34")  # Blue color

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print_slow(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.", delay=0.05, color="1;32")  # Green color
            break
        elif guess < secret_number:
            print_colorful_text("Too low! Try again.", ["1;31", "1;33", "1;35"])  # Red, Yellow, Magenta
        else:
            print_colorful_text("Too high! Try again.", ["1;31", "1;33", "1;35"])  # Red, Yellow, Magenta

if __name__ == "__main__":
    guess_the_number()

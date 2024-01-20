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

def get_names_with_gender(num_names):
    names_with_gender = []
    for i in range(num_names):
        name = input(f"Enter name {i + 1}: ")
        gender = input(f"Is {name} male or female? ").lower()
        while gender not in ["male", "female"]:
            print("Invalid input. Please enter 'male' or 'female'.")
            gender = input(f"Is {name} male or female? ").lower()
        names_with_gender.append((name, gender))
    return names_with_gender

def create_pairs(names_with_gender):
    male_names = [name for name, gender in names_with_gender if gender == "male"]
    female_names = [name for name, gender in names_with_gender if gender == "female"]
    
    random.shuffle(male_names)
    random.shuffle(female_names)

    pairs = [(male_names[i], female_names[i]) for i in range(min(len(male_names), len(female_names)))]
    return pairs

def display_pairs(pairs):
    for pair in pairs:
        print_colorful_text(f"{pair[0]} and {pair[1]} are the best", ["1;31", "1;32", "1;33", "1;34", "1;35"])

def print_colorful_text(text, colors):
    words = text.split()
    for i, color in enumerate(colors):
        print(f"\033[{color}m{words[i]}\033[0m", end=' ')
    print()

def main():
    num_names = int(input("Enter the number of names you want to input: "))
    names_with_gender = get_names_with_gender(num_names)
    pairs = create_pairs(names_with_gender)
    display_pairs(pairs)

if __name__ == "__main__":
    main()

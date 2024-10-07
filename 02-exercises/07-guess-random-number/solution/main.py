import random

number_to_guess = random.randint(1, 10)

guess = int(input("Vælg et tal mellem 1 og 10: "))

correct_guess = number_to_guess == guess
print(f"Dit gæt er: {correct_guess}")

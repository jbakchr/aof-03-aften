import random

comp_number = random.randint(1, 10)
user_number = int(input("Vælg et tal mellem 1 og 10: "))

is_equal = comp_number == user_number
is_different = comp_number != user_number
is_greater = comp_number > user_number
is_less = comp_number < user_number

"""
Eksempler på strings (del 2)
"""

# Eksempel 1: 'slicing' af string
name = "Jonas Bak Phillipson"

first_name = name[:4]  # Jonas
middle_name = name[6:9]  # Bak
last_name = name[10:]  # Phillipson

last_three = name[-3:]  # son

even_chars = name[::2]
print(even_chars)  # JnsBkPilpo

reversed_name = name[::-1]  # nospillihP kaB sanoJ


# Eksempel 2: Metoder på strings
upper_txt = "Make me uppercase!"
print(upper_txt.upper())

strip_me = "  Please fix me   "
print(strip_me.strip())

grocery_list = "Apples, Bananas, Beers"
print(grocery_list.split(", "))


# Eksempel 3: Sammenkædning af strings ("String concatenation")
first_name = "Jonas "
last_name = " Phillipson"
full_name = first_name + last_name

title = "Benovelent Dictator for life"
man = "Guido van Rossum"
python_dictator = title + ": " + man


# Eksempel 4: Formatering af strings
character = "knights"
who_say = "Ni!"
sentence = "We are the {} who say: {}"
print(sentence.format(character, who_say))

person = "Guido van Rossum"
title = "Dictator"
txt = "Who is the {1} of Python? Answer: {0}"
print(txt.format(person, title))

first_name = "Jonas"
middle_name = "Bak"
last_name = "Phillipson"
print(f"Hi my name is {first_name} {middle_name} {last_name}")

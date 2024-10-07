"""
Eksempler på strings (del 1)
"""

# Eksempel 1: Strings med " og '
name_with_double_quotes = "Jonas"
name_with_single_quotes = "Sir Lancelot"


# Eksempel 2: Multiline strings - bevarer formateringen
multiline_string = """This is
a multiline
string"""


# Eksempel 3.1: Fuck up af flere "double quotes" i samme string - og løsning med "escape characters"
# fuck_up_one = "Hej, jeg hedder Jonas "The Man" Bak Phillipson"
fuck_up_one = 'Hej, jeg hedder Jonas "The Man" Bak Phillipson'


# Eksempel 3.2: Fuck up af flere 'single quotes' i samme string - og løsning med "escape characters"
# fuck_up_two = 'Guido van Rossum er 'Diktatoren' af Python'
fuck_up_two = "Guido van Rossum er 'Diktatoren' af Python"


# Eksempel 4: Strings er i realiteten en liste af karakterer (et 'iterable' objekt faktisk) - og kan derfor tilgå hver karakter
my_awesome_name = "Jonas"
# index    -->     01234
# længde   -->     12345
first_character = my_awesome_name[0]
last_character = my_awesome_name[len(my_awesome_name) - 1]


# Eksempel 5: Loop igennem en string
who_is_god = "JonASS"
for letter in who_is_god:
    print(letter)


# Eksempel 6: Få længden af en string
awesome_text = "Programming is awesome"
length_of_text = len(awesome_text)


# Eksempel 7: Tjek for text i string
txt = "The best things in life are free!"
print("free" in txt)

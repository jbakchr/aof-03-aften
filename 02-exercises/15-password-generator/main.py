"""
I denne opgave skal du kode en password generator, der giver brugeren et tilfældigt password bestående af det
antal karakterer, som brugeren selv angiver længden på.

I nedenstående har jeg givet dig noget kode som giver et tilfældigt tal mellem tallene 65 og 122.

Din opgave bliver derfor at spørge brugeren, hvor mange karakterer personens password skal være på, og så skabe
et tilfældigt password herudfra.

* HINT *
For at få en karakter ud fra et tal, skal du bruge en af Pythons indbyggede funktioner til at konvertere et tal til
en karakter.
"""

import random

random_number = random.randint(65, 122)

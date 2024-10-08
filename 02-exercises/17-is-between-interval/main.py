"""
I denne opgave skal du tjekke, hvorvidt en tilfældigt tal genereret af computeren er både større
end og mindre end 2 tal som en bruger definerer.

I nedenstående er du givet koden til, at computeren genererer et tilfældigt tal mellem 1 og 100.

Din opgave er således først at bede brugeren om et interval bestående af en form for "startværdi"
og en "slutværdi" - fx 'startværdi' sat af brugeren til 25, og 'slutværdi' sat af brugeren til 75 - 
og så tjekke, hvorvidt computeren tal både er større end 'startværdien' OG mindre end 'slutværdien'.

Print evt. resultatet ud.
"""

import random

random_number = random.randint(1, 100)

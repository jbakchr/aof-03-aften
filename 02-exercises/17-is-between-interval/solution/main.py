import random

random_number = random.randint(1, 100)

start = int(input("Indtast startværdi: "))
end = int(input("Indtast slutværdi: "))

is_between = start < random_number and random_number < end
print(is_between)

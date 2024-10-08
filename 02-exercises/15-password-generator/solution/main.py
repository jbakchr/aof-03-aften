import random

pwd_length = int(input("Hvor mange karakterer skal der være i dit password? "))

password = ""

for _ in range(0, pwd_length):
    char = chr(random.randint(65, 122))
    password += char

print(password)

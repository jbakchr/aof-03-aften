base = int(input("Indtast 'base' tallet: "))
exponent = int(input("Indtast 'exponent' tallet: "))

sum = 1

for _ in range(exponent):
    sum *= base

print(f"{base}^{exponent} = {sum}")

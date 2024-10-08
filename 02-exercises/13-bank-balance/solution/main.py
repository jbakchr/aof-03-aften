bills = [1000, 2500, 3700]

salary = float(input("Indtast løn: "))

expenses = 0

for i in range(3):
    expenses -= bills[i]

print(f"Du har {salary + expenses} tilbage af din løn")

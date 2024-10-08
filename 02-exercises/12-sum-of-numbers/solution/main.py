start = int(input("Indtast startværdi: "))
end = int(input("Indtast slutværdi: "))

sum = 0

for i in range(start, end + 1):
    sum += i

print(f"Summen af tallene mellem {start} og {end} er: {sum}")

# Multiplication Table ClassWork
Table = []

Range = int(input("Enter the range of the multiplication table: "))

for x in range(1, Range+1):
    row = []
    for y in range(1, Range+1):
        Mult = x*y
        row.append(Mult)
    Table.append(row)

for row in Table:
    print(" ".join(f"{num:3}" for num in row))
roof_height = 5
body_height = 2
body_width = 3

for i in range(roof_height):
    for j in range(roof_height - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Berechnung der Einrückung für den Body
padding = (2 * roof_height - 1 - body_width) // 2


for k in range(body_height):
    for l in range(padding):
        print(' ', end='')
    for l in range(body_width):
        print('#', end='')
    print()

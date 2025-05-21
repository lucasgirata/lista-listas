
numeros = []
pares = []

for i in range(1, 101):
    numeros.append(i)

    if i % 2 == 0:
        pares.append(i)

print(f"Números de 1 a 100: {numeros}")
print(f"Números pares de 1 a 100: {pares}")

pares = []
impares = []
ordem = []

for i in range(1, 11):

    if i % 2 == 0:
        pares.append(i)

    else:
        impares.append(i)

ordem.extend(pares)
ordem.extend(impares)

print(f"Números pares de 1 a 10: {pares}")
print(f"Números impares de 1 a 10: {impares}")
print(f"Números em ordem: {sorted(ordem)}")
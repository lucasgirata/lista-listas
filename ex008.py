
numeros = []
soma = 0

for i in range(1, 11):
    numeroElevado = i ** 2
    numeros.append(numeroElevado)
    soma += numeroElevado


print(f"Números de 1 a 10 elevados ao quadrado: {numeros}")
print(f"Soma de todos os números: {soma}")
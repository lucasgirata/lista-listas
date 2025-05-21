
palavras = ["Melancia", "Girafa", "Sal", "Camisa", "Meia"]

maior = palavras[0]
menor = palavras[0]

for palavra in palavras:

    tamanho = len(palavra)

    if len(maior) < tamanho:
        maior = palavra
    if len(menor) > tamanho:
        menor = palavra

print(palavra)
print(f"A maior palavra da lista é: {maior}")
print(f"A menor palavra da lista é: {menor}")

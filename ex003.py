
frase = input("Digite uma frase: ")

listaPalavras = frase.split()

listasSeparadas = [[listaPalavras] for listaPalavras in listaPalavras]

print(listasSeparadas)

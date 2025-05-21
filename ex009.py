import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random.shuffle(alfabeto)

letraCerta = random.choice(alfabeto)

print(alfabeto)
tentativa = int(input(f"Informe a posição (0 a {len(alfabeto)}) da letra {letraCerta} nas letras do alfabeto embaralhadas: "))

posicaoCerta = alfabeto.index(letraCerta)

if tentativa == posicaoCerta:
    print("Parabéns! Você acertou")
else:
    print("Ops! Você errou")
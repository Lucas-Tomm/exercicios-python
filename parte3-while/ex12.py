soma = 0
numero = int(input("Digite um número (0 encerra): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 encerra): "))

print(f"Soma: {soma}")

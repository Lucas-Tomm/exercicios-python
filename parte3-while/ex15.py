quantidade_positivos = 0
numero = int(input("Digite um número (0 encerra): "))

while numero != 0:
    if numero > 0:
        quantidade_positivos += 1
    numero = int(input("Digite um número (0 encerra): "))

print(f"Quantidade de números positivos: {quantidade_positivos}")

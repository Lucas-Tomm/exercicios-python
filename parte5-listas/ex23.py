numeros = [7, 14, 3, 21, 9]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"Maior valor: {maior}")

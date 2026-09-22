numero = int(input("Digite um número: "))

if numero < 0:
    print("O fatorial não é definido para números negativos.")
else:
    fatorial = 1
    for valor in range(1, numero + 1):
        fatorial *= valor
    print(f"Fatorial: {fatorial}")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"Maior: {primeiro_numero}")
elif segundo_numero > primeiro_numero:
    print(f"Maior: {segundo_numero}")
else:
    print("Os números são iguais")

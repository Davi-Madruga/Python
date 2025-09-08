numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

escolha = int(input("[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\n-> "))

if escolha == 1:
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")

elif escolha == 2:
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")

elif escolha == 3:
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")

elif escolha == 4:
    resultado = numero1 / numero2
    print(f"{numero1} / {numero2} = {resultado}")
    
else:
    print("Resposta Inválida")
def somar(historico,numero1,numero2):
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
    historico.append(f"{numero1} + {numero2} = {resultado}")

def subtrair(historico,numero1,numero2):
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")
    historico.append(f"{numero1} - {numero2} = {resultado}")

def multiplicar(historico,numero1,numero2):
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")
    historico.append(f"{numero1} * {numero2} = {resultado}")

def dividir(historico,numero1,numero2):
    resultado = numero1 / numero2
    print(f"{numero1} / {numero2} = {resultado}")
    historico.append(f"{numero1} / {numero2} = {resultado}")

def mostrar_historico(historico):
    for x in historico:
        print(x)

def limpar_historico(historico):
    historico.clear()

print("-=- Calculadora -=-")
historico = []
lista = [0,1,2,3]
while True:
    try:
        operacao = int(input("[0]SOMAR\n[1]SUBTRAIR\n[2]MULTIPLICAR\n[3]DIVIDIR\n[4]MOSTRAR HISTORICO\n[5]LIMPAR HISTORICO\n[6]SAIR\n->"))  
        if( operacao in lista):
            numero1 = int(input("Digite o numero1: "))
            numero2 = int(input("Digite o numero2: "))
            if( operacao == 0 ):
                somar(historico,numero1,numero2)

            elif( operacao == 1 ):
                subtrair(historico,numero1,numero2)

            elif( operacao == 2 ):
                multiplicar(historico,numero1,numero2)

            elif( operacao == 3 ):
                try:
                    dividir(historico,numero1,numero2)
                except ZeroDivisionError:
                    print("Não é possivel dividir por 0")
        elif( operacao == 4 ):
            mostrar_historico(historico)

        elif( operacao == 5 ):
            limpar_historico(historico)

        elif( operacao == 6 ):
            break
        else:
            print("ERRO")

    except ValueError:
        print("Resposta Inválida")
print("Obrigado, Até logo...")        
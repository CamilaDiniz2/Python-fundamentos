def soma(x1, x2):
    return x1 + x2

def sub(x1, x2):
    return x1 - x2

def mult(x1, x2):
    return x1 * x2

def div(x1, x2):
    return x1 / x2

print("Calculadora Python")
numOperacoes = int(input("Digite o número de operações que você deeja realizar: "))

count = 0;
while (count < numOperacoes):
    print("Qual será a operação de número " + str(count+1) + " que você deseja: ")

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exit")

    opcao = int(input("Digite a opção escolhida: "))

    x1 = int(input("Digite o primeiro número: "))
    x2 = int(input("Digite o segundo número : "))

    if (opcao == 1):
        print("Você escolheu a função Soma...")
        print("A soma dos números digitados é  " +str(soma(x1, x2)))

    elif (opcao == 2):
        print("Você escolheu a função Subtração...")
        print("A subtração dos números digitados é  " + str(sub(x1, x2)))

    elif (opcao == 3):
        print("Você escolheu a função Multiplicação...")
        print("A multiplicação dos números digitados é  " + str(mult(x1, x2)))

    elif (opcao == 4):
        print("Você escolheu a função Divisão...")
        print("A Divisão dos números digitados é  " + str(div(x1, x2)))

    count += 1
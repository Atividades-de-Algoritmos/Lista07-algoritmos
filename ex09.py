#
# autores:
# Michel Silva
#
# data: 25/06/2022

# Faça um programa que leia vários conjuntos de três valores reais e mostre para cada conjunto: sua soma,
# seu produto e sua média. O programa deve parar quando um conjunto não entrar com seus valores em ordem crescente.
#
# usando o laço while:
# entrada de dados

while continuar:
    valor1 = int(input("Digite o 1º valor: "))
    valor2 = int(input("Digite o 2º valor: "))
    valor3 = int(input("Digite o 3º valor: "))
    if valor1 > valor2 > valor3:
        print(f"A soma é: {valor1 + valor2 + valor3}")
        print(f"O produto é: {valor1 * valor2 * valor3}")
        print(f"A média é: {(valor1 + valor2 + valor3) / 3}")
        continuar = True
    else:
        print("Não foram digitados valores em ordem crescente")
        continuar = False


print("Fim do programa")

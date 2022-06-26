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
continuar = True # Inicializa a variável de continuidade com True
while continuar: # Laço infinito que não tem condição de parada (continua)
    valor1 = int(input("Digite o 1º valor: ")) # Recebe o 1º valor do conjunto
    valor2 = int(input("Digite o 2º valor: ")) # Recebe o 2º valor do conjunto
    valor3 = int(input("Digite o 3º valor: ")) # Recebe o 3º valor do conjunto
    if valor1 > valor2 > valor3: # Verifica se o 1º valor é maior que o 2º e se o 2º é maior que o 3º
        print(f"A soma é: {valor1 + valor2 + valor3}") # Imprime a soma dos valores do conjunto
        print(f"O produto é: {valor1 * valor2 * valor3}") # Imprime o produto dos valores do conjunto
        print(f"A média é: {(valor1 + valor2 + valor3) / 3}") # Imprime a média dos valores do conjunto
        continuar = True # Continua o laço infinito
    else: # Se o 1º valor não for maior que o 2º nem o 3º
        print("Não foram digitados valores em ordem crescente") # Imprime a mensagem de erro de valores não em ordem crescente
        continuar = False # Para o laço infinito e não continua


print("Fim do programa")

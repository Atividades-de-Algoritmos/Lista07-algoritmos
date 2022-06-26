#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
# 8.	 Faça um programa que leia vários inteiros positivos e mostre, no final, a soma dos números pares e a soma
# dos números ímpares. O programa de parar quando entrar um número maior que 1000.

# usando o laço for:
# entrada de dados
soma_pares = 0 # Inicializa a soma dos números pares com 0 (zero)
soma_impares = 0 # Inicializa a soma dos números ímpares com 0 (zero)
for i in range(1, 1001): # Laço que percorre os números de 1 a 1000 (n+1)
    valor = int(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    if valor > 1000: # Se o valor for maior que 1000
        break # Para o laço e sai do programa
    if valor % 2 == 0: # Se o valor for par (divisivel por 2)
        soma_pares += valor # Soma o valor lido a soma dos números pares
    else:
        soma_impares += valor # Soma o valor lido a soma dos números ímpares

# saída de dados
print(f"A soma dos números pares é: {soma_pares}") # Imprime a soma dos números pares de todos os valores lidos
print(f"A soma dos números ímpares é: {soma_impares}") # Imprime a soma dos números ímpares de todos os valores lidos
print("Fim do programa")



print("----------------------------------------------------")
# usando o laço while:
# entrada de dados
soma_pares = 0 # Inicializa a soma dos números pares com 0 (zero)
soma_impares = 0 # Inicializa a soma dos números ímpares com 0 (zero)
i = 1 # Inicializa o contador do laço com 1
while i <= 1000: # Laço que percorre os números de 1 a 1000 (n+1)
    valor = int(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    if valor > 1000: # Se o valor for maior que 1000
        break # Para o laço e sai do programa
    if valor % 2 == 0: # Se o valor for par (divisivel por 2)
        soma_pares += valor # Soma o valor lido a soma dos números pares
    else:
        soma_impares += valor # Soma o valor lido a soma dos números ímpares
    i += 1 # Incrementa o contador do laço

# saída de dados
print(f"A soma dos números pares é: {soma_pares}") # Imprime a soma dos números pares de todos os valores lidos
print(f"A soma dos números ímpares é: {soma_impares}") # Imprime a soma dos números ímpares de todos os valores lidos
print("Fim do programa")

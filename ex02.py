#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#

# 2.	Em linguagem Python, elabore um programa que leia n valores e mostre a soma de seus quadrados.
#
# usando o laço for
# entrada de dados
n = int(input("Digite o número de valores: ")) # Recebe o número de valores a serem lidos

# processamento de dados
soma = 0 # Inicializa a soma com 0 (zero)
for i in range(1, n+1): # Laço que percorre os números de 1 a n (n+1)
    valor = float(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    soma += valor ** 2 # Soma o quadrado do valor lido a soma

# saída de dados
print(f"A soma dos quadrados é: {soma}") # Imprime a soma dos quadrados de todos os valores lidos

print("Fim do programa com for")

# usando o laço while
# entrada de dados
n = int(input("Digite o número de valores: ")) # Recebe o número de valores a serem lidos

# processamento de dados
soma = 0 # Inicializa a soma com 0 (zero)
i = 1 # Inicializa o contador do laço com 1
while i <= n: # Laço que percorre os números de 1 a n (n+1)
    valor = float(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    soma += valor ** 2 # Soma o quadrado do valor lido a soma
    i += 1 # Incrementa o contador do laço

# saída de dados
print(f"A soma dos quadrados é: {soma}") # Imprime a soma dos quadrados de todos os valores lidos

print("Fim do programa com while")

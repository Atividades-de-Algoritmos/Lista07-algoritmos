#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
# 3.	Em linguagem Python, faça um programa que leia 10 inteiros positivos, ignorando não positivos,
# e imprima sua média.

# entrada e processamento
soma = 0 # Inicializa a soma com 0 (zero)
for i in range(1, 11): # Laço que percorre os números de 1 a 10 (n+1)
    valor = int(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    if valor > 0: # Se o valor for positivo
        soma += valor # Soma o valor lido a soma
    else:
        print("Valor inválido") # Imprime "Valor inválido"
        i -= 1 # Decrementa o contador do laço

# saída de dados
print(f"A média é: {soma/10}") # Imprime a média de todos os valores lidos
print("Fim do programa")

#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
# 4.	Em linguagem Python, escreva um programa que leia um número inteiro e calcule a soma de
# todos os divisores desse número, com exceção dele próprio. Ex. a soma dos divisores do
# número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

# entrada de dados
numero = int(input("Digite um número inteiro: ")) # Recebe o número a ser calculado os divisores

# processamento de dados
soma = 0 # Inicializa a soma com 0 (zero)
for i in range(1, numero): # Laço que percorre os números de 1 a n (n+1)
    if numero % i == 0: # Se o número for divisível por i
        soma += i  # Soma i a soma de divisores

# saída de dados
print(f"A soma dos divisores é: {soma}") # Imprime a soma dos divisores de todos os valores lidos
print("Fim do programa")

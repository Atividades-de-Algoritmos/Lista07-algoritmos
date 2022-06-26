#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# Faça um programa que leia um número n e mostre na tela os n primeiros números primos.
#
# entrada de dados
n = int(input("Digite um número: ")) # Recebe o número a ser testado

# processamento de dados
for i in range(1, n+1): # Laço que percorre os números de 1 a n (n+1)
    primo = True # Inicializa a variável primo como True (verdadeiro)
    for j in range(2, i): # Laço que percorre os números de 2 a i (i+1)
        if i % j == 0: # Se o número for divisível por j
            primo = False # Altera a variável primo para False (falso)
    if primo: # Se o número for primo
        print(i) # Imprime o número primo

# saída de dados
print("Fim do programa")


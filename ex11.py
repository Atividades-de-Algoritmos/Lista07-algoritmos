#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# Faça um programa que leia um número n e imprima se ele é primo ou não. (um número primo tem apenas 2
# divisores: 1 e ele mesmo! O número 1 não é primo!

# entrada de dados
n = int(input("Digite um número: ")) # Recebe o número a ser testado

# processamento de dados
# Verifica se o número é primo
primo = True # Inicializa a variável primo como True (verdadeiro)
for i in range(2, n): # Laço que percorre os números de 2 a n (n+1)
    if n % i == 0: # Se o número for divisível por i
        primo = False # Altera a variável primo para False (falso)

# saída de dados
if primo: # Se o número for primo
    print(f"O número {n} é primo") # Imprime que o número é primo
else: # Se o número não for primo
    print(f"O número {n} não é primo") # Imprime que o número não é primo
print("Fim do programa")

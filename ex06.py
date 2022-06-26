#
#
# autores:
# Emanuel Franklyn
# 
# data: 25/06/2022
#
# 6. Faça um programa algoritmo para exibir a tabuada de 0 a 9.

for i in range(0, 10): # Laço de repetição que percorre os números de 0 a 9 (n+1) e armazena o valor na variável i
  for j in range(0, 10): # Laço de repetição que percorre os números de 0 a 9 (n+1) e armazena o valor na variável j
    print(f"{i} x {j} = {i * j}") # Imprime o resultado da multiplicação de i e j

print("Fim do programa") # Informa ao usuário que o programa terminou
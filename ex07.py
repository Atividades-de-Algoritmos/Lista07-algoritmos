#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
#  7 - Escreva um algoritmo que gera números entre 1000 e 1999 e mostra aqueles que divididos por 11 dão resto 5.

# entrada de dados
for i in range(1000, 2000): # Laço que percorre os números de 1000 a 1999 (n+1)
    if i % 11 == 5: # Se o resto da divisão por 11 do número lido for 5
        print(i) # Imprime o número lido

# saída de dados
print("Fim do programa")

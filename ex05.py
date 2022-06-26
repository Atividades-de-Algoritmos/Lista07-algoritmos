#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
#  5.	Escreva um algoritmo em Python que lê 15 valores reais, encontra o maior e o menor
#  deles e mostra o resultado.

# entrada de dados
maior = 0 # Inicializa o maior com 0 (zero)
menor = 0 # Inicializa o menor com 0 (zero)
for i in range(1, 16): # Laço que percorre os números de 1 a 15 (n+1)
    valor = float(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
    if i == 1: # Se for o primeiro valor lido
      maior = valor # Atribui o valor lido ao maior
      menor = valor # Atribui o valor lido ao menor
    else:
      if valor > maior: # Se o valor lido for maior que o maior
        maior = valor # Atribui o valor lido ao maior
      else:
        if valor < menor: # Se o valor lido for menor que o menor
          menor = valor # Atribui o valor lido ao menor

# saída de dados
print(f"O maior valor é: {maior}") # Imprime o maior valor  lido
print(f"O menor valor é: {menor}") # Imprime o menor valor  lido
print("Fim do programa")



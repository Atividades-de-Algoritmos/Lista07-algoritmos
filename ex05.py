#
#
# autores:
# Michel Silva
# 
#
# data: 25/06/2022
#
# 5. Escreva um algoritmo em Python que lê 15 valores reais, encontra o maior e o menor
# deles e mostra o resultado.

# entrada de dados
maior = 0 # Inicializa a variável maior com o valor 0 (zero)
menor = 0 # Inicializa a variável menor com o valor 0 (zero)

for i in range(1, 16): # Laço de repetição que percorre os números de 1 a 15 (n+1) e armazena o valor na variável i
  valor = float(input(f"Digite o {i}º valor: ")) # Recebe o valor do i-ésimo número a ser lido
  
  if i == 1: # Se for o primeiro valor lido
    maior = valor # Atribui o valor lido à variável maior
    menor = valor # Atribui o valor lido à variável menor
  
  else: # Caso contrário, se for um valor diferente do primeiro
    if valor > maior: # Se o valor lido for maior que o maior já registrado
      maior = valor # Atribui o valor lido à variável maior
    
    elif valor < menor: # Caso contrário, se o valor lido for menor que o menor já registrado
      menor = valor # Atribui o valor lido à variável menor
    
    # Se o valor for igual ao maior ou ao menor, não faz nada pois não há necessidade de alterá-los
    # Logo, não precisamos usar o else nesse caso específico

# saída de dados
print(f"O maior valor é: {maior}") # Imprime a variável maior
print(f"O menor valor é: {menor}") # Imprime a variável menor

print("Fim do programa") # Informa ao usuário que o programa terminou
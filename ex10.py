#
#
# autores:
# Michel Silva
#
# data: 25/06/2022
#
# 10.	 Faça um programa que leia as médias finais de vários alunos de uma turma e mostre a maior média, a menor média
# e a média aritmética da turma. O programa deve parar quando encontrar uma média negativa.
#
# usando o laço while:
# entrada de dados
soma_medias = 0 # Inicializa a soma das médias com 0 (zero)
media_aritmetica = 0 # Inicializa a média aritmética com 0 (zero)
media_maior = 0 # Inicializa a média máxima com 0 (zero)
media_menor = 0 # Inicializa a média mínima com 0 (zero)
i = 0 # Inicializa o contador do laço com 0
contador = 0 # Inicializa o contador de alunos com 0
continuar = True # Inicializa a variável de continuidade com True (verdadeiro)

while continuar: # Laço infinito que não tem condição de parada
    media = float(input("Digite a média do aluno: ")) # Recebe a média do aluno
    if media > 0: # Se a média for positiva
        soma_medias += media # Soma a média a soma das médias
        contador += 1 # Incrementa o contador de alunos
        if contador == 1: # Se o contador de alunos for 1
            media_maior = media # Atribui a média do aluno a média máxima
            media_menor = media # Atribui a média do aluno a média mínima
        else: # Se o contador de alunos for maior que 1
            if media > media_maior: # Se a média do aluno for maior que a média máxima
                media_maior = media # Atribui a média do aluno a média máxima
            if media < media_menor: # Se a média do aluno for menor que a média mínima
                media_menor = media # Atribui a média do aluno a média mínima
    else: # Se a média for negativa
        continuar = False # Para o laço infinito e não continua
        print("Fim do programa")
    i += 1 # Incrementa o contador do laço
    media_aritmetica = soma_medias / contador # Calcula a média aritmética
    print(f"A média aritmética da turma é: {media_aritmetica}") # Imprime a média aritmética
    print(f"A média máxima é: {media_maior}") # Imprime a média máxima
    print(f"A média mínima é: {media_menor}") # Imprime a média mínima
    print(f"A soma das médias é: {soma_medias}") # Imprime a soma das médias
    print(f"O número de alunos é: {contador}") # Imprime o número de alunos
    print(f"O número de iterações é: {i}") # Imprime o número de iterações
    print("") # Imprime uma linha em branco

print("Fim do programa")



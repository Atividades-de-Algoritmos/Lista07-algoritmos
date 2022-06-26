#
# autores:
# Michel Silva
#
# data: 25/06/2022

# 1.	Faça um programa que simula uma calculadora que aceita as seguintes operações: soma, subtração, divisão e
# multiplicação. O programa inicia pedindo para o usuário escolher uma opção do menu:
# 1. Somar
# 2. Subtrair
# 3. Dividir
# 4. Multiplicar
# 5. Sair.
# Ao escolher a opção, o programa solicita os dois números a serem operados (exceto se a opção escolhida for a 5),
# efetua a operação, mostra o resultado na tela e volta para o menu para que o usuário escolha outra opção.
#
# obs:  essa solução é sem estrutura de repetição

# entrada de dados
print("*** Calculadora ***")
print("1. Somar")
print("2. Subtrair")
print("3. Dividir")
print("4. Multiplicar")
print("5. Sair")
opcao = int(input("Digite a opção desejada: ")) # Recebe a opção desejada do usuário
valor1 = float(input("Digite o primeiro valor: ")) # Recebe o primeiro valor
valor2 = float(input("Digite o segundo valor: ")) # Recebe o segundo valor

# processamento de dados
if opcao == 1: # Se a opção for 1 (somar)
    resultado = valor1 + valor2 # soma
    print(f"O resultado da soma é: {resultado}")
elif opcao == 2: # Se a opção for 2 (subtrair)
    resultado = valor1 - valor2 # subtração
    print(f"O resultado da subtração é: {resultado}")
elif opcao == 3: # Se a opção for 3 (dividir)
    resultado = valor1 / valor2 # divisão
    print(f"O resultado da divisão é: {resultado}")
elif opcao == 4: # Se a opção for 4 (multiplicar)
    resultado = valor1 * valor2 # multiplicação
    print(f"O resultado da multiplicação é: {resultado}")
elif opcao == 5: # Se a opção for 5 (sair)
    print("Saindo...") # Imprime "Saindo..."
else: # Se a opção for diferente de 1, 2, 3, 4 e 5
    print("Opção inválida") # Imprime "Opção inválida"
    resultado = 0 # resultado é 0 (zero)

print("Fim do programa")


# Peça dis números para o usuário e imprima a soma, subtração, multiplicação e divisão entre eles.

# Também mostre se os números são iguais ou não.

numero1 = float(input("Digite o primeiro número: ")) # Convertendo para float para permitir números decimais. Exemplo: 1.5
numero2 = float(input("Digite o segundo número: ")) # Convertendo para float para permitir números decimais. Exemplo: 2.5

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

igual = numero1 == numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Os números são iguais?", igual)
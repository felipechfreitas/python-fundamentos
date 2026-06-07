# DESAFIO CONDICIONAL COM INPUT

# Crie um programa que solicite ao usuário sua idade e imprima se ele é maior de idade ou não.

# Dica: Use a função input() para obter a idade do usuário e converta-a para um número inteiro usando a função int().

idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# ==============================
# DESAFIO CONDICIONAL COM MULTIPLAS CONDIÇÕES
# ==============================

nota = 6

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

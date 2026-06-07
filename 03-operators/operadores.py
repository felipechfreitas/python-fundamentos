# Operadores em Python

# ==============================
# OPERADORES ARITMÉTICOS
# ==============================

a = 10
b = 3

print(a + b)  # Soma
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão
print(a // b) # Divisão inteira
print(a % b)  # Resto da divisão
print(a ** b) # Potência

# Ou dessa forma:

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto:", a % b)
print("Potência:", a ** b)

# ==============================
# OPERADORES DE COMPARAÇÃO
# ==============================

idade = 18

print(idade == 18)  # Igual
print(idade != 18)  # Diferente
print(idade > 18)   # Maior
print(idade < 18)   # Menor
print(idade >= 18)  # Maior ou igual
print(idade <= 18)  # Menor ou igual

# Exemplo de comparação:

nota = 7

print(nota >= 6)  # True
print(nota < 6)   # False

# ==============================
# OPERADORES LÓGICOS
# ==============================

idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira) # Verdadeiro/True se a pessoa tem 18 anos ou mais E tem carteira

print(idade >= 18 or tem_carteira) # Verdadeiro/True se a pessoa tem 18 anos ou mais OU tem carteira

print(not tem_carteira) # Verdadeiro/True se a pessoa NÃO tem carteira

# Se tem_carteira = True, o resultado será False
# Se tem_carteira = False, o resultado será True

# ==============================
# OPERADORES DE ATRIBUIÇÃO
# ==============================

numero = 10

numero += 5 # equivalente a numero = numero + 5
print(numero) # output: 15

numero -= 2 # equivalente a numero = numero - 2
print(numero) # output: 13

numero *= 3 # equivalente a numero = numero * 3
print(numero) # output: 39

numero /= 2 # equivalente a numero = numero / 2
print(numero) # output: 19.5
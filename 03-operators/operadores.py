# Operadores em Python

# ==============================
# OPERADORES ARITMÉTICOS
# ==============================

a = 10
b = 3

print(a + b)   # Soma
print(a - b)   # Subtração
print(a * b)   # Multiplicação
print(a / b)   # Divisão
print(a // b)  # Divisão inteira
print(a % b)   # Resto da divisão
print(a ** b)  # Potência

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

# Exemplo prático

nota = 7

print(nota >= 6)  # True
print(nota < 6)   # False

# ==============================
# OPERADORES LÓGICOS
# ==============================

idade = 20
tem_carteira = True

# Ambas as condições precisam ser verdadeiras
print(idade >= 18 and tem_carteira)

# Basta uma das condições ser verdadeira
print(idade >= 18 or tem_carteira)

# Inverte o valor booleano
print(not tem_carteira)

# Se tem_carteira = True, o resultado será False
# Se tem_carteira = False, o resultado será True

# ==============================
# COMPARAÇÃO DE BOOLEANOS
# ==============================

print(True == True)     # True
print(True == False)    # False
print(False == False)   # True

print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# ==============================
# COMPARAÇÃO LÓGICA
# ==============================

print(3 > 2 and 4 > 3) # True - porque ambas as condições são verdadeiras
print(3 > 2 and 4 < 3) # False - porque a segunda condição é falsa
print(3 < 2 and 4 < 3) # False - porque ambas as condições são falsas

print(3 > 2 or 4 > 3) # True - porque ambas as condições são verdadeiras
print(3 > 2 or 4 < 3) # True - porque a primeira condição é verdadeira, mesmo que a segunda seja falsa
print(3 < 2 or 4 < 3) # False - porque ambas as condições são falsas

print(not 3 > 2) # False - porque 3 é realmente maior que 2, então o resultado de not é False
print(not 3 < 2) # True - porque 3 não é menor que 2, então o resultado de not é True

print(not True) # False
print(not False) # True

print(not not True) # True - porque o primeiro not inverte para False, e o segundo not inverte de volta para True
print(not not False) # False - porque o primeiro not inverte para True, e o segundo not inverte de volta para False

# ==============================
# COMPARAÇÃO DE STRINGS
# ==============================

nome1 = "Alice"
nome2 = "Bob"

print(nome1 == nome2) # False - porque "Alice" e "Bob" são strings diferentes
print(nome1 != nome2) # True - porque "Alice" e "Bob" são strings diferentes

print(nome1 == "Alice") # True - porque nome1 é igual a "Alice"
print(nome2 == "Bob") # True - porque nome2 é igual a "Bob"

print("A" in nome1) # True - porque a letra "A" está presente na string "Alice"
print("B" in nome1) # False - porque a letra "B" não está presente na string "Alice"

print("A" in nome2) # False - porque a letra "A" não está presente na string "Bob"
print("B" in nome2) # True - porque a letra "B" está presente na string "Bob"

# ==============================
# OPERADORES DE ATRIBUIÇÃO
# ==============================

numero = 10

numero += 5
print(numero)  # 15

numero -= 2
print(numero)  # 13

numero *= 3
print(numero)  # 39

numero /= 2
print(numero)  # 19.5

# ==============================
# PRECEDÊNCIA DE OPERADORES
# ==============================

resultado = 10 + 5 * 2
print(resultado)  # 20

resultado = (10 + 5) * 2
print(resultado)  # 30
# Listas em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Listas armazenam múltiplos valores.
# 2. São definidas usando colchetes [].
# 3. Cada item possui um índice.
# 4. Índices começam em 0.
# 5. Listas podem ser alteradas.
# 6. Permitem adicionar, remover e modificar itens.

# ==============================
# 1. Criando listas
# ==============================

frutas = ["Maçã", "Banana", "Laranja"]

print(frutas) # output: ['Maçã', 'Banana', 'Laranja']
print(type(frutas)) # output: <class 'list'>

# ==============================
# 2. Acessando elementos
# ==============================

print(frutas[0])  # output: Maçã
print(frutas[1])  # output: Banana
print(frutas[2])  # output: Laranja

# ==============================
# 3. Alterando valores
# ==============================

frutas[1] = "Uva" # o que era "Banana" foi alterado para "Uva"

print(frutas) # output: ['Maçã', 'Uva', 'Laranja']

# ==============================
# 4. Tamanho da lista
# ==============================

print(len(frutas)) # output: 3

# ==============================
# 5. Percorrendo lista com for
# ==============================

for fruta in frutas:
    print(fruta)

# Maçã
# Uva
# Laranja

# ==============================
# 6. Utilizando enumerate()
# ==============================

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# output
# 0 Maçã
# 1 Uva
# 2 Laranja

# ==============================
# 7. Verificando existência
# ==============================

print("Maçã" in frutas) # output: True
print("Pera" in frutas) # output: False

# ==============================
# 8. Lista com tipos diferentes
# ==============================

dados = ["Felipe", 31, 1.90, True]

print(dados) # output: ['Felipe', 31, 1.9, True]
print(type(dados[0])) # output: <class 'str'>
print(type(dados[1])) # output: <class 'int'>
print(type(dados[2])) # output: <class 'float'>
print(type(dados[3])) # output: <class 'bool'>

# ==============================
# 9. Lista vazia
# ==============================

tarefas = []

print(tarefas) # output: []

# ==============================
# 10. Lista dentro de lista
# ==============================

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz) # output: [[1, 2, 3], [4, 5, 6]]

print(matriz[0]) # output: [1, 2, 3]
print(matriz[1]) # output: [4, 5, 6]
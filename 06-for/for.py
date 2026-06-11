# For em Python

# ==============================
# 1. Estrutura Básica
# ==============================

# O for é utilizado para percorrer elementos de uma sequência.

nomes = ["Felipe", "João", "Maria"]

for nome in nomes:
    print(nome)

# ==============================
# 2. Utilizando range()
# ==============================

# range(5) gera números de 0 até 4

for numero in range(5):
    print(numero)

# ==============================
# 3. Definindo início e fim
# ==============================

for numero in range(1, 6):
    print(numero)

# Saída/Print:
# 1
# 2
# 3
# 4
# 5

# ==============================
# 4. Definindo intervalo
# ==============================

# Conta de 2 em 2

for numero in range(0, 11, 2):
    print(numero)

# Saída/Print:
# 0
# 2
# 4
# 6
# 8
# 10

# ==============================
# 5. Percorrendo Strings
# ==============================

nome = "Python"

for letra in nome:
    print(letra)

# ==============================
# 6. Utilizando enumerate()
# ==============================

# O enumerate() permite percorrer uma lista e obter:
# - o índice (posição)
# - o valor armazenado

tarefas = ["Python", "GitHub", "LinkedIn"]

for indice, tarefa in enumerate(tarefas):
    print(indice, tarefa)

# Saída:
# 0 Python
# 1 GitHub
# 2 LinkedIn

# Explicação:
# A lista possui índices começando em 0.

# Índice | Valor
# -------|-----------
#    0   | Python
#    1   | GitHub
#    2   | LinkedIn

# O enumerate() retorna os dois valores ao mesmo tempo:
# indice -> posição do item
# tarefa -> valor armazenado naquela posição

# ==============================
# 7. Enumerate iniciando em 1
# ==============================

# Em muitos casos não queremos mostrar índices começando em 0
# para o usuário.

for indice, tarefa in enumerate(tarefas, start=1):
    print(f"{indice} - {tarefa}")

# Saída:
# 1 - Python
# 2 - GitHub
# 3 - LinkedIn

# Explicação:
# O parâmetro start=1 faz a contagem começar em 1
# apenas na exibição.

# A lista continua armazenada internamente assim:

# Índice real | Valor
# ------------|-----------
#      0      | Python
#      1      | GitHub
#      2      | LinkedIn

# Isso é muito útil para menus e listas exibidas ao usuário.

# Exemplo real utilizado no projeto Lista de Tarefas:

# for indice, tarefa in enumerate(tarefas, start=1):
#     print(f"{indice} - {tarefa}")

# Depois, para remover:

# escolha = int(input("Qual tarefa deseja remover? "))
# indice_remover = escolha - 1

# Subtraímos 1 porque o usuário vê a lista começando em 1,
# mas o Python continua armazenando os índices começando em 0.

# ==============================
# 8. Somando valores
# ==============================

numeros = [10, 20, 30]

soma = 0

for numero in numeros:
    soma += numero

print("Soma:", soma)

# ==============================
# 9. Utilizando break
# ==============================

for numero in range(10):
    if numero == 5:
        break

    print(numero)

# O loop para quando encontra o número 5

# ==============================
# 10. Utilizando continue
# ==============================

for numero in range(5):
    if numero == 2:
        continue

    print(numero)

# O número 2 será ignorado

# ==============================
# 11. Exemplo prático
# ==============================

frutas = ["Maçã", "Banana", "Laranja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")
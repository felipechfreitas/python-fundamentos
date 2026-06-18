# Métodos de Listas em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Métodos são funções que pertencem a um objeto.
# 2. Listas possuem métodos próprios para adicionar,
#    remover, ordenar e manipular elementos.
# 3. Os métodos mais usados são:
#    append(), insert(), remove(), pop(),
#    sort(), reverse(), clear() e count().

# ==============================
# 1. append()
# ==============================

# Adiciona um item ao final da lista.

tarefas = ["Python", "GitHub"]

tarefas.append("LinkedIn")

print(tarefas)

# Saída:
# ['Python', 'GitHub', 'LinkedIn']

# ==============================
# 2. insert()
# ==============================

# Adiciona um item em uma posição específica.

tarefas = ["Python", "GitHub"]

tarefas.insert(1, "SQL")

print(tarefas)

# Saída:
# ['Python', 'SQL', 'GitHub']

# ==============================
# 3. remove()
# ==============================

# Remove um item pelo valor.

linguagens = ["Python", "Java", "SQL"]

linguagens.remove("Java")

print(linguagens)

# Saída:
# ['Python', 'SQL']

# ==============================
# 4. pop()
# ==============================

# Remove um item pelo índice.

frutas = ["Maçã", "Banana", "Laranja"]

fruta_removida = frutas.pop(1)

print(frutas)
print(fruta_removida)

# Saída:
# ['Maçã', 'Laranja']
# Banana

# ==============================
# 5. sort()
# ==============================

# Ordena a lista em ordem crescente.

numeros = [5, 2, 8, 1]

numeros.sort()

print(numeros)

# Saída:
# [1, 2, 5, 8]

# ==============================
# 6. reverse()
# ==============================

# Inverte a ordem dos elementos.

nomes = ["Felipe", "Maria", "João"]

nomes.reverse()

print(nomes)

# Saída:
# ['João', 'Maria', 'Felipe']

# ==============================
# 7. count()
# ==============================

# Conta quantas vezes um valor aparece.

numeros = [1, 2, 3, 1, 1, 5]

print(numeros.count(1))

# Saída:
# 3

# ==============================
# 8. index()
# ==============================

# Retorna o índice de um elemento.

frutas = ["Maçã", "Banana", "Laranja"]

print(frutas.index("Banana"))

# Saída:
# 1

# ==============================
# 9. clear()
# ==============================

# Remove todos os itens da lista.

tarefas = ["Python", "GitHub", "SQL"]

tarefas.clear()

print(tarefas)

# Saída:
# []

# ==============================
# 10. len()
# ==============================

# Retorna a quantidade de itens da lista.

tarefas = ["Python", "GitHub", "SQL"]

print(len(tarefas))

# Saída:
# 3

# ==============================
# 11. Exemplo prático
# ==============================

tarefas = []

tarefas.append("Estudar Python")
tarefas.append("Praticar Git")
tarefas.append("Criar projeto")

print(tarefas)

tarefas.remove("Praticar Git")

print(tarefas)

# Saída:
# ['Estudar Python', 'Praticar Git', 'Criar projeto']
# ['Estudar Python', 'Criar projeto']
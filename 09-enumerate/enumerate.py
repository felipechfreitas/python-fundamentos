# Enumerate em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. enumerate() adiciona um índice a cada item de uma lista.
# 2. Muito utilizado junto com loops for.
# 3. Evita criar contadores manualmente.
# 4. Retorna índice e valor ao mesmo tempo.
# 5. Sintaxe: enumerate(iteravel, start=0)
#    - iteravel: lista, string, tupla ou qualquer sequência.
#    - start: define em qual número a contagem começa.
# 6. A cada volta do loop, o enumerate() retorna dois valores:
#    (indice, valor)
# 7. O primeiro valor retornado vai para a primeira variável
#    do for, e o segundo valor vai para a segunda variável.
# 8. Os nomes das variáveis podem ser quaisquer nomes,
#    mas normalmente usamos "indice" e "valor" para facilitar a leitura.

# ==============================
# 1. For comum
# ==============================

frutas = ["Maçã", "Banana", "Laranja"]

for fruta in frutas:
    print(fruta)

# ==============================
# 2. For com enumerate
# ==============================

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# Saída:
# 0 Maçã
# 1 Banana
# 2 Laranja

# ==============================
# 3. Exibindo numeração amigável
# ==============================

for indice, fruta in enumerate(frutas):
    print(f"{indice + 1} - {fruta}")

# Saída:
# 1 - Maçã
# 2 - Banana
# 3 - Laranja

# ==============================
# 4. Enumerate com lista de nomes
# ==============================

nomes = ["Felipe", "Maria", "João"]

for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")

# O enumerate() gera internamente algo parecido com:

# Output
# Posição 0: Felipe
# Posição 1: Maria
# Posição 2: João

# ==============================
# 5. Enumerate iniciando em outro número
# ==============================

for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

# Saída:
# 1 Maçã
# 2 Banana
# 3 Laranja

# ==============================
# 6. Exemplo semelhante ao projeto
# ==============================

tarefas = [
    "Estudar Python",
    "Praticar Git",
    "Atualizar LinkedIn"
]

for indice, tarefa in enumerate(tarefas, start=1):
    print(f"{indice} - {tarefa}")

# output
# 1 - Estudar Python
# 2 - Praticar Git
# 3 - Atualizar LinkedIn

# ==============================
# 7. Sem enumerate (mais trabalhoso)
# ==============================

contador = 0

for fruta in frutas:
    print(contador, fruta)
    contador += 1

# O enumerate faz isso automaticamente.
# Tuplas em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Tuplas armazenam múltiplos valores.
# 2. São definidas utilizando parênteses ().
# 3. Mantêm a ordem dos elementos.
# 4. Permitem elementos repetidos.
# 5. São imutáveis (não podem ser alteradas).
# 6. São mais rápidas que listas em algumas situações.
# 7. Muito utilizadas para dados que não devem mudar.

# ==============================
# 1. Criando uma tupla
# ==============================

frutas = ("Maçã", "Banana", "Laranja")

print(frutas) # Saída: ('Maçã', 'Banana', 'Laranja')
print(type(frutas)) # Saída: <class 'tuple'>

# ==============================
# 2. Acessando elementos
# ==============================

print(frutas[0]) # Maçã
print(frutas[1]) # Banana
print(frutas[2]) # Laranja

# ==============================
# 3. Tamanho da tupla
# ==============================

print(len(frutas)) # 3

# ==============================
# 4. Percorrendo uma tupla
# ==============================

for fruta in frutas:
    print(fruta)

# Saída
# Maçã
# Banana
# Laranja

# ==============================
# 5. Verificando existência
# ==============================

print("Banana" in frutas) # True
print("Uva" in frutas) # False

# ==============================
# 6. Tuplas permitem repetição
# ==============================

numeros = (1, 2, 3, 1, 2, 1)

print(numeros) # Saída: (1, 2, 3, 1, 2, 1)

# ==============================
# 7. Contando elementos
# ==============================

print(numeros.count(1)) # Saída: 3
print(numeros.count(2)) # Saída: 2

# ==============================
# 8. Encontrando posição
# ==============================

print(numeros.index(3)) # Saída: 2. Está na segunda posição da tupla

# ==============================
# 9. Tupla com diferentes tipos
# ==============================

dados = (
    "Felipe",
    31,
    True,
    1.90
)

print(dados) # Saída: ('Felipe', 31, True, 1.9)

# ==============================
# 10. Desempacotamento
# ==============================

nome, idade, ativo, altura = dados

print(nome) # Felipe
print(idade) # 31
print(ativo) # True
print(altura) # 1.9

# ==============================
# 11. Convertendo tupla para lista
# ==============================

frutas_lista = list(frutas)

print(frutas_lista) # Saída: ['Maçã', 'Banana', 'Laranja'] . Como pode ver, alterou para lista, pois ficou entre chaves.
print(type(frutas_lista)) # saída: <class 'list'>

# ==============================
# 12. Convertendo lista para tupla
# ==============================

nomes = ["Felipe", "Maria", "João"] # É um dict

nomes_tupla = tuple(nomes) # variavel nomes_tupla armazena os nomes em tuplas

print(nomes_tupla) # Saída: ('Felipe', 'Maria', 'João')
print(type(nomes_tupla)) # Saída: <class 'tuple'>

# ==============================
# 13. Tupla com um único elemento
# ==============================

linguagem = ("Python",)

print(linguagem) # Saída: ('Python',)
print(type(linguagem)) # Saída: <class 'tuple'>

# Sem a vírgula não é uma tupla

texto = ("Python")

print(type(texto)) # <class 'str'>

# ==============================
# 14. Exemplo semelhante a projetos
# ==============================

usuario = (
    101,
    "Felipe",
    "Administrador"
)

print(f"ID: {usuario[0]}") # ID: 101
print(f"Nome: {usuario[1]}") # Nome: Felipe
print(f"Perfil: {usuario[2]}") # Perfil: Administrador

# ==============================
# 15. Boa prática
# ==============================

# Utilize tuplas quando os dados
# não precisarem ser alterados.
#
# Exemplos:
# - Coordenadas (x, y)
# - Datas
# - Configurações fixas
# - Dados de leitura
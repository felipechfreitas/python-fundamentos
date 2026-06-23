# Módulos em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Módulos são arquivos Python (.py).
# 2. Permitem reutilizar código.
# 3. Utilizam a palavra-chave import.
# 4. Evitam repetição de código.
# 5. Podem importar módulos próprios ou da biblioteca do Python.
# 6. Facilitam a organização dos projetos.

# ==============================
# 1. O que é um módulo?
# ==============================

# Todo arquivo .py pode ser considerado um módulo.

# Exemplo:
#
# calculadora.py
#
# def somar(a, b):
#     return a + b
#
# ----------------------
#
# main.py
#
# import calculadora
#
# print(calculadora.somar(10, 5))

# ==============================
# 2. Importando módulos da biblioteca padrão
# ==============================

import math

print(math.sqrt(25))  # Raiz quadrada . Saída: 5.0
print(math.pow(2, 3)) # Potência . Saída: 8.0

# ==============================
# 3. Importando funções específicas
# ==============================

from math import sqrt # Nesse caso, só puxa a função de Raiz quadrada

print(sqrt(36)) # Saída: 6.0

# ==============================
# 4. Utilizando apelidos (alias)
# ==============================

import math as m

print(m.sqrt(49)) # Dentro do print ele chama o m e coloca a função dentro do math e dentro dos parenteses o número pra saber raiz quadrada

# ==============================
# 5. Módulo random
# ==============================

import random

numero = random.randint(1, 10)

print(numero)

# Gera um número aleatório entre 1 e 10

# ==============================
# 6. Módulo datetime
# ==============================

from datetime import datetime

agora = datetime.now()

print(agora) # Saída: 2026-06-22 22:44:20.546964

# Data e hora atuais

# ==============================
# 7. Obtendo apenas a data
# ==============================

print(agora.date()) # Saída: 2026-06-22

# ==============================
# 8. Obtendo apenas a hora
# ==============================

print(agora.time()) # Saída: 22:44:20.546964

# ==============================
# 9. Exemplo de módulo criado pelo usuário
# ==============================

# Arquivo:
#
# mensagens.py
#
# def saudacao():
#     print("Olá!")
#
# ----------------------
#
# Arquivo principal:
#
# import mensagens
#
# mensagens.saudacao()

# ==============================
# 10. Importando apenas uma função
# ==============================

# Arquivo:
#
# mensagens.py
#
# def saudacao():
#     print("Olá!")
#
# ----------------------
#
# from mensagens import saudacao
#
# saudacao()

# ==============================
# 11. Verificando informações do módulo
# ==============================

print(dir(math))

# Exibe funções e atributos disponíveis

# ==============================
# 12. Boa prática
# ==============================

# Utilize import no início do arquivo.
# Organize módulos por responsabilidade.
# Evite importar tudo utilizando:
#
# from modulo import *
#
# Prefira:
#
# from modulo import funcao
#
# ou
#
# import modulo
# ==================================
# INPUT() EM PYTHON
# ==================================

# ==================================
# RESUMO RÁPIDO
# ==================================

# input() -> recebe dados do usuário
#
# str() -> converte para texto
# int() -> converte para inteiro
# float() -> converte para decimal
#
# input() sempre retorna string
#
# ValueError ocorre quando a conversão falha
#
# try/except evita que o programa quebre com erros de conversão.

# input() é usado para receber dados digitados pelo usuário.

# ==================================
# INPUT BÁSICO
# ==================================

nome = input("Digite seu nome: ")

print("Olá,", nome)

# ==================================
# RETORNO DO INPUT()
# ==================================

# Independentemente do que o usuário digite,
# o retorno sempre será uma string.

idade = input("Digite sua idade: ")

print(type(idade))

# Exemplo de saída:
# <class 'str'>

# ==================================
# CONVERTENDO PARA INTEIRO
# ==================================

idade = int(input("Digite sua idade: "))

print(type(idade))
print("Sua idade é:", idade)

# Exemplo de saída:
# <class 'int'>

# ==================================
# CONVERTENDO PARA FLOAT
# ==================================

altura = float(input("Digite sua altura: "))

print(type(altura))
print("Sua altura é:", altura)

# Exemplo:
# 1.80

# ==================================
# USANDO INPUT EM CÁLCULOS
# ==================================

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print("Resultado:", soma)

# ==================================
# ERRO COM INPUT
# ==================================

# Se o usuário digitar texto ao invés de número:

# idade = int(input("Digite sua idade: "))

# Entrada:
# abc

# Resultado:
# ValueError

# ==================================
# TRATANDO ERROS COM TRY/EXCEPT
# ==================================

# Estrutura do try/except:
# try:
#     código que PODE gerar um erro
# except TipoDoErro:
#     código para lidar com o erro

try:
    idade = int(input("Digite sua idade: "))
    print("Idade cadastrada:", idade)

except ValueError:
    print("Erro: Digite apenas números.")
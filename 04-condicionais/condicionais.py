# Condicionais em Python


# ==============================
# RESUMO RÁPIDO
# ==============================

# Condicionais são estruturas de controle que permitem executar blocos de código diferentes com base em condições específicas. Em Python, as principais estruturas condicionais são:

# 1. if (se): Executa um bloco de código se uma condição for verdadeira.

# 2. if-else (se-senão): Executa um bloco de código
#    se uma condição for verdadeira e outro bloco de código se a condição for falsa.

# 3. if-elif-else (se-senão se-senão):
#    Permite verificar múltiplas condições sequencialmente, executando o bloco de código correspondente à primeira condição verdadeira, ou um bloco de código final se todas as condições forem falsas.

# 4. Condicionais aninhadas: Permite colocar uma estrutura condicional dentro de outra, para verificar condições adicionais dentro de um bloco de código já condicionado.

# ==============================
# IF ou SE
# ==============================

# Estrutura básica do if
# if condição:
#     bloco de código

idade = 18

if idade >= 18: # Verifica se a idade é maior ou igual a 18
    print("Maior de idade") # O bloco de código dentro do if é executado apenas se a condição for verdadeira

# ==============================
# IF-ELSE ou SE-SENÃO
# ==============================

# Estrutura do if-else
# if condição:
#     bloco de código se a condição for verdadeira
# else:
#     bloco de código se a condição for falsa

nota = 7

if nota >= 6: # Verifica se a nota é maior ou igual a 6
    print("Aprovado") # O bloco de código dentro do if é executado se a condição for verdadeira, caso contrário, o bloco de código dentro do else é executado
else: # Se a condição do if for falsa
    print("Reprovado") # O bloco de código dentro do else é executado se a condição do if for falsa

# ==============================
# IF-ELIF-ELSE ou SE-SENÃO SE-SENÃO
# ==============================

# Estrutura do if-elif-else
# if condição1:
#     bloco de código se a condição1 for verdadeira
# elif condição2:
#     bloco de código se a condição2 for verdadeira
# else:
#     bloco de código se todas as condições anteriores forem falsas

nota = 8

if nota >= 9: # Verifica se a nota é maior ou igual a 9
    print("Excelente") # O bloco de código dentro do if é executado se a condição for verdadeira
elif nota >= 6: # Se a condição do if for falsa, verifica se a nota é maior ou igual a 6
    print("Aprovado") # O bloco de código dentro do elif é executado se a condição for verdadeira
else: # Se todas as condições anteriores forem falsas
    print("Reprovado") # O bloco de código dentro do else é executado se todas as condições anteriores forem falsas


# OBS: O PYTHON executa apenas o primeiro código verdadeiro.

nota = 10

if nota >= 6:
    print("Aprovado")
elif nota >= 9:
    print("Excelente")

# ==============================
# CONDICIONAIS COM STRINGS
# ==============================

nome = "Alice"

if nome == "Alice": # Verifica se o nome é igual a "Alice"
    print("Usuário encontrado!") # O bloco de código dentro do if é executado se a condição for verdadeira
else: # Se a condição do if for falsa
    print("Usuário não encontrado!") # O bloco de código dentro do else é executado se a condição do if for falsa

# ==============================
# CONDICIONAIS COM OPERADORES LÓGICOS
# OPERADOR AND ==============================

idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira: # Verifica se a idade é maior ou igual a 18 e se tem carteira
    print("Pode dirigir!") # O bloco de código dentro do if é executado se ambas as condições forem verdadeiras
else: # Se alguma das condições for falsa
    print("Não pode dirigir!") # O bloco de código dentro do else é executado se alguma das condições for falsa

# ==============================
# OPERADOR OR
# ==============================

tem_dinheiro = False
tem_cartao = True

if tem_dinheiro or tem_cartao: # Verifica se tem dinheiro ou tem cartão
    print("Pode comprar!") # O bloco de código dentro do if é executado se pelo menos uma das condições for verdadeira
else: # Se ambas as condições forem falsas
    print("Não pode comprar!") # O bloco de código dentro do else é executado se ambas as condições forem falsas

# ==============================
# OPERADOR NOT
# ==============================

esta_logado = False

if not esta_logado: # Verifica se não está logado
    print("Faça login") # O bloco de código dentro do if é executado se a condição for verdadeira (ou seja, se não está logado)

# Se esta_logado fosse True, o resultado de not esta_logado seria False, e o bloco de código dentro do if não seria executado.

# ==============================
# CONDICIONAIS ANINHADAS
# ==============================

idade = 20

if idade >= 18: # Verifica se a idade é maior ou igual a 18
    if idade >= 60: # Verifica se a idade é maior ou igual a 60
        print("Idoso") # O bloco de código dentro do if é executado se a primeira condição for verdadeira e a segunda condição for verdadeira
    else: # Se a segunda condição for falsa
        print("Adulto") # O bloco de código dentro do else é executado se a primeira condição for verdadeira e a segunda for falsa
else: # Se a primeira condição for falsa
    print("Menor de idade") # O bloco de código dentro do else é executado se a primeira condição for falsa


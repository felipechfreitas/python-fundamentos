# ==================================
# VARIÁVEIS EM PYTHON
# ==================================

# RESUMO RÁPIDO

# str   -> texto
# int   -> número inteiro
# float -> número decimal
# bool  -> True ou False
# list  -> coleção de itens
# dict  -> chave e valor
#
# type() -> mostra o tipo
# len()  -> mostra o tamanho
# input() -> recebe entrada do usuário

# Variáveis são usadas para armazenar valores e dados em um programa.

# ==================================
# TIPOS DE VARIÁVEIS
# ==================================

nome = "Felipe"  # String (texto)
idade = 30  # Inteiro
altura = 1.90  # Float
is_married = True  # Booleano

skills = ["Python", "JavaScript", "SQL"]  # Lista é composta por colchetes []

person_info = {
    "nome": "Felipe",
    "idade": 30,
    "altura": 1.90,
    "is_married": True
}  # Dicionário é composto por chaves {}

# ==================================
# IMPRESSÃO DE VALORES
# ==================================

print(nome) # output: Felipe
print(idade) # output: 30
print(altura) # output: 1.9
print(is_married) # output: True
print(skills) # output: ['Python', 'JavaScript', 'SQL']
print(person_info) # output: {'nome': 'Felipe', 'idade': 30, 'altura': 1.9, 'is_married': True}

print("Nome:", nome) # output: Nome: Felipe
print("Idade:", idade) # output: Idade: 30
print("Altura:", altura) # output: Altura: 1.9
print("Casado:", is_married) # output: Casado: True

# ==================================
# TYPE()
# ==================================

print(type(nome)) # output: <class 'str'>
print(type(idade)) # output: <class 'int'>
print(type(altura)) # output: <class 'float'>
print(type(is_married)) # output: <class 'bool'>
print(type(skills)) # output: <class 'list'>
print(type(person_info)) # output: <class 'dict'>

# ==================================
# MÚLTIPLAS VARIÁVEIS
# ==================================

x, y, z = 10, 20, 30

print(x) # output: 10
print(y) # output: 20
print(z) # output: 30

# ==================================
# ATUALIZANDO VARIÁVEIS
# ==================================

idade = 31 # A variável 'idade' agora tem um novo valor

print("Idade atualizada:", idade)

# ==================================
# OPERAÇÕES COM VARIÁVEIS
# ==================================

soma = idade + 5 # A variável 'soma' armazena o resultado da operação de adição entre 'idade' e 5

print("Idade + 5:", soma) # output: Idade + 5: 36

# ==================================
# CONCATENAÇÃO DE STRINGS
# ==================================

sobrenome = "Silva"

nome_completo = nome + " " + sobrenome

print(nome_completo) # output: Felipe Silva

cidade = "São Paulo"

print(nome + " mora em " + cidade) # output: Felipe mora em São Paulo

# ==================================
# F-STRINGS
# ==================================

# Estrurura de uma f-string:
# f"Texto {variável} mais texto {outra_variável}"

print(f"{nome} tem {idade} anos e mede {altura} metros.") # output: Felipe tem 31 anos e mede 1.9 metros.

# ==================================
# FUNÇÕES COM VARIÁVEIS
# ==================================

comprimento_nome = len(nome) # A função len() retorna o número de caracteres em uma string.

print(comprimento_nome) # output: 6

# ==================================
# INPUT()
# ==================================

idade_usuario = input("Digite sua idade: ") # A função input() permite que o usuário digite um valor, que é armazenado na variável 'idade_usuario'.

print("Você digitou:", idade_usuario) # output: Você digitou: (o que o usuário digitou)

print(type(idade_usuario)) # output: <class 'str'>, mesmo que o usuário digite um número, ele será armazenado como uma string.

# Observação:
# input() sempre retorna uma string.

# ==================================
# LISTAS E DICIONÁRIOS
# ==================================

frutas = ["maçã", "banana", "laranja"] # A variável 'frutas' é uma lista que armazena três strings: "maçã", "banana" e "laranja".

pessoa = {
    "nome": "Felipe",
    "idade": 30
}

# A variável 'pessoa' é um dicionário que armazena duas chaves: "nome" e "idade", com os respectivos valores "Felipe" e 30.

print(frutas) # output: ['maçã', 'banana', 'laranja']
print(pessoa) # output: {'nome': 'Felipe', 'idade': 30}

print(type(frutas)) # output: <class 'list'>
print(type(pessoa)) # output: <class 'dict'>
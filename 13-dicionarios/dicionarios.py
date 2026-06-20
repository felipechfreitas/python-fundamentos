# Dicionários em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Dicionários armazenam dados em pares chave:valor.
# 2. São definidos utilizando {}.
# 3. Cada chave deve ser única.
# 4. Permitem armazenar diferentes tipos de dados.
# 5. Muito utilizados para representar objetos.
# 6. Permitem adicionar, alterar e remover informações.
# 7. Métodos importantes: keys(), values() e items().

# ==============================
# 1. Criando um dicionário
# ==============================

pessoa = {
    "nome": "Felipe",
    "idade": 31,
    "cidade": "Guarulhos"
}

print(pessoa) # Saída: {'nome': 'Felipe', 'idade': 31, 'cidade': 'Guarulhos'}
print(type(pessoa)) # Saída: <class 'dict'>
print(type(pessoa["idade"])) # Saída: <class 'int'>

# ==============================
# 2. Acessando valores
# ==============================

print(pessoa["nome"]) # Saída: Felipe
print(pessoa["idade"]) # Saída: 31
print(pessoa["cidade"]) # Saída: Guarulhos

# ==============================
# 3. Utilizando get()
# ==============================

print(pessoa.get("nome")) # Retorna o valor associado à chave "nome". Saída: Felipe

# Retorna None se a chave não existir
print(pessoa.get("telefone"))

# ==============================
# 4. Alterando valores
# ==============================

pessoa["idade"] = 32

print(pessoa) # Saída: {'nome': 'Felipe', 'idade': 32, 'cidade': 'Guarulhos'}

# ==============================
# 5. Adicionando novos dados
# ==============================

pessoa["profissao"] = "Analista"

print(pessoa) # Saída: {'nome': 'Felipe', 'idade': 32, 'cidade': 'Guarulhos', 'profissao': 'Analista'}

# ==============================
# 6. Removendo itens
# ==============================

del pessoa["cidade"] # Remove a chave cidade do dicionário

print(pessoa) # Saída: {'nome': 'Felipe', 'idade': 32, 'profissao': 'Analista'}

# ==============================
# 7. Verificando existência de chave
# ==============================

print("nome" in pessoa) # Saída: True
print("cidade" in pessoa) # Saída: False

# ==============================
# 8. Percorrendo apenas as chaves
# ==============================

for chave in pessoa:
    print(chave)

# Saída:
# nome
# idade
# profissao

# ==============================
# 9. Percorrendo apenas os valores
# ==============================

for valor in pessoa.values():
    print(valor)

# Saída:
# Felipe
# 32
# Analista

# ==============================
# 10. Percorrendo chave e valor
# ==============================

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# O método items() retorna pares (chave, valor).
# O Python atribui automaticamente:
# chave -> primeiro valor
# valor -> segundo valor

# Saída:
# nome: Felipe
# idade: 32
# profissao: Analista

# ==============================
# 11. Obtendo todas as chaves
# ==============================

print(pessoa.keys()) # Saída: dict_keys(['nome', 'idade', 'profissao'])

# ==============================
# 12. Obtendo todos os valores
# ==============================

print(pessoa.values()) # Saída: dict_values(['Felipe', 32, 'Analista'])

# ==============================
# 13. Obtendo chave e valor
# ==============================

print(pessoa.items()) # Retorna pares (chave, valor). Saída: dict_items([('nome', 'Felipe'), ('idade', 32), ('profissao', 'Analista')])

# ==============================
# 14. Dicionário com listas
# ==============================

usuario = {
    "nome": "Felipe",
    "skills": ["Python", "SQL", "Git"]
}

print(usuario) # Saída: {'nome': 'Felipe', 'skills': ['Python', 'SQL', 'Git']}
print(usuario["skills"]) # Saída: ['Python', 'SQL', 'Git']
print(usuario["skills"][0]) # Python

# ==============================
# 15. Exemplo semelhante a projetos
# ==============================

projeto = {
    "nome": "Sistema de Tarefas",
    "status": "Em andamento",
    "tarefas": 10
}

print(projeto["nome"])
print(projeto["status"])
print(projeto["tarefas"])

# ==============================
# 16. Boa prática
# ==============================

# Utilize nomes claros para as chaves.
# Evite abreviações desnecessárias.
# Organize os dados relacionados dentro do mesmo dicionário.
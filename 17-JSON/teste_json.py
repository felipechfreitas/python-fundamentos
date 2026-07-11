import json

# ==============================
# Teste 1 - Convertendo um dicionário para JSON
# ==============================

pessoa = {
    "nome": "Felipe",
    "idade": 31,
    "cidade": "Guarulhos"
}

print("Dicionário Python:")
print(pessoa)

# Saída:
# {'nome': 'Felipe', 'idade': 31, 'cidade': 'Guarulhos'}

print(type(pessoa)) # Saída: <class 'dict'>

print()

# Converte o dicionário para JSON
pessoa_json = json.dumps(pessoa)

print("JSON:")
print(pessoa_json)

# Saída:
# {"nome": "Felipe", "idade": 31, "cidade": "Guarulhos"}

print(type(pessoa_json)) # Saída: <class 'str'>

# O que era um dicionário Python agora é uma String no formato JSON.

# ==============================
# Teste 2 - JSON BONITO
# ==============================

# O parâmetro indent organiza o JSON com espaços, facilitando a leitura.
# Quanto maior o valor do indent, maior será o recuo.
# O valor mais utilizado é 4.

print()

print("JSON formatado:")
print(json.dumps(pessoa, indent=4))

# Saída:
# {
#     "nome": "Felipe",
#     "idade": 31,
#     "cidade": "Guarulhos"
# }

# O parâmetro indent define quantos espaços serão utilizados para organizar (indentar) o JSON.
# O valor mais utilizado é 4, pois deixa o conteúdo mais legível.

# O conteúdo continua sendo uma String JSON.
# A diferença é que agora ela está formatada com indentação,
# tornando a leitura muito mais fácil.

print(type(json.dumps(pessoa, indent=4))) # Saída: <class 'str'>


# ==============================
# Teste 3 - Criando um arquivo JSON
# ==============================

pessoa = {
    "nome": "Felipe",
    "idade": 31,
    "cidade": "Guarulhos",
    "profissao": "Analista Fiscal",
    "skills": [
        "Python",
        "SQL",
        "Power BI"
    ]
}

# O método dump() grava um objeto Python diretamente em um arquivo.
# Se o arquivo não existir, ele será criado automaticamente.

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

print("Arquivo dados.json criado com sucesso!")

# Após executar o código, verá que o arquivo dados.json foi criado. Daí percebemos que um dicionário Python foi transformado em um arquivo .json.

# ==============================
# Teste 4 - Lendo um arquivo JSON
# ==============================

# O método load() lê um arquivo JSON e converte
# automaticamente seu conteúdo para um objeto Python.

with open("dados.json", "r", encoding="utf-8") as arquivo:

# Explicação do código acima: Abrindo arquivo para leitura.

    dados = json.load(arquivo)

# Explicação do código acima: Abre o arquivo dados.json, lê o arquivo e converte automaticamente para um dicionário Python.

print("Conteúdo do arquivo:")
print(dados)

print()

print("Tipo da variável:")
print(type(dados)) # Saída: <class 'dict'> . Linha comprova que o json.load() devolve um dicionário Python.

# Saída esperada:

# Conteúdo do arquivo:
# {'nome': 'Felipe', 'idade': 31, 'cidade': 'Guarulhos', 'profissao': 'Analista Fiscal', 'skills': ['Python', 'SQL', 'Power BI']}

# Tipo da variável:
# <class 'dict'>

# Percebe que ele não é mais uma string, mas sim um dicionário Python.
# Observe que o JSON foi convertido novamente para um dicionário Python.

# Se aterar manualmente uma informação no arquivo dados.json e rodar novamente o  teste 4, a informação alterada será exibida no terminal.

print()

print("Nome:", dados["nome"])
print("Idade:", dados["idade"])
print("Cidade:", dados["cidade"])

# ==============================
# Teste 5 - Convertendo uma String JSON para um dicionário
# ==============================

# Criamos uma String que está no formato JSON.
# Apesar de parecer um dicionário, ela ainda é apenas um texto (String).

texto_json = '''
{
    "nome": "Felipe",
    "idade": 31,
    "cidade": "Guarulhos"
}
'''

print("Conteúdo da String JSON:")
print(texto_json)

print()

print("Tipo da variável antes da conversão:")
print(type(texto_json)) # Saída: <class 'str'>

# Saída:
# Conteúdo da String JSON:
# {
#     "nome": "Felipe",
#     "idade": 31,
#     "cidade": "Guarulhos"
# }

# O método loads() converte uma String JSON
# para um objeto Python (neste caso, um dicionário).

dados = json.loads(texto_json)

print()

print("Conteúdo após a conversão:")
print(dados)

# Saída: {'nome': 'Felipe', 'idade': 31, 'cidade': 'Guarulhos'}

print()

print("Tipo da variável após a conversão:")
print(type(dados)) # Saída: <class 'dict'>

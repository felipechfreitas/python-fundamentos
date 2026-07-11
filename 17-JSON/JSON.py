# JSON em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. JSON significa JavaScript Object Notation.
# 2. É um formato utilizado para troca de dados entre sistemas.
# 3. É muito utilizado em APIs, aplicações web e automações.
# 4. Em Python utilizamos o módulo json para trabalhar com esse formato.
# 5. Um dicionário Python pode ser convertido para JSON.
# 6. Um JSON também pode ser convertido para um dicionário Python.
# 7. Principais funções:
#    - dumps() -> Converte objeto Python para JSON (String)
#    - loads() -> Converte JSON (String) para objeto Python
#    - dump()  -> Salva JSON em um arquivo
#    - load()  -> Lê JSON de um arquivo

import json

# ==============================
# 1. O que é JSON?
# ==============================

# JSON é um formato de texto utilizado para armazenar
# e transportar informações entre diferentes sistemas.

# Exemplo de JSON:
#
# {
#     "nome": "Felipe",
#     "idade": 31,
#     "cidade": "Guarulhos"
# }

# ==============================
# 2. Dicionário Python
# ==============================

pessoa = {
    "nome": "Felipe",
    "idade": 31,
    "cidade": "Guarulhos"
}

print(pessoa)
print(type(pessoa))

# Saída:
# {'nome': 'Felipe', 'idade': 31, 'cidade': 'Guarulhos'}
# <class 'dict'>

# ==============================
# 3. Convertendo um dicionário para JSON
# ==============================

# dumps() converte um objeto Python para uma String no formato JSON.

pessoa_json = json.dumps(pessoa)

print(pessoa_json)
print(type(pessoa_json))

# Saída:
# {"nome": "Felipe", "idade": 31, "cidade": "Guarulhos"}
# <class 'str'>

# Observe que agora o resultado é uma String.

# ==============================
# 4. JSON formatado
# ==============================

# O parâmetro indent deixa o JSON organizado.

json_formatado = json.dumps(pessoa, indent=4)

print(json_formatado)

# Resultado:

# {
#     "nome": "Felipe",
#     "idade": 31,
#     "cidade": "Guarulhos"
# }

# ==============================
# 5. Convertendo JSON para dicionário
# ==============================

texto_json = '''
{
    "nome": "Maria",
    "idade": 28,
    "cidade": "São Paulo"
}
'''

# loads() converte uma String JSON para um dicionário Python.

dados = json.loads(texto_json)

print(dados)
print(type(dados))

# Saída:
# {'nome': 'Maria', 'idade': 28, 'cidade': 'São Paulo'}
# <class 'dict'>

# ==============================
# 6. Acessando informações
# ==============================

# Depois da conversão podemos acessar normalmente.

print(dados["nome"])
print(dados["idade"])

# ==============================
# 7. Salvando JSON em arquivo
# ==============================

# dump() grava um objeto Python em um arquivo JSON.

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

print("Arquivo JSON criado com sucesso!")

# O parâmetro ensure_ascii=False mantém caracteres especiais,
# como acentos e cedilhas.

# ==============================
# 8. Lendo um arquivo JSON
# ==============================

# load() lê um arquivo JSON e converte automaticamente
# para um dicionário Python.

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados_json = json.load(arquivo)

print(dados_json)
print(type(dados_json))

# ==============================
# 9. Exemplo semelhante a projetos
# ==============================

funcionario = {
    "nome": "Felipe",
    "cargo": "Analista Fiscal",
    "skills": [
        "Python",
        "SQL",
        "Power BI"
    ]
}

with open("funcionario.json", "w", encoding="utf-8") as arquivo:
    json.dump(funcionario, arquivo, indent=4, ensure_ascii=False)

print("Arquivo funcionario.json criado!")

# ==============================
# 10. Tratando erros
# ==============================

try:

    with open("arquivo_inexistente.json", "r") as arquivo:
        dados = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo JSON não encontrado.")

# ==============================
# 11. Boas práticas
# ==============================

# Utilize sempre o módulo json.
# Utilize indent=4 para facilitar a leitura.
# Utilize ensure_ascii=False para manter acentos.
# Utilize try/except quando ler arquivos.
# Prefira nomes claros para as chaves do JSON.
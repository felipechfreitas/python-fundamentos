# Arquivos em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Arquivos permitem salvar dados permanentemente.
# 2. Utilizamos a função open() para abrir arquivos.
# 3. Sempre devemos fechar o arquivo após utilizá-lo.
# 4. O comando with é a forma mais segura de trabalhar com arquivos.
# 5. Podemos ler, escrever e adicionar informações em arquivos.
# 6. Os principais modos são: "r", "w", "a" e "x".

# ==============================
# 1. O que é um arquivo?
# ==============================

# Um arquivo é um local onde podemos armazenar informações
# para utilizá-las futuramente.

# Exemplos:
# clientes.txt
# produtos.csv
# dados.json

# ==============================
# 2. Abrindo um arquivo
# ==============================

# Sintaxe:
#
# arquivo = open("arquivo.txt", "r")
#
# r = leitura (Read)

# ==============================
# 3. Lendo um arquivo
# ==============================

# Exemplo:
#
# with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
#
# print(conteudo)
#
# O método read() lê todo o conteúdo do arquivo.

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# O método read() lê todo o conteúdo do arquivo.
# encoding define a codificação utilizada para ler ou escrever o arquivo.
# O UTF-8 é o padrão mais utilizado atualmente e suporta caracteres
# especiais, como acentos, cedilha e símbolos.

# ==============================
# 4. Escrevendo em um arquivo
# ==============================

with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, Python!")

# O modo "w" (Write) serve para escrever em um arquivo.
# Se o arquivo não existir, ele será criado.
# Se o arquivo já existir, todo o conteúdo anterior será apagado.

# ==============================
# 5. Adicionando conteúdo
# ==============================

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nNova linha adicionada.")

# O modo "a" adiciona conteúdo ao final do arquivo.

# ==============================
# 6. Lendo linha por linha
# ==============================

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

# Muito útil para arquivos grandes.

# ==============================
# 7. Lendo todas as linhas
# ==============================

with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()

print(linhas)

# readlines() retorna uma lista.

# ==============================
# 8. Modos de abertura
# ==============================

# "r" -> leitura
# "w" -> escrita (apaga conteúdo anterior)
# "a" -> adiciona conteúdo
# "x" -> cria arquivo novo (gera erro se já existir)

# ==============================
# 9. Exemplo semelhante a projetos
# ==============================

tarefas = [
    "Estudar Python",
    "Praticar Git",
    "Atualizar LinkedIn"
]

with open("tarefas.txt", "w") as arquivo:

    for tarefa in tarefas:
        arquivo.write(tarefa + "\n")

print("Arquivo criado com sucesso!")

# ==============================
# 10. Lendo o arquivo criado
# ==============================

with open("tarefas.txt", "r") as arquivo:

    for linha in arquivo:
        print(linha.strip())

# strip() remove o \n do final de cada linha.

# ==============================
# 11. Tratando erros
# ==============================

try:

    with open("arquivo_inexistente.txt", "r") as arquivo:
        print(arquivo.read())

except FileNotFoundError:
    print("Arquivo não encontrado.")

# ==============================
# 12. Boas práticas
# ==============================

# Utilize sempre "with".
# Evite esquecer arquivos abertos.
# Utilize try/except quando necessário.
# Escolha corretamente o modo de abertura.

# ==============================
# O que o "with" faz?
# ==============================

# O comando "with" abre o arquivo e garante que ele será fechado
# automaticamente ao final do bloco de código, mesmo que ocorra um erro.
#
# Sem o "with", seria necessário fazer:
#
# arquivo = open("arquivo.txt", "r")
# print(arquivo.read())
# arquivo.close()
#
# Por isso, utilizar "with" é considerado uma boa prática.
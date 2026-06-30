# ==============================
# 1. Lendo um arquivo ("r")
# ==============================

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# Criei um arquivo com o nome arquivo.txt e coloquei um texto
# Depois rodei o código e o conteúdo contido no arquivo apareceu no terminal.

# ==============================
# 2. Escrevendo em um arquivo ("w")
# ==============================

# print("\n===== Conteúdo antes da escrita =====")

# with open("saida.txt", "r", encoding="utf-8") as arquivo:
#    print(arquivo.read())

# O modo "w" (Write) serve para escrever em um arquivo.
# Se o arquivo não existir, ele será criado.
# Se o arquivo já existir, todo o conteúdo anterior será apagado.

# with open("saida.txt", "w", encoding="utf-8") as arquivo:
#    arquivo.write("Nova informação.")

# print("\n===== Conteúdo depois da escrita =====")

# with open("saida.txt", "r", encoding="utf-8") as arquivo:
#    print(arquivo.read())

# ==============================
# 3. Adicionando conteúdo ("a")
# ==============================

# O modo "a" (Append) adiciona novas informações ao final do arquivo.
# Diferente do modo "w", ele NÃO apaga o conteúdo existente.

# with open("saida.txt", "a", encoding="utf-8") as arquivo:
#    arquivo.write("\nSegunda informação.")
#    arquivo.write("\nTerceira informação.")

# print("\n===== Conteúdo após append =====")

# with open("saida.txt", "r", encoding="utf-8") as arquivo:
#     print(arquivo.read())


# RESUMO
#
# "r" -> Apenas lê o arquivo.
#
# "w" -> Escreve no arquivo.
#        Se existir, apaga tudo antes.
#
# "a" -> Adiciona novas informações no final.
#        Nunca apaga o conteúdo existente.


# ==============================
# 4. Lendo apenas uma linha (readline())
# ==============================

# O método readline() lê apenas UMA linha do arquivo por vez.
# Cada vez que ele é chamado, o Python avança para a próxima linha.

with open("saida.txt", "r", encoding="utf-8") as arquivo:

    print(arquivo.readline()) # Primeira linha
    print(arquivo.readline()) # Segunda linha
    print(arquivo.readline()) # Terceira linha

# No terminal fica:
# Primeira linha
#
# Segunda linha
#
# Terceira linha

# Se quiser remover o espaço entre cada linha, escrever dessa forma:

with open("saida.txt", "r", encoding="utf-8") as arquivo:

    print(arquivo.readline().strip()) # Primeira linha
    print(arquivo.readline().strip()) # Segunda linha
    print(arquivo.readline().strip()) # Terceira linha
    print(arquivo.readline().strip()) # Quarta linha
    print(arquivo.readline().strip()) # Essa linha aparecerá como uma string vazia

# Observações:
#
# read()       -> Lê todo o arquivo.
#
# readline()   -> Lê apenas uma linha por vez.
#
# Cada chamada do readline() avança automaticamente
# para a próxima linha do arquivo.
#
# Utilize strip() para remover a quebra de linha (\n).

# ==============================
# 5. Lendo todas as linhas (readlines())
# ==============================

# O método readlines() lê todas as linhas do arquivo
# e retorna uma lista, onde cada posição representa uma linha.

with open("saida.txt", "r", encoding="utf-8") as arquivo:

    linhas = arquivo.readlines()

print(linhas)

print(type(linhas))

print(linhas[0])
print(linhas[1])
print(linhas[2])

print(linhas[0].strip())
print(linhas[1].strip())
print(linhas[2].strip())

for linha in linhas:
    print(linha.strip())

# ==============================
# RESUMO
# ==============================

# read()
# Lê todo o arquivo e retorna uma única string.

# readline()
# Lê apenas uma linha por vez.

# readlines()
# Lê todas as linhas e retorna uma lista.

# ==============================
# 6. Criando um arquivo ("x")
# ==============================

# O modo "x" cria um novo arquivo.
# Se o arquivo já existir, o Python gera um erro.

try:
    with open("novo_arquivo.txt", "x", encoding="utf-8") as arquivo:
        arquivo.write("Arquivo criado com sucesso!")

    print("Arquivo criado!")

except FileExistsError:
    print("O arquivo já existe.")

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
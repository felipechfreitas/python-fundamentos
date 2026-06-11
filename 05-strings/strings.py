# Strings em Python

# ==============================
# 1. Criando Strings
# ==============================

nome = "Felipe"  # String contendo o primeiro nome
sobrenome = "Freitas"  # String contendo o sobrenome

print(nome)
print(sobrenome)

# Exibindo o tipo das variáveis
print(type(nome))
print(type(sobrenome))

# ==============================
# 2. Concatenação
# ==============================

# Junta duas strings utilizando o operador +
nome_completo = nome + " " + sobrenome

print(nome_completo)

# ==============================
# 3. F-Strings
# ==============================

idade = 31

# Forma moderna de inserir variáveis dentro de textos
print(f"{nome_completo} tem {idade} anos")

# ==============================
# 4. Tamanho da String
# ==============================

# len() retorna a quantidade de caracteres
print(len(nome))

# ==============================
# 5. Acessando Caracteres
# ==============================

# Índices começam em 0
print(nome[0])
print(nome[1])
print(nome[2])

# ==============================
# 6. Maiúsculas e Minúsculas
# ==============================

print(nome.upper())       # Tudo maiúsculo
print(nome.lower())       # Tudo minúsculo
print(nome.capitalize())  # Primeira letra maiúscula

# ==============================
# 7. Removendo Espaços
# ==============================

texto = "      Python      "

# Remove espaços do início e do fim
print(texto.strip())

# ==============================
# 8. Substituindo Conteúdo
# ==============================

frase = "Eu estudo Java"

# Substitui uma palavra por outra
print(frase.replace("Java", "Python"))

# ==============================
# 9. Verificando Conteúdo
# ==============================

# Verifica se a palavra existe dentro da string
print("Python" in frase)
print("Java" in frase)

# ==============================
# 10. Dividindo Texto
# ==============================

linguagens = "Python,Java,SQL"

# Transforma uma string em lista
lista = linguagens.split(",")

print(lista)
print(type(lista))

# ==============================
# 11. Contando Ocorrências
# ==============================

texto = "Python Python SQL"

print(texto.count("Python"))

# ==============================
# 12. Procurando Texto
# ==============================

frase = "Eu estudo Python"

print(frase.find("Python"))

# ==============================
# 13. Verificando Início e Fim
# ==============================

arquivo = "relatorio.pdf"

print(arquivo.startswith("relatorio"))
print(arquivo.endswith(".pdf"))
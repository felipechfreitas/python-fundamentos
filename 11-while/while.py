# While em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. while executa um bloco de código enquanto uma condição for verdadeira.
# 2. Muito utilizado quando não sabemos quantas vezes o loop irá executar.
# 3. A condição é verificada antes de cada repetição.
# 4. É necessário atualizar a condição para evitar loops infinitos.
# 5. Pode ser utilizado com break e continue.
# 6. Muito usado em menus, validações e entrada de dados.

# ==============================
# 1. Estrutura básica
# ==============================

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# Saída:
# 1
# 2
# 3
# 4
# 5

# ==============================
# 2. Contagem crescente
# ==============================

numero = 1

while numero <= 10:
    print(numero)
    numero += 1

# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# ==============================
# 3. Contagem regressiva
# ==============================

contador = 5

while contador > 0:
    print(contador)
    contador -= 1

print("Fim da contagem!")

# output
# 5
# 4
# 3
# 2
# 1
# Fim da contagem!

# ==============================
# 4. Loop infinito (exemplo)
# ==============================

# CUIDADO:
# Este código nunca termina.

# while True:
#     print("Executando para sempre")

# ==============================
# 5. Utilizando break
# ==============================

contador = 1

while True:
    print(contador)

    if contador == 5:
        break

    contador += 1

# O break encerra o loop imediatamente.

# output
# 1
# 2
# 3
# 4
# 5

# ==============================
# 6. Utilizando continue
# ==============================

contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue

    print(contador)

# Saída:
# 1
# 2
# 4
# 5

# O continue pula a execução atual
# e volta para o início do loop.

# ==============================
# 7. Recebendo dados do usuário
# ==============================

senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")

print("Acesso liberado!")

# O loop continuará executando
# até que a senha correta seja digitada.

# ==============================
# 8. Exemplo com menu
# ==============================

opcao = ""

while opcao != "4":

    print("\nMENU")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

print("Programa encerrado.")

# Exemplo parecido com o projeto
# Lista de Tarefas.

# ==============================
# 9. Somando números
# ==============================

# Vamos somar os números de 1 até 5.

soma = 0
# A variável soma começa em 0 porque ainda não somamos nada.

contador = 1
# O contador começa em 1, que será o primeiro número da soma.

while contador <= 5:
    # Enquanto o contador for menor ou igual a 5,
    # o bloco abaixo será executado.

    soma += contador
    # Equivalente a:
    # soma = soma + contador
    #
    # A cada volta do loop, o valor atual do contador
    # é adicionado à variável soma.

    contador += 1
    # Incrementa o contador em 1 para avançar para o próximo número.

print(f"Soma total: {soma}")

# Resultado:
# 15

# ==============================
# 10. Boas práticas
# ==============================

# Sempre atualize a variável de controle.
#
# Exemplo correto:

contador = 1

while contador <= 3:
    print(contador)
    contador += 1

# Exemplo incorreto:
#
# contador = 1
#
# while contador <= 3:
#     print(contador)
#
# O contador nunca muda,
# criando um loop infinito.
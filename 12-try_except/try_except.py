# Try Except em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. try é usado para testar um bloco de código.
# 2. except captura erros sem encerrar o programa.
# 3. Muito utilizado com input().
# 4. Evita que o programa quebre por entradas inválidas.
# 5. Pode tratar diferentes tipos de erros.
# 6. else executa se nenhum erro acontecer.
# 7. finally executa sempre.

# ==============================
# 1. Estrutura Básica
# ==============================

# try:
#    codigo_que_pode_dar_erro()

# except TipoDoErro:
#    tratar_erro()

try:
    numero = int(input("Digite um número: "))
    print(numero)

except ValueError:
    print("Digite apenas números inteiros.")

# ==============================
# 2. Exemplo sem erro
# ==============================

try:
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade é {idade}")

except ValueError:
    print("Valor inválido.")

# ==============================
# 3. Tratando divisão por zero
# ==============================

try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# ==============================
# 4. Tratando múltiplos erros
# ==============================

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)

except ValueError:
    print("Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# ==============================
# 5. Utilizando else
# ==============================

try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Entrada inválida.")

else:
    print(f"Número digitado: {numero}")

# ==============================
# 6. Utilizando finally
# ==============================

try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Entrada inválida.")

finally:
    print("Fim da execução.")

# ==============================
# 7. Exemplo semelhante ao projeto
# ==============================

try:
    escolha = int(input("Escolha uma tarefa: "))
    print(f"Você escolheu a tarefa {escolha}")

except ValueError:
    print("Digite apenas números.")

# ==============================
# 8. Capturando o erro na variável
# ==============================

try:
    numero = int(input("Digite um número: "))

except ValueError as erro:
    print(f"Erro encontrado: {erro}")

# ==============================
# 9. Boa prática
# ==============================

# Evite usar:
#
# except:
#     print("Erro")
#
# Prefira capturar erros específicos:
#
# except ValueError:
#     print("Digite apenas números")
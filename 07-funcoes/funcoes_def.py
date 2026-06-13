# Funções em Python

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. Função é um bloco de código reutilizável que realiza uma tarefa específica.
# 2. Definida usando a palavra-chave def.
# 3. Pode receber parâmetros para personalizar seu comportamento.
# 4. Pode retornar valores usando return.
# 5. Ajuda a organizar o código, evitar repetições e facilitar manutenção.
# 6. Boas práticas: use nomes claros, prefira funções pequenas e com uma única responsabilidade.

# ==============================
# 1. O que é uma função?
# ==============================

# Funções servem para organizar o código,
# evitar repetições e facilitar manutenção.

def saudacao(): # Definindo a função saudacao, que não recebe parâmetros e não retorna nada.
    print("Olá, mundo!") # O corpo da função é o código que será executado quando a função for chamada.

saudacao() # Chamando a função saudacao para executar o código dentro dela.

# ==============================
# 2. Função com parâmetro
# ==============================

def cumprimentar(nome): # A função cumprimentar recebe um parâmetro chamado nome, que é utilizado dentro da função para personalizar a mensagem de saudação.
    print(f"Olá, {nome}!") # O f-string é utilizado para formatar a string, inserindo o valor do parâmetro nome dentro da mensagem.

cumprimentar("Felipe") # Chamando a função cumprimentar e passando o argumento "Felipe" para o parâmetro nome, resultando na impressão da mensagem "Olá, Felipe!".

# ==============================
# 3. Função com mais de um parâmetro
# ==============================

def somar(a, b): # A função somar recebe dois parâmetros.
    print(a + b) # O corpo da função realiza a soma dos parâmetros a e b e imprime o resultado. Note que essa função não retorna um valor, apenas exibe o resultado da soma.

somar(10, 5) # Chamando a função somar e passando os argumentos 10 e 5 para os parâmetros a e b, respectivamente, resultando na impressão do valor 15, que é a soma de 10 e 5.

# ==============================
# 4. Retornando valores com return
# ==============================

def multiplicar(a, b): # Recebe dois parametros
    return a * b # O corpo da função realiza a multiplicação dos parâmetros a e b e retorna o resultado. Diferente da função somar, que apenas imprimia o resultado, a função multiplicar permite que o valor seja utilizado posteriormente no código em lugar de apenas exibi-lo.

resultado = multiplicar(4, 3) # Armazena o retorno da função multiplicar.

print(resultado) # Imprime o valor armazenado na variável resultado, que é 12, o resultado da multiplicação de 4 e 3 realizada pela função multiplicar.

# ==============================
# 5. Armazenando retorno em variável
# ==============================

def calcular_idade(ano_atual, ano_nascimento): # Mesma coisa da função multiplicar, mas agora para calcular a idade de uma pessoa com base no ano atual e no ano de nascimento. A função recebe dois parâmetros, ano_atual e ano_nascimento, e retorna a diferença entre eles, que é a idade da pessoa.
    return ano_atual - ano_nascimento

idade = calcular_idade(2025, 1994) # Chamando a função calcular_idade e passando os argumentos 2025 e 1994 para os parâmetros ano_atual e ano_nascimento, respectivamente. O resultado da subtração (31) é retornado pela função e armazenado na variável idade.

print(f"Idade: {idade}") # Imprime a mensagem "Idade: 31", utilizando um f-string para formatar a string e inserir o valor da variável idade dentro da mensagem.

# ==============================
# 6. Função sem retorno
# ==============================

def exibir_mensagem(): # A função exibir_mensagem não recebe parâmetros e não retorna nenhum valor. Ela apenas executa um comando de impressão para exibir uma mensagem na tela.
    print("Bem-vindo ao sistema!")

exibir_mensagem()

# ==============================
# 7. Função retornando True ou False
# ==============================

def maior_de_idade(idade): # A função maior_de_idade recebe um parâmetro idade e retorna (return) um valor booleano (True ou False) indicando se a idade é maior ou igual a 18 anos, o que é comumente utilizado para verificar se uma pessoa é considerada maior de idade.
    return idade >= 18

print(maior_de_idade(20)) # Chamando a função maior_de_idade e passando o argumento 20 para o parâmetro idade. O resultado (True) é retornado pela função e impresso na tela.
print(maior_de_idade(15)) # Chamando a função maior_de_idade e passando o argumento 15 para o parâmetro idade. O resultado (False) é retornado pela função e impresso na tela.

# ==============================
# 8. Função utilizando listas
# ==============================

def listar_nomes(nomes): # A função listar_nomes recebe um parâmetro nomes, que é esperado ser uma lista de nomes. O corpo da função utiliza um loop for para percorrer cada nome na lista e imprimir cada um deles na tela.
    for nome in nomes: # Percorre cada item da lista
        print(nome)

pessoas = ["Felipe", "Maria", "João"]

listar_nomes(pessoas) # Chamando a função listar_nomes e passando a lista pessoas como argumento para o parâmetro nomes. A função irá iterar sobre cada nome na lista pessoas e imprimir cada um deles na tela, resultando na impressão de "Felipe", "Maria" e "João" em linhas separadas.

# ==============================
# 9. Exemplo semelhante ao projeto
# ==============================

def adicionar_tarefa(tarefas, tarefa): # A função adicionar_tarefa recebe dois parâmetros: tarefas, que é uma lista onde as tarefas serão armazenadas, e tarefa, que é a tarefa a ser adicionada à lista. O corpo da função utiliza o método append() para adicionar a tarefa fornecida ao final da lista de tarefas.
    tarefas.append(tarefa) # O método append() é utilizado para adicionar um item ao final de uma lista. Neste caso, a tarefa fornecida como argumento para o parâmetro tarefa será adicionada à lista tarefas.

lista_tarefas = []

adicionar_tarefa(lista_tarefas, "Estudar Python") # Chamando a função adicionar_tarefa e passando a lista lista_tarefas e a string "Estudar Python" como argumentos para os parâmetros tarefas e tarefa, respectivamente. A função irá adicionar a string "Estudar Python" à lista lista_tarefas.
adicionar_tarefa(lista_tarefas, "GitHub") # Mesma coisa da linha anterior.

print(lista_tarefas) # Imprime o conteúdo da lista lista_tarefas, que agora contém as tarefas "Estudar Python" e "GitHub", resultando na saída: ['Estudar Python', 'GitHub'].

# ==============================
# 10. Boas práticas
# ==============================

# Use nomes claros para as funções.
# Prefira funções pequenas.
# Cada função deve ter uma única responsabilidade.

def calcular_media(nota1, nota2): # A função calcular_media recebe dois parâmetros, nota1 e nota2.
    return (nota1 + nota2) / 2 # O cálculo da média é feito somando as duas notas (nota1 e nota2) e dividindo o resultado por 2, que é a quantidade de notas. O valor resultante é retornado pela função para ser utilizado posteriormente no código.

media = calcular_media(8, 10) # Chamando a função calcular_media e passando os argumentos 8 e 10 para os parâmetros nota1 e nota2, respectivamente. O resultado do cálculo da média (9.0) é retornado pela função e armazenado na variável media.

print(media)
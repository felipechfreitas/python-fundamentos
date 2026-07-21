# Programação Orientada a Objetos (POO)

# ==============================
# RESUMO RÁPIDO
# ==============================

# 1. POO é uma forma de organizar programas utilizando objetos.
# 2. Objetos representam elementos do mundo real.
# 3. Classes são modelos (ou moldes) utilizados para criar objetos.
# 4. Um objeto é uma instância criada a partir de uma classe. Um objeto possui atributos (características) e métodos (ações).
# 5. Uma mesma classe pode criar vários objetos do mesmo tipo, cada um com características próprias.
# 6. POO facilita organização, reutilização e manutenção do código.

# ==============================
# CONCEITOS IMPORTANTES
# ==============================

# Classe:
# É o molde utilizado para criar objetos.
#
# Exemplo:
# Classe Boneco
#
# Pense na classe como a impressora 3D pronta para fabricar bonecos.

# Objeto:
# É uma instância criada a partir de uma classe.
# Cada objeto possui seus próprios atributos e métodos.
#
# Exemplo:
# boneco1 = Boneco("Homem-Aranha", "Azul", 25)
#
# boneco1 é um objeto criado a partir da classe Boneco.

# Atributos:
# São as características de um objeto.
#
# Exemplo:
# nome
# cor
# altura

# Métodos:
# São as ações que um objeto pode executar.
#
# Exemplo:
# apresentar()
# pintar()
# embalar()

# __init__:
# É o método construtor.
# Ele é executado automaticamente sempre que um objeto é criado.
# Sua função é inicializar os atributos do objeto.

# self:
# Representa o próprio objeto que está sendo criado ou utilizado.
#
# Sempre que encontrar "self", pense:
#
# "este objeto"
#
# ou, no nosso exemplo:
#
# "este boneco"

# ==============================
# O exemplo da impressora 3D
# ==============================

# Imagine que você possui uma impressora 3D.
#
# Ela foi configurada para fabricar apenas bonecos.
#
# A impressora representa a CLASSE.
#
# Cada boneco produzido representa um OBJETO.
#
# Exemplo:
#
# Impressora 3D (Classe Boneco)
#
#        │
#        ├── Boneco 1
#        ├── Boneco 2
#        └── Boneco 3
#
# Todos são bonecos, mas cada um possui características próprias.

# Analogia:
#
# Impressora 3D  → Classe
# Boneco impresso → Objeto
#
# A impressora pode fabricar vários bonecos.
# Cada boneco terá suas próprias características, mesmo tendo sido criado pelo mesmo molde.

# ==============================
# Classe Boneco
# ==============================

class Boneco:

    def __init__(self, nome, cor, altura): # o __int__ é um método especial chamado de construtor. Ele é executado automaticamente quando um objeto é criado a partir da classe.

        # self representa o próprio objeto criado.
        # Pense no self como:
        #
        # "este boneco"

        # O atributo "nome" deste boneco recebe o valor informado.

        self.nome = nome
        self.cor = cor
        self.altura = altura

        # Exemplo:
        #
        # Boneco("Batman", "Preto", 30)
        #
        # nome = "Batman"
        # cor = "Preto"
        # altura = 30
        #
        # self.nome = "Batman"
        # self.cor = "Preto"
        # self.altura = 30
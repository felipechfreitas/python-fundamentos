from poo import Boneco # estou importando a classe Boneco do arquivo poo.py

# Criando objetos

boneco1 = Boneco("Homem-Aranha", "Azul", 25)
boneco2 = Boneco("Batman", "Preto", 30)
boneco3 = Boneco("Hulk", "Verde", 35)

print("===== BONECO 1 =====")
print(f"Nome: {boneco1.nome}")
print(f"Cor: {boneco1.cor}")
print(f"Altura: {boneco1.altura} cm")

# Acessando os atributos do objeto.
# Utilizamos a sintaxe:
#
# objeto.atributo
#
# Exemplo:
# boneco1.nome
#
# Significa:
# "Pegue o atributo nome do objeto boneco1."

print()

print("===== BONECO 2 =====")
print(f"Nome: {boneco2.nome}")
print(f"Cor: {boneco2.cor}")
print(f"Altura: {boneco2.altura} cm")

print()

print("===== BONECO 3 =====")
print(f"Nome: {boneco3.nome}")
print(f"Cor: {boneco3.cor}")
print(f"Altura: {boneco3.altura} cm")
"""
F strings
"""
nome = 'Yara'
idade = 36
altura = 1.43
e_maior = idade > 18
peso = 53
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(idade * altura)
print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')
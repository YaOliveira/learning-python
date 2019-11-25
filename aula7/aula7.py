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
print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')  # f strings
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))  # format
print('{n} tem {i} anos de idade e seu imc é {m:.2f}'.format(n = nome, i = idade, m = imc))  # format
print('{0} {0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
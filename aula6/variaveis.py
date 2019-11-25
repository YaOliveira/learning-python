"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Yara'
idade = 36
altura = 1.43
e_maior = idade > 18
peso = 53

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(idade * altura)
print(nome, 'tem', idade, 'de idade e seu imc é', peso // altura ** 2)
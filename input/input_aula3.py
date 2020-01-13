"""
Entrada de dados - input - aula 3
"""
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
ano_nascimento = 2020 - int(idade)

print()
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')
print()
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu em: {ano_nascimento}.')


numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
print(f'O resultado da soma é {numero_1 + numero_2} ')
"""
Condições IF, ELIF e ELSE
"""

# if False:
#     print("Verdadeiro.")
# elif True:
#     print("Qual é o seu nome? ")
# else:
#     print("Não é falso.")

"""
Operadores Relacionais - Aula 4
== igualdade
>maior que
>= maior ou igual que
< menor
<= menor ou igual que
!= diferente
"""

print (2 == 2)

num_1 = 2  # int
num_2 = '2' # str
num_3 = 3 #int

expressao = num_1 == num_2
expressao_ = num_1 > num_3

print(expressao)  #  irá imprimir o resultado da pergunta
print(expressao_)  #  irá imprimir o resultado da pergunta

nome = input ('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 17 # muito jovem
idade_maior = 45 # passou da idade

if idade >= idade_menor and idade <=idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} não pegar empréstimo.')


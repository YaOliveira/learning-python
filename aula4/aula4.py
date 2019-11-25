"""
Tipos de dados
str - string - texto - 'Texto' - "Texto"
int - inteiro - 123456 - 0 -10 -20 -50 -1500 1500
float - real/ponto flutuante 10.50 1.5
bool - booleano - lógico - True or False 10 == 10
"""
print('Yara', type('Yara'))  # str
print(type("Yara"))  # str
print("10", type("10"))  # str
print(10, type(10))  # int
print(10 == 10, type(10 == 10))  # True bool
print("l" == "L", type("l" == "L"))  # False bool
print("L" == "L", type("L" == "L"))  # True bool
print(bool(""))  # False
print(bool("10"))  # True
print(bool([]))  # False
print(bool(0))  # False
print ("yara", type("yara"), bool("yara"))  # Transformation uma string em boolean
print('10', type('10'), int('10'))  # Transformation uma string em integer
print('10', type('10'), type(int('10')))  # Transformation uma string em integer
print(10, type(10), int(10))  # não terá ponto flutuante
print(10, type(10), float(10))  # terá ponto flutuante

# String: nome
print('Yara', type('Yara'))

# Integer: idade
print('36', type(36))

# Float: altura
print(1.43, type(1.43))

# Verificar se é < 18
print(36 > 18, type(32 > 18))

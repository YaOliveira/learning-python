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

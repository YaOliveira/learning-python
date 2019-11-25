"""
Tipos de operações:
+, -, /, //, **, %, ()
"""
print('Multiplicação * ', 10 * 10)  # Multiplicação
print('Adição + ', 10 + 10)  # Adição
print('Subtração - ', 10 - 10)  # subtração
print('Divisão / ', 10 / 10)  # Divisão
# print('Multiplicação com string', '10' * '10') # Multiplicação com string - neste caso dá erro
print('Multiplicação com string', 10  * '10') # Multiplicação com string - operador de Repetição
print('Concatenando +', 'Yara' + 'Bruno')  # Concatenando strings
print ('Concatenando +', 'Yara' + ' ' + 'Bruno e ele tem ' + str(42) + ' anos')  # Concatenando strings com espaço
# print ('Concatenando +', 5 + '5')  # Soma/ Concatenação - neste caso dá erro
print(10 / 3)  # gera resultado da divisão com ponto flutuante
print(10 // 3)  # gera resultado da divisão arredondado e sem ponto flutuante
print(2 ** 10)  # 2 elevado a 10, ou seja, exponenciação
print(10 % 2)  # módulo da divisão sem sobra, ou seja, 0
print(9 % 2)  # módulo da divisão
print(5 + 2 * 10) # parênteses, altera a precedência do operador result 25
print((5 + 2) * 10) # parênteses, altera a precedência do operador result 70
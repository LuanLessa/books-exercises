""" Try it out
1 Use float() to create a number from a string like '12.34'. Make sure the result is 
really a number!
2 Try using int() to create an integer from a decimal number like 56.78. Did the answer 
get rounded up or down?
3 Try using int() to create an integer from a string. Make sure the result is really an 
integer! """

# 1
number = float("12.34")
print("A variável com o valor:", number, "é do tipo", type(number))

# 2
print(int(56.78)) # A resposta sempre será arredondada para baixo

# 3
number = int("12")
print("A variável com o valor:", number, "é do tipo", type(number))
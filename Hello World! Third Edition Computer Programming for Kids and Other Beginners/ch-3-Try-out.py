""" Try it out
1 Solve the following problems either using interactive mode or by writing a small 
program:
a) Three people ate dinner at a restaurant and want to split the bill. The total is $35.27,
and they want to leave a 15% tip. How much should each person pay?
b) Calculate the area and perimeter of a rectangular room, 12.5 meters by 16.7 meters.
2 Write a program to convert temperatures from Fahrenheit to Celsius. The formula for 
that is C = 5 / 9 * (F - 32).
3 Do you know how to figure out how long it will take to get somewhere in a car? The 
formula (in words) is “travel time equals distance divided by speed.” Make a program 
to calculate the time it will take to drive 200 km at 80 km per hour and display the 
answer. """

# 1
# a
people = 3
total = 35.27
tipRate = total * 0.15
print("O valor que cada pessoa pagará adicionando a gorgeta de 15% é de, R$:", (total + tipRate)/people)
# b
largura = 12.5
altura = 16.7
area = largura * altura
perimmetro = largura + altura
print("A área do retângulo é", area,"e o perímetro é", perimmetro)

# 2
temperaturaF = float(input("Digite uma temperatura em Fahrenheit: "))
print("A temperatura convertida para Celcius é de: ", 5 / 9 * (temperaturaF - 32))

# 3
print("O tempo de chegada é de aproximadamente:", 200 // 80, "horas e", int(200 % 80 / 80 * 60), "minutos.")
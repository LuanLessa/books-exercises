""" Try it out
1 Make a variable and assign a number to it (any number you like). Then display your
variable using print.
2 Modify your variable, either by replacing the old value with a new value or by adding
something to the old value. Display the new value using print.
3 Make another variable and assign a string (some text) to it. Then display it using
print.
4 Just like in the last chapter, in interactive mode, get Python to calculate the number of
minutes in a week. But this time, use variables. Make variables for days_per_week,
hours_per_day, and minutes_per_hour (or make up your own names), and then multiply them together.
5 People are always saying there’s not enough time to get everything done. How many
minutes would there be in a week if there were 26 hours in a day? (Hint: change the
hours_per_day variable.)
"""
# 1
myNumber = 30
print(myNumber)
# 2
myNumber = myNumber + 30
print(myNumber)
# 3
myText = "Hello World!"
print(myText)
# 4
week = 7
day = 24
hour = 60

print("O número de minutos em uma semana é de", week * day * hour,"minutos.")
print("O número de horas em uma semana é de", week * day,"horas.")
# 5
day = 26
print("O número de minutos em uma semana é de", week * day * hour,"minutos.")
print("O número de horas em uma semana é de", week * day,"horas.")
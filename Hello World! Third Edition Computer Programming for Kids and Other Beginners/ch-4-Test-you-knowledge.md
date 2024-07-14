# Test your knowledge

## 1 - When you use int() to convert a decimal number to an integer, does the result get rounded up or down?
Será sempre arredondado para baixo.

## 2 - If you entered thing1 in the interactive shell, and it told you '4', what would type(thing1) be?
Será do tipo string.

## 3 - (Extra challenging question): Without using any other functions besides int(), how could you get a number to round off instead of rund down? (For example, 13.2 would round down to 13, but 13.7 would round up to 14.)
number = 13.2 ou 13.7
if number - int(number) < 0.6:
    int(number)
else:
    int(number) + 1
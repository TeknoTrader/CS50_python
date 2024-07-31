import cs50
from cs50 import get_int

height = get_int("Select the height: ")

if (height < 1) or (height > 8):
    height = get_int("Select the height: ")

for i in range(1, height + 1):
    if (i != height):
        # Instead of "*" symbol in the print function, you can use a for/while loop to print in the same line
        print(" " * (height - i), end='')
    print("#" * i, end='  ')
    print("#" * i)

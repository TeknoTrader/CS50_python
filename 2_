import cs50
from cs50 import get_int

card_number = get_int("Insert your card number: ")

card_number = str(card_number)

# Here it comes a function that detects if the card number is valid: it is the primary filter for the validation
def Luhn():
    first_array = []
    second_array = []

    i = len(card_number) - 1
    while i >= 0:
        digit = int(card_number[i])
        if (len(card_number) - i) % 2 == 0:
            moltiplication = digit * 2
            if moltiplication > 9:
                # Sum of the result
                second_array.append(moltiplication - 9)
            else:
                second_array.append(moltiplication)
        else:
            first_array.append(digit)
        i -= 1

    summatory1 = sum(second_array)
    summatory2 = sum(first_array)

    total_sum = summatory1 + summatory2
    if total_sum % 10 == 0:
        return True
    else:
        return False


# Mastercard requirements
mastercard_number1 = 5
mastercard_number2 = range(1, 6)
mastercard_digits = 16

# Visa requirements
visa_number = 4
visa_digits = range(13, 17)

# American Express requirements
amex_number1 = 3
amex_number2 = [4, 7]
amex_digits = 15

if Luhn():
    if (int(card_number[0]) == visa_number) and (len(card_number) in visa_digits):
        print("VISA")
    elif (int(card_number[0]) == amex_number1) and (int(card_number[1]) in amex_number2) and (len(card_number) == amex_digits):
        print("AMEX")
    elif (int(card_number[0]) == mastercard_number1) and (int(card_number[1]) in mastercard_number2) and (len(card_number) == mastercard_digits):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")

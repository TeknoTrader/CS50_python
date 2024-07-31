import cs50

arac = 0
number_words = 100
End_sentence = ['.', '!', '?']


def main():
    text = cs50.get_string("Insert you text:\n")
    letters = 0
    words = 1
    phrases = 0

    for i in range(len(text)):
        if (Letter(text[i])):
            letters += 1
        elif (text[i] == ' '):
            words += 1
        elif (Separator(text[i]) and Separator(text[i - 1]) == False):
            phrases += 1

    # Index calculation
    L = letters / words * number_words
    S = phrases / words * number_words
    index = 0.0588 * L - 0.296 * S - 15.8
    INDEX = round(index)

    # Print results
    if (INDEX < 1):
        print("Before Grade 1\n")
    elif (INDEX >= 16):
        print("Grade 16+\n")
    else:
        for i in range(2, 16):
            if (INDEX == i):
                print("Grade", INDEX)

# Check if the element is a letter
def Letter(element):
    uppercase = (element >= 'a') and (element <= 'z')
    lowercase = (element >= 'A') and (element <= 'Z')
    if (uppercase or lowercase):
        return True
    else:
        return False

# Check if the element is a punctuation mark
def Separator(element):
    for i in range(len(End_sentence)):
        if (element == End_sentence[i]):
            return True
            break
    else:
        return False

# Let's run the program
main()

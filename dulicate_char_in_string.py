mystring = input("enter string")
char_validated = []
for letter in mystring:
    if letter in char_validated:
        continue
    char_validated.append(letter)

    count = 0
    for letter2 in mystring:
        if letter == letter2:
            count+=1

    if count > 0:
        print(f"{letter} is repeated {count} times")

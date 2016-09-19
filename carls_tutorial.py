password1 = 'justplaintext'
password2 = 'JustCapitalLetters'
password3 = 'TheWh01e5heb4ng'


def lesson_one(password):
    print(password)


def lesson_two(password):
    for character in password:
        print(character)


def lesson_three(password):
    for character in password:
        if character.isupper():
            print('The password contains at least one capital letter.')
            break


def lesson_four(password):
    for character in password:
        if character.isupper():
            print('The password contains at least one uppercase character.')
            break

    for character in password:
        if character.islower():
            print('The password contains at least one lowercase character.')
            break

    for character in password:
        if character.isnumeric():
            print('The password contains at least one number.')
            break


def lesson_five(password):
    uppercase = False
    lowercase = False
    numeric = False

    for character in password:
        if character.isupper():
            uppercase = True
            break

    for character in password:
        if character.islower():
            lowercase = True
            break

    for character in password:
        if character.isnumeric():
            numeric = True
            break

    if uppercase and lowercase and numeric:
        print('This is a valid password.')
    else:
        print('This is not a valid password. Please ensure that your password contains at least one uppercase '
              'character, one lowercase character and one number.')

lesson_five(password3)

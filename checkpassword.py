DIGITS = '0123456789'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def check(password):
    '''Return True if password has at least one digit and one uppercase
    letter.  Otherwise, return False.
    '''
    
    has_uppercase_letter = False
    has_digit_letter = False

    for char in password:
        for char in DIGITS:
            if char in password:
                has_digit = True
                
        for char in UPPERCASE_LETTERS:
            if char in password:
                has_uppercase_letter = True

    return has_digit and has_uppercase_letter
            

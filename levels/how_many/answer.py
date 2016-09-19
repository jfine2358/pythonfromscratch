'''This is a model answer for this level.'''

DIGITS = '0123456789'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Decision here. Do we says numerals or digits? User's language or
# ours? When do we insist on our own language? Is it pedagogic goal?


def how_many_digits(password):

    how_many = 0                # Initialize.
    for char in password:
        if char in DIGITS:
            how_many = how_many + 1 # Not '+=' yet!
            
    return how_many


def how_many_lower(password):

    how_many = 0                # Initialize.
    for char in password:
        if char in LOWER:
            how_many = how_many + 1 # Not '+=' yet!
            
    return how_many


def how_many_upper(password):

    how_many = 0                # Initialize.
    for char in password:
        if char in UPPER:
            how_many = how_many + 1 # Not '+=' yet!
            
    return how_many

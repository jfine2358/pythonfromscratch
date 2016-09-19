Prerequisites
-------------

 - python and IDLE is installed on student machine
 

Lesson steps
------------

1. Show a full working solution without too much explanations::

    password = input('Please enter your password:')
    
    if len(password) < 5:
        raise Exception('Password should be at least 5 characters long')
    
    number_of_numbers = 0
    number_of_uppercase_letters = 0
    
    for letter in password:
        if letter in range('A', 'Z'):
            number_of_uppercase_letters += 1
        elif letter in range('0', '9'):
            number_of_numbers += 1
        elif letter not in range('a', 'z'):
            raise Exception('Your password contains character that is not accepted:', letter)
    
    if number_of_numbers == 0:
        raise Exception('Password should contain at least one number')
    if number_of_uppercase_letters == 0:
        raise Exception('Password should contain at least one letter')

        
    print 'Success! Your password is safe enough!'
    
    
2. Explain how to run it through IDLE
3. Go through the problem line by line
3.1. This is how ask can ask user a question and get his keyboard input. Tell about variables and how user input is
     going to be stored in ``password`` variable::
     
      password = input('Please enter your password:')

3.2. Lets validate or password length first. This allows to explain how 'if' statment works without
     needing to go through for loop yet::

      if len(password) < 5:
         raise Exception('Password should be at least 5 characters long')
      
3.2. Teach how to calculate number of upper case letters in password. This I think is a bit hard
     for single step and would be good to split into smaller chunks. We need to explain
     `for X in Y`, and `range()` function and `if X in range()`. And also `x += 1`

    number_of_uppercase_letters = 0
    
    for letter in password:
        if letter in range('A', 'Z'):
            number_of_uppercase_letters += 1


    

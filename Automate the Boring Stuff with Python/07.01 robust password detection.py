#! python
# Script to detect a robust password

from re import compile, search

# password input

def checkpass(password):
    # Eight characters, upcase and lowercase, one digit
    # Creating patterns
    eightChar = re.compile(r'\d{8}|\w{8}')   # Eight characters
    lowerChar = re.compile(r'[a-z]')         # Lowercase
    upperChar = re.compile(r'[A-Z]')         # Uppercase
    digitChar = re.compile(r'\d')            # One digit
    
    # Validation
    if eightChar.search(password) == None:
        print('Your password must have at least 8 characters')
    elif lowerChar.search(password) == None:
        print('Your password must have lowercase characters')
    elif upperChar.search(password) == None:
        print('Your password must have uppercase characters')
    elif digitChar.search(password) == None:
        print('Your password must have at least 1 digit')
    else:
        print('Your password is safe')
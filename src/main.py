import string
import random 

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
TYPES = ["MIN","MAY","DIG","SYMB"]




def generate_password():
    password=""
    while not validate(password):
        password=""
        size = random.randint(8,16)
        for i in range(0,size):
            selector = random.choice(TYPES)
            if selector == "MIN":
                password += random.choice(string.ascii_lowercase)
            if selector == "MAY":
                password += random.choice(string.ascii_uppercase)
            if selector == "DIG":
                password += random.choice(string.digits)
            if selector == "SYMB":
                password += random.choice(SYMBOLS)
        
        #print(password)

    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
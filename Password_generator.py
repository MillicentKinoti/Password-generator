
#random module performs random generations
#string module contains various string constant which contains the ascii characters of all cases

import random
import string


def get_random_password():
    letters_of_the_password=int(input("Enter the number of letters in your password: "))
    numbers_of_the_password=int(input("Enter the number of numbers in your password: "))
    symbols_of_the_password=int(input("Enter the number of symbols in your password: ")) 

    letters_pass= ''.join(random.choice(string.ascii_letters) for i in range(letters_of_the_password))
    numbers_pass= ''.join(random.choice(string.digits) for i in range(numbers_of_the_password))
    symbols_pass=''.join(random.choice(string.punctuation) for i in range(symbols_of_the_password))
    password= letters_pass + numbers_pass+ symbols_pass
    if len(password) < 6:
        print("Password should be a minimum of 6 characters")
        exit()

    result=random.sample(password, len(password))
    random_password= ''.join((result))
    print('Your password is {}'.format(random_password))

print(get_random_password())



    

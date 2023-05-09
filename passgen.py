#Base Code Block by DabCat95 5/9/2023
import random
import string

def generate_password(length):
    # Define password char's
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    #Combine character sets and build pool
    all_chars = lowercase + uppercase + digits + symbols

    #Shuffle chars to make password random
    shuffled_chars = random.sample(all_chars, len(all_chars))

    #Generate password after shuffle
    password = ''.join(random.sample(shuffled_chars, length))

    return password

#Main Code Loop
password = generate_password(14) #Generate random password and diplay
print(password)
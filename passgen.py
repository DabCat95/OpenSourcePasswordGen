#Base Code Block by DabCat95 5/9/2023
import secrets
import string

def generate_password(length):
    #Define alphanumerics
    alphabet = string.ascii_letters + string.digits

    #Genertate passwords until one meets requirements
    while True:
        #Use secrets to generate random password
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        #Check if password meets requirements
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break

    #return generated password
    return password

#Main Code Loop
password = generate_password(14) #Generate a random 14 character password
print(password)
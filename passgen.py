#Base Code Block by DabCat95 5/9/2023
import secrets
import string
#import crpytographic libraries
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

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
    print("Password generation using Secrets complete.")
    return password

def generate_aes_key():
    #Gen random 32-byte key and return
    key = secrets.token_bytes(32)
    return key

#Run password through AES encryption
def encrypt_aes(password, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad(password.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    print("Password AES Encyption complete. Returning Encypted Password...\n")
    return encrypted_text.hex()

#Main Code Loop
password = generate_password(12) #Generate a random 12 character password
key = generate_aes_key()
ePass = encrypt_aes(password, key)
print(ePass)
#print(password)
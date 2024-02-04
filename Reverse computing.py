import hashlib
import random
import string

def encrypt_and_shorten_code(original_code, rounds):
    # Generate a random salt
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    # Combine the original code with the salt
    salted_code = original_code + salt
    
    # Apply multiple rounds of reverse computing to the salted code
    encrypted_code = salted_code
    for _ in range(rounds):
        encrypted_code = ''.join(['1' if bit == '0' else '0' for bit in encrypted_code])
    
    # Shorten the encrypted code using a hash function (SHA-256)
    shortened_code = hashlib.sha256(encrypted_code.encode()).hexdigest()
    
    return salted_code, shortened_code

# Test the encryption and shortening function
original_code = "SecretSecurityCode123"
rounds = 5
salted_code, encrypted_and_shortened_code = encrypt_and_shorten_code(original_code, rounds)

print("Original Security Code:", original_code)
print("Salted Code:", salted_code)
print("Encrypted and Shortened Code:", encrypted_and_shortened_code

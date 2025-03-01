import random

# Utility function to check for primality (simple and not efficient for large numbers)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Generate a prime number in a given range (for demonstration, use small primes)
def generate_prime_candidate(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# Generate RSA public and private keys
def generate_keys():
    # Step 1: Generate two distinct prime numbers
    p = generate_prime_candidate()
    q = generate_prime_candidate()
    while q == p:
        q = generate_prime_candidate()
    
    # Step 2: Compute n and φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose public exponent e (commonly 65537)
    e = 65537
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    # Ensure e and φ(n) are co-prime; if not, choose a different e
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    
    # Step 4: Compute d, the modular inverse of e modulo φ(n)
    def modinv(a, m):
        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        return x % m
    d = modinv(e, phi)
    
    return ((n, e), (n, d))  # Return public and private keys

# Function to encrypt a plaintext message using the public key
def encrypt(public_key, plaintext):
    n, e = public_key
    # Convert plaintext into an integer representation
    m = int.from_bytes(plaintext.encode('utf-8'), 'big')
    # Encrypt: ciphertext c = m^e mod n
    c = pow(m, e, n)
    return c

# Function to decrypt a ciphertext using the private key
def decrypt(private_key, ciphertext):
    n, d = private_key
    # Decrypt: m = c^d mod n
    m = pow(ciphertext, d, n)
    # Convert integer back to bytes then to string
    length = (m.bit_length() + 7) // 8
    plaintext = m.to_bytes(length, 'big').decode('utf-8', errors='ignore')
    return plaintext

# Example usage
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello, RSA!"
ciphertext = encrypt(public_key, message)
print("Encrypted:", ciphertext)

decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted:", decrypted_message)

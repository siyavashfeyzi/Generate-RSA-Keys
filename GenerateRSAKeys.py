from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)


# Generate public key
public_key = private_key.public_key()
print("Public key generated.")

# Save private key to a string
private_key_str = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')
print("Private key saved to string.")

# Save public key to a string
public_key_str = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')
print("Public key saved to string.")

print("Private Key:\n", private_key_str)
print("Public Key:\n", public_key_str)

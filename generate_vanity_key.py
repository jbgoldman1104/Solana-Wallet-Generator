import nacl.signing
import base58
import os

def generate_vanity_keypair(prefix):
    prefix_bytes = prefix.encode('utf-8')
    while True:
        # Generate a new random keypair
        seed = os.urandom(32)
        private_key = nacl.signing.SigningKey(seed)
        private_key_bytes = private_key.encode()

        # Check if the private key matches the desired prefix
        if private_key_bytes.startswith(prefix_bytes):
            # Generate the corresponding public key
            public_key = private_key.verify_key
            public_key_bytes = public_key.encode()

            # Encode in base58 for Solana compatibility
            private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')
            public_key_base58 = base58.b58encode(public_key_bytes).decode('utf-8')

            return private_key_base58, public_key_base58

# Desired prefix for the private key
desired_prefix = "ABC"

private_key, public_key = generate_vanity_keypair(desired_prefix)

print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
from cryptography.fernet import Fernet

# Function to save the key to a file
def save_key_to_file(key, filename="secret.bin"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key_from_file(filename="secret.bin"):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Ask the user for the message to encrypt
message = input("Enter your custom messageeeeeeeeeees: ")

# Generate a secret key
key = Fernet.generate_key()
print("The secret key has been generated and saved to 'secret.key'.")

# Save the key to a file
save_key_to_file(key)

# Load the key back from the file for decryption
key = load_key_from_file()

# Initialize the Fernet object
fernet = Fernet(key)

# Encrypt the message
enc_message = fernet.encrypt(message.encode())
print("\nThe encrypted message is:", enc_message)

# Decrypt the message
dec_message = fernet.decrypt(enc_message).decode()
print("\nThe decrypted message is:", dec_message)

import string

class TextEncryptor:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.alphabet = list(string.ascii_lowercase)
        self.encryption_mapping = self.generate_encryption_mapping()
        self.decryption_mapping = {v: k for k, v in self.encryption_mapping.items()}

    def generate_encryption_mapping(self):
        # Generates encryption based on secret key
        shifted_alphabet = self.shift_alphabet(self.secret_key)
        return {self.alphabet[i]: shifted_alphabet[i] for i in range(len(self.alphabet))}

    def shift_alphabet(self, key):
        # Create a shifted version of the alphabet based on the key
        shift = sum(int(digit) for digit in key) % 26
        return self.alphabet[shift:] + self.alphabet[:shift]

    def encrypt(self, text):
        # Convert text to lowercase
        # Replace each letter with encryption
        encrypted_text = ''.join([self.encryption_mapping.get(char, char) for char in text.lower()])
        return encrypted_text

    def decrypt(self, encrypted_text, input_key):
        # Decrypt to go back to original text, only if the correct key is provided
        if input_key == self.secret_key:
            decrypted_text = ''.join([self.decryption_mapping.get(char, char) for char in encrypted_text])
            return decrypted_text
        else:
            return "Incorrect key! Decryption failed."

# Example usage:

# User inputs a secret key
secret_key = "1234"
encryptor = TextEncryptor(secret_key)

# List of original messages
original_messages = [
    "Hello World",
    "Python programming is fun",
    "Keep calm and carry on",
    "Encryption is the key to security",
    "Learning never exhausts the mind",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be that is the question",
    "All that glitters is not gold",
    "A journey of a thousand miles begins with a single step",
    "Better late than never",
    "Actions speak louder than words",
    "Every cloud has a silver lining",
    "Fortune favors the brave",
    "Practice makes perfect",
    "The pen is mightier than the sword",
    "Time and tide wait for no man",
    "You can't judge a book by its cover",
    "Absence makes the heart grow fonder",
    "Beauty is in the eye of the beholder",
    "Birds of a feather flock together"
]


# Encrypt all messages and store them
encrypted_messages = []
for i, original_message in enumerate(original_messages, 1):
    encrypted_message = encryptor.encrypt(original_message)
    encrypted_messages.append(encrypted_message)
    # print(f"Original Message {i}: {original_message}")
    print(f"Encrypted Message {i}: {encrypted_message}")
    print("\n" + "-"*40 + "\n")

# Prompt the user to input the secret key for decryption
input_key = input("Enter the secret key to decrypt the messages: ")

# Decrypt all messages using the provided key
for i, encrypted_message in enumerate(encrypted_messages, 1):
    decrypted_message = encryptor.decrypt(encrypted_message, input_key)
    print(f"Encrypted Message {i}: {encrypted_message}")
    print(f"Decrypted Message {i}: {decrypted_message}")
    print("\n" + "-"*40 + "\n")

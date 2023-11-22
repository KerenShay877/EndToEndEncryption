def xor_encrypt(message, key):
    encrypted = ''.join(chr(ord(char) ^ key) for char in message)
    return encrypted

def xor_decrypt(encrypted_message, key):
    return xor_encrypt(encrypted_message, key)  # XOR encryption is symmetric

def send_message(sender, receiver, message, key):
    encrypted_message = xor_encrypt(message, key)
    print(f"{sender} sent an encrypted message to {receiver}: {encrypted_message}")
    return encrypted_message

def receive_message(sender, receiver, encrypted_message, key):
    decrypted_message = xor_decrypt(encrypted_message, key)
    print(f"{receiver} received an encrypted message from {sender}: {decrypted_message}")
    return decrypted_message
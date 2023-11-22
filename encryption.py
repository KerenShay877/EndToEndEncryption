def xor_encrypt(message, key):
    encrypted = ''.join(chr(ord(char) ^ key) for char in message)
    return encrypted

def xor_decrypt(encrypted_message, key):
    return xor_encrypt(encrypted_message, key)  # XOR encryption is symmetric
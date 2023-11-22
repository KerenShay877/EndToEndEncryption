from authentication import register, login
from key_exchange import generate_shared_key
from encryption import xor_encrypt, xor_decrypt
from transmission import send_message, receive_message

def main():
    # User registration
    register("user1", "password1")
    register("user2", "password2")

    # User login
    login("user1", "password1")
    login("user2", "password2")

    # Key exchange
    shared_key_user1 = generate_shared_key("password1")
    shared_key_user2 = generate_shared_key("password2")

    # Secure transmission
    message1 = send_message("user1", "user2", "Hello, user2!", shared_key_user1)
    message2 = receive_message("user1", "user2", message1, shared_key_user2)

if __name__ == "__main__":
    main()
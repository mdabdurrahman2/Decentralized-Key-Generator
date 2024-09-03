# This is the Key Generation Server

import socket
import rsa
import Generate_Server_Keys
import RSA_encrypt_decrypt
import Response_Phrase_Generation

private_key,public_key = RSA_encrypt_decrypt.loadKeys()

print(public_key)
print(private_key)


# We need to format the public and the private keys
public_key_bytes = public_key.save_pkcs1(format='PEM')
private_key_bytes = private_key.save_pkcs1(format='PEM')
print('This is the public key in bytes: ')
print(public_key_bytes)
print('This is the private key in bytes: ')
print(private_key_bytes)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)

while True:
    # Connection being made with the key generation client!
    print("Waiting for Connection .... ")
    connection,client_address = server_socket.accept()
    print(f"Connected to f{client_address}")
    print("Connection made successfully!")

    connection.sendall(public_key_bytes)

    received_encrypted_data = connection.recv(4096)

    print("THis is the received encrypted data from the key generation client: ")

    print(received_encrypted_data)

    received_decrypted_data = RSA_encrypt_decrypt.decrypt(received_encrypted_data,private_key)

    print("This is the received decrypted data from the key generation client: ")
    print(received_decrypted_data)

    response_secret_otp = Response_Phrase_Generation.generate_int_from_random(received_decrypted_data)

    with open("key_store.txt",'a') as file:
        file.write(response_secret_otp + "\n")

    print("The response secret phrase has been added to the key store!")

    connection.close()






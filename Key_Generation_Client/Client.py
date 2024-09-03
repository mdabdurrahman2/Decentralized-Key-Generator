import rsa
import socket
import RSA_encrypt_decrypt
from Secret_Phrase_Generation import generate_int_from_random

server_ip = '127.0.0.1'
server_port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((server_ip,server_port))

public_key_bytes_received = sock.recv(4096)

print("This is the public key received from the server: ")
print(public_key_bytes_received)

# bytes --> rsa format
received_public_key  = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

print("This is the rsa format of the public key received from the server: ")
print(received_public_key)

with open('public_key_server.pem','wb') as file:
    file.write(public_key_bytes_received)


seed = input("Provide the seed value here: ")
secret_phrase = str(generate_int_from_random(seed))

print("This is the generated secret value: " + secret_phrase)

encrypted_data = RSA_encrypt_decrypt.encrypt(secret_phrase,received_public_key)

print("This is the encrypted secret phrase: ")

print(encrypted_data)

sock.sendall(encrypted_data)

# close the connection
sock.close()
# Decentralized Key Generator
 This project is a decentralized key generator implemented using Python and socket programming. The server generates RSA public and private keys and listens for incoming client connections. Upon connection, the server sends the public key to the client. The client then uses this public key to encrypt a secret phrase generated based on a user-provided seed and sends the encrypted data back to the server. The server decrypts this data using its private key, generates a response phrase, and stores it securely. This decentralized approach allows for secure key exchange and secret sharing without centralized intermediaries.

 
# Features
- **RSA Key Generation:** The server generates RSA public and private keys for secure communication.
- **Public Key Exchange:** The server sends its public key to the client for encrypting sensitive data.
- **Secret Phrase Encryption:** The client encrypts a secret phrase using the public key and sends it to the server.
- **Decentralized Key Storage:** The server securely stores the decrypted data in a key store.
  
# Requirements
Python 3.9
rsa Python library

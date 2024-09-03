import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def loadKeys():
    with open('public_Key_Server.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('private_Key_Server.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


# generateKeys()

# private_Key, public_Key = loadKeys()
#
# print("This is the private key:")
# print(private_Key)
#
# print("This is the public key:")
# print(public_Key)
#
# print("This is the ciphertext ------------------------------------------------------------------------------------------- ")
# plain_text = "This is the sample plaintext message!"
# cipher_text = encrypt(plain_text, public_Key)
# print(cipher_text)
# #
# print("This is the decrypted text -----------------------------------------------------------------------------------------")
# plain_text_after_decryption = decrypt(cipher_text, private_Key)
# print(plain_text_after_decryption)


import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('public_Key_Server.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('private_Key_Server.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

generateKeys()


import rsa

def createKeys():
    pk, sk = rsa.newkeys(1028)

    with open("./keys/pk.pem", "r+") as f1:
        f1.write(pk.save_pkcs1("PEM").decode())

    with open("./keys/sk.pem", "r+") as f2:
        f2.write(sk.save_pkcs1("PEM").decode())

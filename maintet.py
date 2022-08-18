import hashlib

msg = '11'
pwd1 = hashlib.sha256(msg.encode('utf8')).hexdigest()
pwd2 = hashlib.sha256(pwd1.encode('utf-8')).hexdigest()
print("pwd2 = ",pwd2)


def encrypt(passwords):
    for i in range(2):
        passwords = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
    return passwords

print(encrypt('11'))


def num(n):
    if  n == 1:
        return 1
    else:
        return n + num(n-1)

print(num(998))
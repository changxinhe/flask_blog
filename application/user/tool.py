import hashlib

#密码加密,利用hash256两次加密
def encrypt(passwords):
    for i in range(2):
        passwords = hashlib.sha256(passwords.encode('utf-8')).hexdigest()
    return passwords
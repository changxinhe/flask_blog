import hashlib

from werkzeug.security import check_password_hash, generate_password_hash

x = 'asdaijfkjfsn'
pwd_x = hashlib.sha256(x.encode('utf-8')).hexdigest()
flag = check_password_hash(pwd_x,x)

pwd1 = '1234'
pwd2 = '1234'
pwd1_1 = generate_password_hash(pwd1)
pwd2_2 = generate_password_hash(pwd2)
print(pwd1_1,'\n',pwd2_2,sep='')

p1 = check_password_hash(pwd1_1,pwd2)

print(p1)
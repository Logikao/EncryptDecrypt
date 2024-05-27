from cryptography.fernet import Fernet

# Carregar a chave de criptografia
with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Carregar e descriptografar a senha
with open('config.enc', 'rb') as enc_file:
    cipher_text = enc_file.read()

db_password = cipher_suite.decrypt(cipher_text).decode('utf-8')

print(db_password)


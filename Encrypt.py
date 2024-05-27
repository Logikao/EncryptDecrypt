from cryptography.fernet import Fernet
import os, ctypes
# Geração de uma chave de criptografia
key = Fernet.generate_key()
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Criptografando a senha
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b'PasswordSenha')

with open('config.enc', 'wb') as enc_file:
    enc_file.write(cipher_text)


#ocultar o arquivo

def definir_arquivo_oculto(caminho_arquivo):
    # Definir atributo oculto
    FILE_ATTRIBUTE_HIDDEN = 0x02
    try:
        ret = ctypes.windll.kernel32.SetFileAttributesW(caminho_arquivo, FILE_ATTRIBUTE_HIDDEN)
        if ret:
            print(f'{caminho_arquivo} foi definido como oculto.')
        else:
            print(f'Falha ao definir {caminho_arquivo} como oculto.')
    except Exception as e:
        print(f'Erro ao definir o arquivo como oculto: {e}')

# Caminho do arquivo existente
file_path = 'key.key' #nome do arquivo

# Definir o arquivo como oculto
definir_arquivo_oculto(file_path)



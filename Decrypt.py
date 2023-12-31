import os
import pyaes
from time import sleep


def Decrypt():
    print("Estamos Descryptografando seus dados, aguarde um momento...")
    sleep(5)

    # abrir o arquivo criptografado
    file_name = "Europa.csv.testeransmware"
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Chave para descriptografia
    key = b"luizdeveaprender"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o arquivo descriptografado
    new_file = "Europa.csv"
    new_file = open(f'{new_file}', "wb")
    new_file.write(decrypt_data)
    new_file.close()
    print("Seus dados foram Restaurados com sucesso! ...")

if __name__ == '__main__':
    Decrypt()

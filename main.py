import sys
import os

# Funzione per generare la keystream pseudo-casuale di OTP
def otp_string_generator(length: int) -> str:
    return ''.join(format(byte, '08b') for byte in os.urandom(length // 8))


# Funzione per eseguire la cifratura della stringa in chiaro
def otp_encryption(plain_text: str, keystream: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(plain_text, keystream))


# Funzione per eseguire la decifratura della stringa in chiaro
def otp_decryption(cipher_text: str, keystream: str) -> str:
    temp = ''.join(str(int(x) ^ int(y)) for x, y in zip(cipher_text, keystream))
    return ''.join(chr(int(temp[i:i+8], 2)) for i in range(0, len(temp), 8))

# Funzione per salvare un file
def save_file(path: str, value: str) -> str:
    file = open(path, "w")
    file.write(value)
    file.close()

# Funzione per leggere il contenuto di un file
def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()
    

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Number of arguments incorrect, see the instructions in the README file")
    else:
        # -c -in file -out cipher
        if sys.argv[1] == "-c":
            # Logica per cifrare il messaggio
            user_input = read_file(sys.argv[3])
            plain_text: str = ''.join(format(ord(char), '08b') for char in user_input)
            
            keystream = otp_string_generator(len(plain_text))
            cipher_text = otp_encryption(plain_text=plain_text, keystream=keystream)
            
            # Salvataggio dei due file, ovvero testo cifrato e keystream
            save_file(path=f"./keystream", value=keystream)
            save_file(path=f"./{sys.argv[5]}", value=cipher_text)
            print("Ecryption done correctly!")
        # -d -in cipher -out file -key keystream
        elif sys.argv[1] == "-d":
            # Logica per decifrare il messaggio
            cipher_text = read_file(sys.argv[3])
            keystream = read_file(sys.argv[7])

            # Salvataggio del file, per il testo in chiaro
            plain_text = otp_decryption(cipher_text=cipher_text, keystream=keystream)
            save_file(path=f"./{sys.argv[5]}", value=plain_text)
            print("Decryption done correctly!")
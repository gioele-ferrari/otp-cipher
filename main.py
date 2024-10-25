import sys
import random
import hashlib

# Funzione per generare la keystream pseudo-casuale di OTP basata su una chiave
def otp_string_generator(key: str, length: int) -> str:
    seed = int(hashlib.sha256(key.encode()).hexdigest(), 16)
    random.seed(seed)

    return ''.join(format(random.getrandbits(8), '08b') for _ in range(length // 8))


# Funzione per eseguire la cifratura della stringa in chiaro
def otp_encryption(plain_text: str, keystream: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(plain_text, keystream))

# Funzione per eseguire la decifratura della stringa in chiaro
def otp_decryption(cipher_text: str, keystream: str) -> str:
    temp = ''.join(str(int(x) ^ int(y)) for x, y in zip(cipher_text, keystream))
    return ''.join(chr(int(temp[i:i+8], 2)) for i in range(0, len(temp), 8))


# Funzione per salvare un file
def save_file(path: str, value: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(value)

# Funzione per leggere il contenuto di un file
def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()
    
if __name__ == "__main__":
    if len(sys.argv) < 8:
        print("Numero di argomenti incorretti, consula il file README per l'uso.")
    else:
        # -c -in file -out cipher -key chiave
        if sys.argv[1] == "-c":
            # Logica per cifrare il messaggio
            user_input = read_file(sys.argv[3])
            plain_text = ''.join(format(ord(char), '08b') for char in user_input)
            
            key = sys.argv[7]
            keystream = otp_string_generator(key=key, length=len(plain_text))
            cipher_text = otp_encryption(plain_text=plain_text, keystream=keystream)
            
            # Salvataggio dei due file, ovvero testo cifrato e keystream
            save_file(path=f"./keystream", value=keystream)
            save_file(path=f"./{sys.argv[5]}", value=cipher_text)
            print("Cifratura completata correttamente, file disponibili in questa directory.")
        
        # -d -in cipher -out file -key chiave
        elif sys.argv[1] == "-d":
            # Logica per decifrare il messaggio
            cipher_text = read_file(sys.argv[3])
            key = sys.argv[7]
            keystream = otp_string_generator(key=key, length=len(cipher_text))

            # Salvataggio del file per il testo in chiaro
            plain_text = otp_decryption(cipher_text=cipher_text, keystream=keystream)
            save_file(path=f"./{sys.argv[5]}", value=plain_text)
            print("Decifratura completata correttamente, file disponibile in questa directory.")
        
        else:
            print("Composizione del comando errata, riprovare o consulta il README per l'uso.")

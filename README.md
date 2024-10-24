
# One-Time Pad (OTP) Encryption/Decryption Tool 🔐💻

Questo progetto è un'implementazione di un semplice algoritmo di cifratura **One-Time Pad (OTP)**, scritto in **Python**. L'OTP è un metodo di cifratura crittograficamente sicuro, dove una chiave casuale della stessa lunghezza del messaggio viene utilizzata una sola volta per cifrare e decifrare un messaggio. Il programma supporta la lettura da file, la generazione di keystream casuali, la cifratura e la decifratura di messaggi.

## 🏁 Come iniziare

Segui questi passaggi per eseguire il progetto localmente:

### 1. Clona il repository

Scarica il progetto localmente eseguendo il seguente comando:

```bash
git clone https://github.com/gioele-ferrari/otp-encryption-tool.git
```

### 2. Accedi alla cartella del progetto

Passa alla cartella del progetto appena scaricata:

```bash
cd otp-encryption-tool
```

### 3. Esegui il programma

Puoi cifrare o decifrare i file utilizzando i comandi spiegati di seguito.

## 🎮 Come funziona

Il programma può cifrare e decifrare file di testo utilizzando un keystream generato casualmente per la cifratura. Ecco come utilizzare il programma:

### 1. **Cifratura**

Per cifrare un file di input, usa il seguente comando:

```bash
py main.py -c -in <input_file> -out <output_cipher_file>
```

- `<input_file>`: Il file di testo che vuoi cifrare.
- `<output_cipher_file>`: Il file in cui vuoi salvare il testo cifrato.

Esempio:

```bash
py main.py -c -in message.txt -out cipher.txt
```

Questo comando genererà due file:

- Un file cifrato (es. `cipher.txt`).
- Un keystream salvato come `keystream` che sarà necessario per la decifratura.

### 2. **Decifratura**

Per decifrare un file cifrato, usa il seguente comando:

```bash
py main.py -d -in <input_cipher_file> -out <output_plaintext_file> -key <keystream_file>
```

- `<input_cipher_file>`: Il file cifrato che desideri decifrare.
- `<output_plaintext_file>`: Il file in cui vuoi salvare il messaggio decifrato.
- `<keystream_file>`: Il file contenente il keystream generato durante la cifratura.

Esempio:

```bash
py main.py -d -in cipher.txt -out decrypted_message.txt -key keystream
```

### Limitazioni

- La chiave generata (keystream) deve essere usata una sola volta per ogni messaggio, come suggerisce la teoria del One-Time Pad. Riutilizzare una chiave comprometterebbe la sicurezza del messaggio.
- La lunghezza della chiave deve essere pari alla lunghezza del messaggio da cifrare.

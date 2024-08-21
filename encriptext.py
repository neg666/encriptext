import subprocess
import sys

def install_libraries():
    try:
        import cryptography
    except ImportError:
        print("Instalando librerías necesarias...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
        print("Librerías instaladas correctamente.")

        # Intentar importar nuevamente después de la instalación
        global Fernet
        from cryptography.fernet import Fernet

install_libraries()

# Después de la instalación, se puede importar normalmente
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key():
    return generate_key()

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text.decode()  # Convertir bytes a string

def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    try:
        decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()  # Convertir string a bytes y luego decodificar
        return decrypted_text
    except Exception as e:
        return f"Error en la desencriptación: {e}"

def print_large_x():
    x_art = """
x       x
 x     x 
  x   x  
   x x   
    x    
   x x   
  x   x  
 x     x 
x       x
"""
    print(x_art)

def main_menu():
    key = load_key()
    
    while True:
        print_large_x()
        print("\n--- Menú de Encriptación con AES ---")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            text = input("Ingrese el texto a encriptar: ")
            encrypted_text = encrypt_text(text, key)
            print(f"Texto encriptado: {encrypted_text}")

        elif choice == "2":
            encrypted_text = input("Ingrese el texto encriptado: ")
            decrypted_text = decrypt_text(encrypted_text, key)
            print(f"Texto desencriptado: {decrypted_text}")

        elif choice == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main_menu()

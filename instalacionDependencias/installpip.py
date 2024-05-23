import subprocess
import sys

def install_pip():
    try:
        import pip
        print("pip ya está instalado")
    except ImportError:
        print("pip no está instalado. Procediendo a instalar pip.")
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("pip instalado y actualizado exitosamente.")

if __name__ == "__main__":
    install_pip()
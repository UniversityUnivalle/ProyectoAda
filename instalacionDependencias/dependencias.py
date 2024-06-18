import subprocess
import sys

def Install_pip():
    try:
        import pip
    except ImportError:
        print("pip no está instalado. Procediendo a instalar pip.")
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("pip instalado y actualizado exitosamente.")

def Install_Dependencies():
    Install_pip()
    try:
        import matplotlib
        import tabulate
        import networkx
    except ImportError:
        import pip
        pip.main(["install", "matplotlib"])
        pip.main(["install", "tabulate"])
        pip.main(["install", "networkx"])
    
    print("Dependencias Instaladas correctamente...")
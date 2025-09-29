import sys
import os

def GetNTKey():
    """
    On récupère la touche pressé pour les os Windows
    """
    
    import msvcrt
    if msvcrt.kbhit():
        return msvcrt.getch().decode()
    return None

def GetPosixKey():
    """
    On recupère la touche de clavier pressé fonctionne pour les os mac et linux
    """
    import tty, termios, select

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None
def ERRORKEY():
    raise Exception("Votre Os n'est pas compatible")

if os.name == "nt":
    GetKey = GetNTKey
elif os.name == "posix":
    GetKey = GetPosixKey
else:
    GetKey = ERRORKEY


print("Appuie sur une touche (q pour quitter) :")
while True:
    key = GetKey()
    if key:
        print(f"Touche pressée : {key}")
        if key.lower() == 'q':
            break
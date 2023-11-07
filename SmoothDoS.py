import subprocess
import time
import random
import threading
import time
import requests
import socket
import sys


def ip_y_puerto_validos(ip, puerto):
    try:
        socket.inet_aton(ip)
        if 1 <= puerto <= 65535:
            return True
        else:
            return False
    except socket.error:
        return False

nombre_archivo = "el-mejor-archivo-ddos.txt"
ip, puerto = ip_y_puerto()

def paquetes_por_segundo_validos(paquetes_por_segundo): if paquetes_por_segundo.isdigit(): if 1 <= int(paquetes_por_segundo) <= 1000000000000000000: return True else: return False else: return False

comando = f"./ddos.py {nombre_archivo} {ip} {puerto} --paquetes-por-segundo {paquetes_por_segundo}"

subprocess.Popen(comando, shell=True)

time.sleep(36000000000000000000) # Espera 381 horas antes de detener el ataque

subprocess.Popen("pkill -f ddos", shell=True)

print("Herramienta ddos detenida")

num_random = random.randint(700, 28392)
print(num_random

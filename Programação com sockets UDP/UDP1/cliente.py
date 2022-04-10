

import socket #socket lib
import threading #thread lib
import sys #lib para processos e sistema
import hashlib #lib para hash

def receive(socket, signal):    #recebe mensagens do servidor
    while signal: #enquanto o cliente estiver conectado
        try: #tenta receber mensagem
            data = socket.recv(1024) #recebe mensagem
            print(str(data.decode("utf-8"))) #imprime mensagem
            response = data.decode("utf-8") 
            # if response[:-1] == "ERROR": #se a mensagem for de erro
            #     signal = False #desconecta o cliente
            #     socket.close() #fecha conexao
            #     sys.exit(0) #sai do programa

        except:
            print("You have been disconnected from the server")
            signal = False
            break

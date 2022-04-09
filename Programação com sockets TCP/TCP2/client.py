'''
    # Descrição: Questão 2) Faça uma aplicação com um servidor que gerencia um conjunto de arquivos remotos entre múltiplos
usuários. O servidor deve responder aos seguintes comandos:

    # Mensagens de solicitação:
    -> ADDFILE <nome arquivo> (1): adiciona um arquivo novo.
    -> DELETE  <nome arquivo> (2): remove um arquivo existente.
    -> GETFILESLIST (3): retorna uma lista com o nome dos arquivos.
    -> GETFILE  <nome arquivo>  (4): faz download de um arquivo.



    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 05/04/2022
    # Data de modificação: 08/04/2022
'''

import socket #socket lib
import threading #thread lib
import sys #lib para processos e sistema
import os #lib para hash

def receive(socket, signal):    #recebe mensagens do servidor
    while signal: #enquanto o cliente estiver conectado
        try: #tenta receber mensagem
            res = socket.recv(3) #recebe mensagem
            

            if int(res[2]) == 1:
                print("SUCCESS")
                if int(res[1]) == 3:
                    numberFiles = int.from_bytes(socket.recv(2), 'big') #recebe numero de arquivos
                    for _ in range(numberFiles):
                        # Recebe o tamanho do arquivo em bigendian
                        filenameSize = int.from_bytes(socket.recv(1), 'big')
                        # Recebe o nome do arquivo
                        print(socket.recv(filenameSize).decode()) #decodifica o nome do arquivo
                elif int(res[1]) == 4:
                    fileName = socket.recv(255).decode('utf-8') #recebe nome do arquivo
                    fileSize = int.from_bytes(socket.recv(4), byteorder='big') #recebe o tamanho do arquivo em bigendian

                    arq = b'' #cria um buffer
                    arq = socket.recv(fileSize) #recebe o arquivo
                    # Recebe o arquivo
                    with open('./files/' + fileName, 'wb') as file: #cria um arquivo com o nome do arquivo recebido
                        file.write(arq) #escreve o arquivo no arquivo criado

            elif int(res[2]) == 2:
                print("ERROR")
        
        except:
            print("You have been disconnected from the server")
            signal = False
            break

def operation(opcao):
    opcoes = {
        "ADDFILE": 1,   
        "DELETE": 2,
        "GETFILESLIST": 3,   
        "GETFILE": 4,
    }
    return opcoes.get(opcao, 0)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket
    sock.connect(('localhost', 3333)) #conecta ao servidor
    isConnected = False
except:
    print("Não foi possível se conectar ao servidor")
    input("Pressione ENTER para sair")
    sys.exit(0)

receiveThread = threading.Thread(target = receive, args = (sock, True)) #cria thread para receber mensagens
receiveThread.start() #inicia thread

while True:
    message = input("~") #recebe mensagem do cliente
    if message != "":
        sendHeader = bytearray(3)
        sendHeader[0] = 1 #envio
        operacao = message.split(' ')[0] #pega a operacao
        sendHeader[1] = operation(operacao) #tipo de operacao
        if sendHeader[1] == 3:
            sendHeader[2] = len(" ")
            sock.send(sendHeader + bytearray(" ".encode()))
        elif sendHeader[1] == 0:
            print("Operação inválida")

        else:
            if len(message.split(' ')) <= 1:
                print("digite o nome do arquivo!")
            else:
                nomeArquivo = message.split(' ')[1] #pega o nome do arquivo
                sendHeader[2] = len(nomeArquivo) #tamanho do nome do arquivo
                if sendHeader[2] < 255:
                    sock.send(sendHeader + bytearray(nomeArquivo.encode())) 
                    if sendHeader[1] == 1:
                        arquivos = os.listdir('./files') #lista os arquivos
                        if nomeArquivo in arquivos: #verifica se o arquivo existe
                            tamArquivo = (os.stat('./files/' + nomeArquivo).st_size).to_bytes(4, "big")  #tamanho do arquivo
                            sock.send(tamArquivo) #envia o tamanho do arquivo
                            arquivo = open('./files/' + nomeArquivo, 'rb') #abre o arquivo
                            arquivo = arquivo.read() #le o arquivo
                            sock.send(arquivo) #envia o arquivo
            
'''
    # Descrição: Questão 1) - Faça um servidor para processar as seguintes mensagens dos clientes. O servidor deve suportar mensagens
    de múltiplos clientes. Use o TCP. As mensagens de solicitação estão no formato String UTF

    # Login
    Inserir login e senha para acesso o servidor. Enviado com flag CONNECT login,password.

    # Mensagens de solicitação:
    #    PWD: path atual
    #    CHDIR <path>: mudar para o diretório <path>
    #    GETDIRS: listar diretórios
    #    GETFILES: listar arquivos
    #    EXIT: Finalizar conexao

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 02/04/2022
    # Data de modificação: 06/04/2022
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
                    numberFiles = int.from_bytes(socket.recv(2), 'big')
                    for _ in range(numberFiles):
                        # Recebe o tamanho do arquivo em bigendian
                        filenameSize = int.from_bytes(socket.recv(1), 'big')
                        # Recebe o nome do arquivo
                        print(socket.recv(filenameSize).decode())
                elif int(res[1]) == 4:
                    filenameSize = int.from_bytes(socket.recv(1), 'big')
                    # Recebe o nome do arquivo
                    print(socket.recv(filenameSize).decode())
                    # Recebe o tamanho do arquivo em bigendian
                    fileSize = int.from_bytes(socket.recv(4), 'big')
                    # Recebe o arquivo
                    with open(socket.recv(filenameSize).decode(), 'wb') as file:
                        file.write(socket.recv(fileSize))
            else:
                print("ERROR")
        
        except:
            print("You have been disconnected from the server")
            signal = False
            break

def operation(opcao):
    opcoes = {
        "ADDFILE": 1,
        "DELETE": 2,
        "GETFILELIST": 3,
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
    sendHeader = bytearray(3)
    sendHeader[0] = 1 #envio
    operacao = message.split(' ')[0] #pega a operacao
    nomeArquivo = message.split(' ')[1] #pega o nome do arquivo
    sendHeader[1] = operation(operacao) #tipo de operacao
    sendHeader[2] = len(nomeArquivo) #tamanho do nome do arquivo
    print(nomeArquivo)
    print(sendHeader[1], sendHeader[2])

    if sendHeader[1] != 3 and sendHeader[2] < 255:
        socket.send(sendHeader + bytearray(nomeArquivo.encode())) 

        if sendHeader[1] == 1:
            arquivos = os.listdir('./files')
            if nomeArquivo in arquivos:
                tamArquivo = (os.stat('./files/' + nomeArquivo).st_size).to_bytes(4, "big") 
                socket.send(tamArquivo)
                arquivo = open('./files/' + nomeArquivo, 'rb')
                arquivo = arquivo.read()
                socket.send(arquivo)
                arquivo.close()
  
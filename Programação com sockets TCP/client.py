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
import hashlib #lib para hash
isConnected = False #variavel para verificar se o cliente esta conectado

def receive(socket, signal):    #recebe mensagens do servidor
    while signal: #enquanto o cliente estiver conectado
        try: #tenta receber mensagem
            data = socket.recv(1024) #recebe mensagem
            print(str(data.decode("utf-8"))) #imprime mensagem
            response = data.decode("utf-8") 
            if response[:-1] == "ERROR": #se a mensagem for de erro
                signal = False #desconecta o cliente
                socket.close() #fecha conexao
                sys.exit(0) #sai do programa

        except:
            print("You have been disconnected from the server")
            signal = False
            break


#registra login e senha
login = input("Login: ")
senha = input("Senha: ")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket
    sock.connect(('localhost', 3333)) #conecta ao servidor
    senhaCriptografada = hashlib.sha512(senha.encode('utf-8')).hexdigest() #criptografa a senha
    print(senhaCriptografada)
    sock.send(('CONNECT '+ str(login) + ',' + str(senhaCriptografada)).encode("utf-8")) #envia mensagem de login

except:
    print("Não foi possível se conectar ao servidor")
    input("Pressione ENTER para sair")
    sys.exit(0)

receiveThread = threading.Thread(target = receive, args = (sock, True)) #cria thread para receber mensagens
receiveThread.start() #inicia thread

while True:
    message = input("~") #recebe mensagem do cliente
    sock.sendall(str.encode(message)) #envia mensagem para o servidor
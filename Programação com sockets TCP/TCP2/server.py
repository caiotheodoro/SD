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


    # Usuários para teste: caio,teste ;  gustavo;teste4  ; campiolo;so
    #

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 02/04/2022
    # Data de modificação: 06/04/2022
'''

import socket
import threading 
import os #lib para processos e sistema
 
connections = [] #lista de conexoes
total_connections = 0 #numero de conexoes

class Client(threading.Thread): 
    def __init__(self, socket, address, id, name, signal): 
        threading.Thread.__init__(self)  #chama o construtor da classe Thread
        self.socket = socket 
        self.address = address
        self.id = id
        self.user = ''
        self.name = name
        self.isConnected = False
        self.signal = signal
    
    def __str__(self): #retorna o nome do cliente
        return str(self.id) + " " + str(self.address) 
    
  
    def verifyLogin(self, data):  #verifica se o usuario existe
      login = data.split(',')[0]
      senha = data.split(',')[1]
      try:
        with open('accounts.txt', 'r') as file: 
          for line in file: 
            if login in line.split(',')[0]:
              #compare hashes
              if senha == line.split(',')[1][:-1]:
                self.user = login
                return True
      except:
        print("Error reading accounts.txt")
        return False

    def run(self):
        while self.signal: #enquanto o cliente estiver conectado
            try: #tenta receber mensagem
                data = self.socket.recv(1024)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data != "": #se a mensagem nao for vazia

              data = data.decode("utf-8") #decodifica a mensagem
              operation = data.split(' ')[0] #separa a operacao da mensagem
              if not self.isConnected and operation == "CONNECT":
                data = data.split(' ')[1] #login;senha
                if self.verifyLogin(data): #verifica se o usuario existe
                  print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - Success") #log de operacao
                  self.socket.send("SUCCESS\n".encode("utf-8")) 
                  self.isConnected = True
                else:
                  print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - Failed") #log de operacao
                  self.socket.send("ERROR\n".encode("utf-8"))
                  
              
              elif operation == 1:  #se a operacao for PWD

                print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - " )#log de operacao
                self.socket.send(( ).encode("utf-8")) #envia mensagem para o cliente
            

              elif operation == 2: #se a operacao for CHDIR
                  data = data.split(' ')[1] #caminho
                  if os.path.isdir(data): #se o caminho existir
                    os.chdir(data) #muda o caminho
                    print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - Success") #log de operacao
                    self.socket.send("SUCCESS\n".encode("utf-8"))
                  else:
                    print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - Failed") #log de operacao
                    self.socket.send("ERROR\n".encode("utf-8"))
              elif operation == 3:

                print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - " )
              
              elif operation == 4:

                print("ID " + str(self.user) + ": Request - " + str(operation) + "-  Response - " )

                
              else:
                self.socket.send(("Comando inválido.").encode("utf-8")) 

def newConnections(socket):  #cria novas conexoes
    while True:
        sock, address = socket.accept() #aceita conexao
        global total_connections #globaliza o numero de conexoes
        connections.append(Client(sock, address, total_connections, "Name", True)) #adiciona o cliente na lista de conexoes
        connections[len(connections) - 1].start() #inicia o cliente
        print("New connection at ID " + str(connections[len(connections) - 1])) #log de nova conexao
        total_connections += 1

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket do tipo TCP
    sock.bind(('localhost', 3333)) #define o ip e a porta do socket
    sock.listen(5) #escuta por conexoes

    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,)) #cria uma nova thread para criar novas conexoes
    newConnectionsThread.start() #inicia a thread
    
main() #inicia o programa
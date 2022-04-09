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

import socket
import threading 
import os #lib para processos e sistema
import logging
 

connections = [] #lista de conexoes
total_connections = 0 #numero de conexoes

FORMAT = '%(asctime)-5s %(clientip)s %(user)s %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
logger = logging.getLogger('tcpserver')

class Client(threading.Thread): 
    def __init__(self, socket, address, id, name, signal): 
        threading.Thread.__init__(self)  #chama o construtor da classe Thread
        self.socket = socket 
        self.address = address
        self.id = id
        self.user = ''
        self.d = {'clientip': address[0], 'user': address[1]}
        self.name = name
        self.signal = signal
    
    def __str__(self): #retorna o nome do cliente
        return str(self.id) + " " + str(self.address) 
    
  

    def run(self):
        while self.signal: #enquanto o cliente estiver conectado
            try: #tenta receber mensagem
                rcvHeader = bytearray(3)
                rcvHeader[0] = 2
                data = bytearray(self.socket.recv(512))
                
            except:
                logger.info("Client %s", "has disconnected", extra=self.d)
                self.signal = False
                connections.remove(self)
                break
            if data != "": #se a mensagem nao for vazia
              operacao = int(data[1])
              nomeArquivo = data[3:].decode('utf-8')
              
              if operacao == 1: #adicionar arquivo
                logger.info('Protocolo: %s', 'Requisição ADDFILE:', extra=self.d)
                rcvHeader[1] = 1
                tamanhoArquivo = int.from_bytes(self.socket.recv(4), byteorder='big')
                logger.info('Protocolo: %s', 'ENVIADO Tamanho do arquivo', extra=self.d)
                arquivo = b''

                arquivo = self.socket.recv(tamanhoArquivo)
                logger.info('Protocolo: %s', 'ENVIADO Arquivo', extra=self.d)

                with open('./server/' + nomeArquivo, 'w+b') as file:
                  file.write(arquivo)
                arquivos = os.listdir(path='./server/')

                if nomeArquivo in arquivos:
                  rcvHeader[2] = 1 #sucesso
                  logger.info('Protocolo: %s', 'REQUISIÇÃO SUCCESS', extra=self.d)
                else:
                  rcvHeader[2] = 2 #erro
                  logger.info('Protocolo: %s', 'REQUISIÇÃO ERROR', extra=self.d)
                self.socket.send(rcvHeader)

              elif operacao == 2: #remover arquivo
                logger.info('Protocolo: %s', 'Requisição DELETE:', extra=self.d)
                rcvHeader[1] = 2
                if(os.path.isfile('./server/' + nomeArquivo)):
                # Tenta remover o arquivo
                  os.remove('./server/' + nomeArquivo)
                  rcvHeader[2] = 1
                  logger.info('Protocolo: %s', 'REQUISIÇÃO SUCCESS', extra=self.d)
                else:
                  rcvHeader[2] = 2
                  logger.info('Protocolo: %s', 'REQUISIÇÃO ERROR', extra=self.d)

                self.socket.send(rcvHeader)
                logger.info('Protocolo: %s', 'RESPOSTA ENVIADA', extra=self.d)
              

              elif operacao == 3: #listar arquivos
                logger.info('Protocolo: %s', 'Requisição GETFILESLIST:', extra=self.d)
                rcvHeader[1] = 3
                arquivos = os.listdir(path='./server/')
                listaArquivos = []
                if len(arquivos) < 0:
                  rcvHeader[2] = 2
                  self.socket.send(rcvHeader)
                  logger.info('Protocolo: %s', 'REQUISIÇÃO ERROR: Não há arquivos no servidor', extra=self.d)

                else:
                  rcvHeader[2] = 1
                  self.socket.send(rcvHeader)
                  logger.info('Protocolo: %s', 'REQUISIÇÃO SUCCESS ', extra=self.d)

                  for arquivo in arquivos:
                    listaArquivos.append(str(arquivo))

                  self.socket.send(len(listaArquivos).to_bytes(2, byteorder='big'))
                  logger.info('Protocolo: %s', 'Enviando lista de arquivos:', extra=self.d)



                  for arquivo in listaArquivos:
                    tamNome = len(arquivo)
                    self.socket.send(tamNome.to_bytes(1, byteorder='big'))
                    self.socket.send(arquivo.encode('utf-8'))
                  logger.info('Protocolo: %s', 'Enviando lista de arquivos:', extra=self.d)

              elif operacao == 4: 
                logger.info('Protocolo: %s', 'Requisição GETFILE:', extra=self.d)
                rcvHeader[1] = 4
                arquivos = os.listdir(path='./server/') #lista de arquivos
              
                if nomeArquivo in arquivos and len(nomeArquivo) < 255:
                  rcvHeader[2] = 1 #sucesso
                  logger.info('Protocolo: %s', 'REQUISIÇÃO SUCCESS:', extra=self.d)
                else:
                  rcvHeader[2] = 2 #erro
                  logger.info('Protocolo: %s', 'REQUISIÇÃO ERROR:', extra=self.d)

                self.socket.send(rcvHeader) #envia o header
                logger.info('Protocolo: %s', 'Enviando HEADER', extra=self.d)

                #send filename
                self.socket.send(nomeArquivo.encode('utf-8'))
                logger.info('Protocolo: %s', 'Enviando NOME ARQUIVO', extra=self.d)

                tamArquivo = (os.stat('./server/' + nomeArquivo).st_size).to_bytes(4, "big")
                self.socket.send(tamArquivo) #envia o tamanho do arquivo
                logger.info('Protocolo: %s', 'Enviando TAMANHO ARQUIVO', extra=self.d)

                with open('./server/' + nomeArquivo, 'rb') as file:  #abre o arquivo
                  arquivo = file.read()  #le o arquivo
                  self.socket.send(arquivo) #envia o arquivo
                logger.info('Protocolo: %s', 'Enviando ARQUIVO', extra=self.d)
                  
                  

              else:
                self.socket.send(("Comando inválido.").encode("utf-8")) 
                logger.info('Protocolo: %s', 'Comando inválido', extra=self.d)

def newConnections(socket):  #cria novas conexoes
    while True:
        sock, address = socket.accept() #aceita conexao
        global total_connections #globaliza o numero de conexoes
        connections.append(Client(sock, address, total_connections, "Name", True)) #adiciona o cliente na lista de conexoes
        connections[len(connections) - 1].start() #inicia o cliente
        d = {'clientip': address[0], 'user': address[1]}
        logger.info('Protocol info: %s', 'connection established', extra=d)
        total_connections += 1

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket do tipo TCP
    sock.bind(('localhost', 3333)) #define o ip e a porta do socket
    sock.listen(5) #escuta por conexoes

    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,)) #cria uma nova thread para criar novas conexoes
    newConnectionsThread.start() #inicia a thread
    
main() #inicia o programa
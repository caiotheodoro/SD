'''
    # Descrição: Questão 2)  Fazer um sistema de upload de arquivos via UDP. Um servidor UDP deverá receber as partes dos arquivos
(1024 bytes), verificar ao final a integridade via um checksum (SHA-1) e armazenar o arquivo em uma pasta padrão.
Sugestões: o servidor pode receber o nome e tamanho do arquivo como o primeiro pacote e o checksum como o último.
Testar o servidor com arquivos textos e binários (ex: imagens, pdf) de tamanhos arbitrários (ex: 100 bytes, 4KiB,
4MiB). O protocolo para a comunicação deve ser criado e especificado textualmente ou graficamente.

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 15/04/2022
    # Data de modificação: 18/04/2022
'''



import hashlib
import logging
import math
import os
import socket

FORMAT = '%(asctime)-5s %(clientip)s %(user)s %(message)s' # Formato da mensagem
logging.basicConfig(format=FORMAT,level=logging.INFO) # Configuração do log
logger = logging.getLogger('udpserver') # Logger

class Client():
    def __init__(self, socket, address): 
        self.socket = socket # Socket
        self.address = address # Endereço
    def main(self):
        while True:
            req, addr = self.socket.recvfrom(1024) # Recebe a mensagem
            d = {'clientip': addr[0], 'user': addr[1]} # Dicionário
            tamArq = int.from_bytes(req[:4], byteorder='big') # Tamanho do arquivo
            nomeArq = req[4:].decode() # Nome do arquivo
            logger.info('Protocolo: %s', 'REQUISIÇÃO RECEBIDA', extra=d) # Log
            pacotes = math.ceil(tamArq/1024) # Quantidade de pacotes
            file = open('./server/' + nomeArq, 'w+b') # Cria o arquivo
            while pacotes > 0: # Enquanto houver pacotes
                data, addr = self.socket.recvfrom(1024) # Recebe o pacote
                file.write(data) # Escreve no arquivo
                pacotes -= 1  # Decrementa o número de pacotes
            file.seek(0)    # Posiciona o cursor no início do arquivo
            checksumHash = hashlib.sha1(file.read()).hexdigest()  # Calcula o checksum
            checksumcli, addr = self.socket.recvfrom(1024)  # Recebe o checksum
            if checksumcli.decode() == checksumHash: # Se o checksum for igual
                logger.info('Protocolo: %s', 'REQUISIÇÃO SUCCESS', extra=d) # Log
            else: # Se não
                os.remove('./server/' + nomeArq) # Remove o arquivo
                logger.info('Protocolo: %s', 'REQUISIÇÃO FAIL', extra=d) # Log
            file.close() # Fecha o arquivo

if __name__ == '__main__': # Se for o main
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria o socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)   # Permite o reuso do endereço
    s.bind(("127.0.0.1", 5973)) # Binda o socket
    Client(s, ("127.0.0.1", 5973)).main() # Inicia o cliente
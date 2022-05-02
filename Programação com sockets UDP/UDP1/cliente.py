'''
    # Descrição: Fazer um chat P2P que possibilite os clientes trocarem mensagens entre si. 
As mensagens possuem o formato: 
- tipo de mensagem [1 byte]
- tamanho apelido (tam_apl) [1 byte]
- apelido [tam_apl (1 a 64) bytes ] 
- tamanho mensagem (tam_msg) [1 byte]
- mensagem [tam_msg bytes] [0-255 byte]


- tipo de mensagem:
    1: mensagem normal
    2: emoji
    3: URL
    4: ECHO (envia e recebe a mesma mensagem para indicar que usuário está ativo

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 17/04/2022
    # Data de modificação: 19/04/2022
'''

from emojis import emojis
from threading import Thread
import sys
import socket

ip = "127.0.0.1"
address = [5761, 5762]



def receptor(player, adr):
    s.bind((ip, int(adr))) # binda o socket ao ip e a porta
    while True: 
        msg, addr = s.recvfrom(322) # recebe uma mensagem no tamanho maximo que a mensagem pode ser enviada 1+1+1+64+255=322
        tipo = int(msg[0]) # pega o tipo da mensagem
        tamPlayer = int(msg[1]) # pega o tamanho do player
        player = msg[2:2+tamPlayer].decode("utf-8") # pega o player
        tamMsg = int(msg[tamPlayer+2]) # pega o tamanho da mensagem
        msg = msg[tamPlayer+3:tamPlayer+3+tamMsg].decode("utf-8") # pega a mensagem

        if tipo == 4: # se for um echo
            msg = (1).to_bytes(1, byteorder="big") + tamPlayer.to_bytes(1, byteorder="big") + player.encode("utf-8") + tamMsg.to_bytes(1, byteorder="big") + msg.encode("utf-8") # cria a mensagem
            print(f"{player} realizou echo") # imprime o echo
            s.sendto(msg, addr) # envia a mensagem para o cliente
        elif tipo == 1: # se for uma mensagem
            print(f"{player}: {msg}") # imprime a mensagem
        elif tipo == 2: # se for um emoji
            print(f"{player}  emoji: {msg}") # imprime o emoji
        elif tipo == 3: # se for uma url
            print(f"{player}  link: {msg}") # imprime o link



def enviador(player, adr):
    while True: 
        msg = input("~ ") # recebe uma mensagem
        tipo = 1 # tipo da mensagem
        tamMsg = len(msg.encode("utf-8")) # tamanho da mensagem
        tamPlayer = len(player.encode("utf-8")) # tamanho do player
        if len(msg.encode("utf-8")) > 254: # se a mensagem for maior que 254
            print("Mensagem muito grande") # imprime mensagem
            continue # volta para o inicio do loop
        else:        # se não
            if msg in emojis: # se a mensagem for um emoji
                tipo = 2
            if msg.encode("utf-8").find(b'http')  != -1: # se a mensagem for uma url
                tipo = 3
            if msg.encode("utf-8").find(b'echo') != -1: # se a mensagem for um echo
                tipo = 4
            msg = (tipo).to_bytes(1, byteorder="big") + tamPlayer.to_bytes(1, byteorder="big") + player.encode("utf-8") + tamMsg.to_bytes(1, byteorder="big") + msg.encode("utf-8") # cria a mensagem
          #  s.send(msg.encode())
            s.sendto(msg, (ip, adr))    # envia a mensagem para o cliente

# def server():
#     global sock
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((ip, address[2]))
#     while True:
#         msg, addr = sock.recvfrom(1024)

if __name__ == '__main__':
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #  s.connect((socket.gethostname(), 3000))
    
    try:
        idx = sys.argv[1]
        
        player = input('Qual o seu nick? ')

        if len(player.encode()) > 64 or len(player.encode()) < 1: # se o player for maior que 64 ou menor que 1
            print('Nome inválido')
            sys.exit()

    #    s.send(player.encode())
       # while True:
        if idx == '1':  
            Thread(target=enviador, args=(player,address[0])).start() # inicia o enviador
            Thread(target=receptor, args=(player,address[1])).start() # inicia o receptor
            # Thread(target=server).start()
        if idx == '2':
            Thread(target=enviador, args=(player,address[1])).start() # inicia o enviador
            Thread(target=receptor, args=(player,address[0])).start() # inicia o receptor
            # Thread(target=server).start()
   
    except:
        print('Erro ao conectar ao servidor')

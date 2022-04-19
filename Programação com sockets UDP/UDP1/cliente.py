import threading
from threading import Thread
import sys
import socket




ip = "127.0.0.1"
address = [5761, 5762, 5763]


def receptor(player, address):
    s.bind((ip, address))
    while True:
        msg, addr = s.recvfrom(1024)
        tipo = int(msg[0])
        tamPlayer = int(msg[1])
        player = msg[2:2+tamPlayer].decode("utf-8")
        tamMsg = int(msg[tamPlayer+2])
        msgPos = tamPlayer+3
        msg = msg[msgPos:msgPos+tamMsg].decode("utf-8")

        if tipo == 4:
            msg = (1).to_bytes(1, byteorder="big") + tamPlayer.to_bytes(1, byteorder="big") + player.encode("utf-8") + tamMsg.to_bytes(1, byteorder="big") + msg.encode("utf-8")
            s.sendto(msg, (ip, address))
        else:
            print(f"{player}: {msg}")
        



def enviador(player, address):
    tipo = 1
    while True:
        msg = input("~ ")
        tamMsg = len(msg.encode("utf-8"))
        tamPlayer = len(player.encode("utf-8"))
        if len(msg.encode("utf-8")) > 254:
            print("Mensagem muito grande")
            continue
        else:  
            if msg.encode("utf-8").find(b'\xF0\x9F\x98\x81') != -1:
                tipo = 2
            if msg.encode("utf-8").find(b'http') != -1:
                tipo = 3
            if msg.encode("utf-8").find(b'echo') != -1:
                tipo = 4
            msg = (tipo).to_bytes(1, byteorder="big") + tamPlayer.to_bytes(1, byteorder="big") + player.encode("utf-8") + tamMsg.to_bytes(1, byteorder="big") + msg.encode("utf-8")
            s.send(msg.encode())
            s.sendto(msg, (ip, address))




if __name__ == '__main__':
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 3000))
    
    try:
        idx = sys.argv[1]
        
        player = input('Qual o seu nick? ')

        if len(player.encode()) > 64 or len(player.encode()) < 1:
            print('Nome inválido')
            sys.exit()

        s.send(player.encode())
       # while True:
        if idx == '1':
            threading.Thread(target=enviador, args=(player,address[0])).start()
            threading.Thread(target=receptor, args=(player,address[1])).start()
            threading.Thread(target=receptor, args=(player,address[2])).start()
        if idx == '2':
            threading.Thread(target=enviador, args=(player,address[1])).start()
            threading.Thread(target=receptor, args=(player,address[0])).start()
            threading.Thread(target=receptor, args=(player,address[2])).start()
        if idx == '3':
            threading.Thread(target=enviador, args=(player,address[2])).start()
            threading.Thread(target=receptor, args=(player,address[0])).start()
            threading.Thread(target=receptor, args=(player,address[1])).start()
        


        
    except:
        print('Erro ao conectar ao servidor')

import socket

IP_Servidor = '192.168.10.8'             

PORT = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destiny = (IP_Servidor, PORT) 

tcp.connect(destiny) 
while 1:
 msg = input()   
tcp.send(bytes(msg,"utf8"))
tcp.close()
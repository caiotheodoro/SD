import socket
MEU_IP = ''  
 # '' =  ouvira em todas as interfaces
PORT = 8000  

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = ''
MEU_SERVIDOR = (MEU_IP, PORT) 
tcp.bind(MEU_SERVIDOR)

tcp.listen(1) 

conexao, client =tcp.accept()
print ("o cliente = ", client, " se conectou")

while 1:
 msg_rcv = conexao.recv(1024)
 if msg != msg_rcv:  
  print ("recebido = ",msg_rcv," , client", client)

conexao.close()
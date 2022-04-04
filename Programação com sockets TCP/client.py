import socket
import threading
import sys
import hashlib
#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break



#Attempt connection to server
login = input("Login: ")
senha = input("Senha: ")
#senha = hashlib.sha512( str( senha ).encode("utf-8")).hexdigest()

print('L'+ str(login) + ';' + senha)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 3333))
    sock.sendall(('L'+ str(login) + ';' + str(senha)).encode("utf-8"))
    #send login senha to server
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    message = input()
    sock.sendall('M'.encode("utf-8") + str.encode(message))
import socket
import threading
import hashlib
#Variables for holding information about connections
connections = []
total_connections = 0

#Client class, new instance created for each connected client
#Each instance has the socket and address that is associated with items
#Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.user = ''
        self.name = name
        self.signal = signal
    
    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    #Attempt to get data from client
    #If unable to, assume client has disconnected and remove him from server data
    #If able to and we get data back, print it in the server and send it back to every
    #client aside from the client that has sent it
    #.decode is used to convert the byte data into a printable string
    def verifyLogin(self, data):
      #verify if data is on accounts.txt
      login = data.split(';')[0]
      senha = data.split(';')[1]
      try:
        with open('accounts.txt', 'r') as file:
          for line in file:
            if login in line.split(';')[0]:
              #compare hashes
              #if hashlib.sha512( str( line.split(';')[1] ).encode("utf-8")).hexdigest() == senha:
              if senha == line.split(';')[1][:-1]:
                self.user = login
                return True
      except:
        print("Error reading accounts.txt")
        return False

    
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data != "":
              data = data.decode("utf-8")
              if data[0] == 'M':
                
                print("ID " + str(self.user) + ": " + str(data[1:]))
                for client in connections:
                    if client.id != self.id:
                        client.socket.sendall((self.user + ":" + data[1:]).encode("utf-8"))
              elif data[0] == 'L':
                  print("entrou")
                  if self.verifyLogin(data[1:]):
                    print("ID " + str(self.user) + ": " + str(data[1:]))
                    self.socket.sendall("Server: Login successful\n".encode("utf-8"))
                  else:
                    self.socket.sendall("Server: Login failed\n".encode("utf-8"))
                    connections.remove(self)
                    self.signal = False
                    break

#Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1

def main():
    #Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 3333))
    sock.listen(5)

    #Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()
    
main()
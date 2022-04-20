# import socket
# from threading import Thread


# def dispatch(client, player): 
#     while True:
#         try:
#             message = client.recv(1024).decode()
#             print(message)
#         except:
#             clientes.remove(client) # remove cliente da lista
#             client.close() # fecha conexão
#             break # sai do loop


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 3000))
# s.listen(2)

# clientes = list()

# while True:
#     client, address = s.accept()
#     clientes.append(client)
#     player = client.recv(1024).decode()
#     print(f'{player} conectou.  {address}')
#     Thread(target=dispatch, args=(client, player)).start()
# client.close()
'''
    Questão 1 - UDP CLIENT 
    Autor:Gustavo Kioshi Asato | Caio Theodoro da Silva
    Data de criação: 18/04/2022
    Descrição: O programa é um chat P2P, no qual 2 clientes se conectam via socket e enviam mensagem entre si.
    As mensagem enviadas serão enviadas com um cabeçalho seguindo o seguinte formato:
    - tipo de mensagem [1 byte]
    - tamanho apelido (tam_apl) [1 byte]
    - apelido [tam_apl (1 a 64) bytes ] 
    - tamanho mensagem (tam_msg) [1 byte]
    - mensagem [tam_msg bytes]
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |   Tipo de mensagem   |  Tamanho apelido  |  apelido   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |        tamanho mensagem      |        mensagem        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''






import re
import socket
import sys
import threading


ip = "127.0.0.1"
porta = [1234, 4323,3233]

#Cria um socket do tipo UCP os parametros AF_INET e SOCK_DGRAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Função para verificar se uma mensagem é uma url
def verificaURL(url):
    #Regex para verificar se a mensagem é uma url 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.match(regex, url)#retorna a url


#Função para receber mensagens
def mensagemRecebe(ip, port):
    # Socket cliente
    print((ip, port))
    socketClient.bind((ip, int(port)))
    while True:
        try:
            # Recebe a mensagem para a variáveis mensage, ipAddress 
            # 332 é o tamanho total que a mensagem possui
            mensagem, ipAddress = socketClient.recvfrom(322)
            print('')
            # Atribui o tipo de mensagem para
            mensagemTipo = int(mensagem[0])
            # Atribui o tamanho do nome para a variável nomeTamanho
            nomeTamanho = int(mensagem[1])
            # Atribui o nick do cliente para a variável nick
            nome = mensagem[2:nomeTamanho+2].decode()
            # Atribui o tamanho da mensagem para a variável mensageTamanho
            mensagemTamanho = mensagem[nomeTamanho+2]
            mensagePosition = int(nomeTamanho + 3)
            # Atribui a mensagem para a variável mensageContent
            mensageContent = mensagem[mensagePosition : (mensagePosition + mensagemTamanho)].decode()
            # Verifica se a mensagem é do tipo ECHO
            if mensagemTipo == 4:
                # Formata a mensagem para reenviar
                mensagem = (mensagemTipo.to_bytes(1,'big') + nomeTamanho.to_bytes(1,'big') + nome.encode() + mensagemTamanho.to_bytes(1,'big') + mensageContent.encode())
                # Envia a mensagem
                socketClient.sendto(mensagem, ipAddress)
                # Não ficar no loop do ECHO
                mensagemTipo =1
            # Verifica se a mensagem é uma url
            elif mensagemTipo == 3:
                print(nome + ':Link:' + mensageContent)
            # Verifica se a mensagem possui emojis
            elif mensagemTipo == 2:
                 print(nome + ':Emoji:' + mensageContent)
            # Verifica se a mensagem é do tipo normal
            else:
                print(nome + ':Mensagem:' + mensageContent)
        except:
            print("")

# Função para enviar mensagens
def mensagenEnvia(ip, port):
    addr = ip, port
    while True:
        #Recebe a mensagem do cliente
        mensagem = input("")
        # Atribui o tipo de mensagem para 1
        mensagemTipo = 1
        # Atribui o tamanho da mensagem para a variável mensagemTamanho
        mensagemTamanho= len(mensagem.encode())
        # Atribui o tamanho do apelido para a variável nickSize
        nicknameSize= len(apelido.encode())
        # Verifica se a mensagem é menor do que 255 bytes
        if len(mensagem.encode()) > 255:
            print("Mensage too long")
        else:
            # Verifica se a mensagem possui emojis
            if(mensagem.find("\o/" ) == 0):
                 mensagemTipo = 2
            # Verifica se a mensagem é uma url
            elif(verificaURL(mensagem) != None):
                mensagemTipo = 3
            # Verifica se a mensagem é do tipo ECHO
            elif(mensagem.find("ECHO") == 0):
                mensagemTipo = 4
            # Formata a mensagem para enviar
            mensagem = (mensagemTipo.to_bytes(1,'big') + nicknameSize.to_bytes(1,'big') + apelido.encode() + mensagemTamanho.to_bytes(1,'big') + mensagem.encode())
            # Envia a mensagem
            socketClient.sendto(mensagem, addr)


def main():
    # recebe qual tipo de cliente que esta acessando
    idx = sys.argv[1]

    #Recebe a mensagem do cliente
    global apelido
    # Recebe o apelido do cliente
    apelido = input("Digite seu nome: ")
    try:
        # Cria um thread para receber mensagens do chat e enviar mensagens
        # Verifica se é o cliente 1
        if(idx == "1"):
            threading.Thread(target=mensagenEnvia, args=(ip, porta[0])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[1])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[2])).start()
        # Verifica se é o cliente 2
        elif(idx == "2"):
            threading.Thread(target=mensagenEnvia, args=(ip, porta[1])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[0])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[2])).start()
        # Verifica se é o cliente 3
        elif(idx == "3"):
            threading.Thread(target=mensagenEnvia, args=(ip, porta[2])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[1])).start()
            threading.Thread(target=mensagemRecebe, args=(ip, porta[0])).start()

    except:
        #Retornamos uma mensagem de erro caso não seja possível criar a thread
        print("ERRO: Erro ao criar thread!")

main()
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
import math
import os
import socket
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog


address = ("127.0.0.1", 5973) # Endereço
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria o socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)   # Permite o reuso do endereço

class NewWindow(Toplevel): # Cria uma nova janela
    def __init__(self, master): # Inicialização da janela
        Toplevel.__init__(self, master) # Inicialização da janela
        self.geometry("300x120") # Tamanho da janela
        self.title("Anexar arquivo") # Titulo da janela
        self.resizable(False, False)   # Não redimensionavel
        self.configure(background="#BEBEBE") # Cor de fundo

    def anexar(self): # Função para anexar arquivo
        origin = filedialog.askopenfilename() # Abre o arquivo
        Label(self , text=origin).grid(row=1, column=0) # Label com o nome do arquivo
        barraProg = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate') # Barra de progresso
        barraProg = Progressbar(self, orient="horizontal", length=200, mode="determinate") # Barra de progresso
        barraProg.place(x=10, y=40) # Posição da barra de progresso
        btnEnviar = Button(self, text ="📨 Enviar arquivo", bg="#ffffff", borderwidth=0) # Botão para enviar
        btnEnviar.bind("<Button>", lambda e: [self.enviar(origin, os.path.basename(origin), barraProg)]) # Envia o arquivo
        btnEnviar.place(x=40, y=80) # Posição do botão
 
    def enviar(self, arquivo, nomeArq, barraProg): # Função para enviar o arquivo
        tamArq = int.to_bytes((os.stat(arquivo).st_size), 4, 'big') # Tamanho do arquivo
        s.sendto((tamArq + nomeArq.encode('utf-8')), address) # Envia o tamanho do arquivo e o nome do arquivo
        pacotes = math.ceil(os.stat(arquivo).st_size/1024) # Quantidade de pacotes
        total = 1/(pacotes*100) # Total de pacotes
        arq = open(arquivo, 'rb') # Abre o arquivo
        checksum = hashlib.sha1(arq.read()).hexdigest() # Calcula o checksum
        arq.seek(0) # Volta para o inicio do arquivo
        progress = 0 # Inicialização do progresso
        while(pacotes > 0): # Enquanto houver pacotes
            data = arq.read(1024) # Le o arquivo
            barraProg['value'] = progress # Atualiza a barra de progresso
            progress += int(total + 1) # Incrementa o progresso
            s.sendto(data, address) # Envia o arquivo
            pacotes -= 1 # Decrementa o pacote
        barraProg['value'] = 100 # Atualiza a barra de progresso
        s.sendto(checksum.encode('utf-8'), address) # Envia o checksum
        arq.close() # Fecha o arquivo
        Label(self, text="Arquivo enviado com sucesso!").place(x=40, y=80) # Label de sucesso
def main(): # Função principal
    root = Tk() # Cria a janela
    root.title("Upload arquivo") # Titulo da janela
    root.geometry("300x120") # Tamanho da janela
    root['bg']='#6000FE' # Cor de fundo
    btn = Button(root, text ="📩 Anexar arquivo", bg="#BEBEBE", borderwidth=0) # Botão para anexar
    btn.bind("<Button>", lambda e: [NewWindow(root).anexar()]) # Anexa o arquivo
    btn.place(x=150, y=100) # Posição do botão
    btn.pack(pady = 40)     # Posição do botão
    root.mainloop() # Loop da janela

if __name__ == '__main__':  # Executa o programa
    main() 

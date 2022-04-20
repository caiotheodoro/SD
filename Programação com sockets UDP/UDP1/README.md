# Como Compilar/executar
```
python ./client.py 1 # Cliente 1
python ./client.py 2 # Cliente 2
```

# Bibliotecas usadas
from threading import Thread
import sys
import socket
```
- socket: implementação de sockets  https://docs.python.org/3/library/socket.html 
- sys:  implementação de funcionalidades de sistema operacional;processos https://docs.python.org/3/library/sys.html
- threading: implementação de threads https://docs.python.org/3/library/threading.html
```

# Exemplo de uso

```
python ./client.py 1
python ./client.py 2 
```

# Digitar os nicks no terminal
### ex: client1: caio, client2: gustavo

### client1: ~ teste

## retorno no cliente 2:      
### caio: teste


### client2: ~ :-)
### (obs:) lista de emojis está em emojis.py
## retorno no cliente 1:  gustavo emoji: :-)    

## client1:  https://www.google.com.br
### retorno no cliente 2:  caio link: https://www.google.com.br


### client2: echo "teste"
## retorno no cliente 2:  caio: echo "teste"









# Como Compilar/executar
```
python ./server.py
python ./python.py
```

# Bibliotecas usadas

```
- socket: implementação de sockets  https://docs.python.org/3/library/socket.html 
- threading: implementação de threads https://docs.python.org/3/library/threading.html
- os:  implementação de funcionalidades de  sistema operacional https://docs.python.org/3/library/os.html
- hashlib: implementação de hash https://docs.python.org/3/library/hashlib.html
- sys:  implementação de funcionalidades de sistema operacional;processos https://docs.python.org/3/library/sys.html
- logging: implementação sistema de log https://docs.python.org/3/library/logging.html
```

# Exemplo de uso

```
python ./server.py
python ./python.py
```

```
~ ADDFILE a.txt
```
### Resposta: ~SUCCESS

```
~ DELETE abc.pdf
```
### Resposta: ~SUCCESS

```
~ GETFILESLIST abc.pdf
```

### Resposta: 
### tt.txt
### a.txt

```
~ GETFILE tt.txt
```
### Resposta: ~SUCCESS




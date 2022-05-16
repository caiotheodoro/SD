#  Dependencias
```
Node e python

```
# Como Compilar/Executar
```bash
python3 ./server/server.py ( necessário utilizar pip install grpcio, google-pasta e protobuf)
Para o client, utilize o comando: npm install e depois node ./client/client.js
```

# Bibliotecas usadas
```bash
- protobuf (google.protobuf): server python  - https://pypi.org/project/protobuf/
- grpcio (google.grpc): server python  - https://pypi.org/project/grpcio/
- google-pasta  - https://pypi.org/project/google-pasta/
- grpc (node): client node  - https://www.npmjs.com/package/grpc
- request (node): client node  - https://www.npmjs.com/package/request
```

# Exemplo de uso
```bash
python3 ./server/server.py
node ./client/client.js
```


# Será aberto uma lista como a abaixo:

```
Digite o serviço requirido:
1 - Inserir Matricula
2 - Alterar notas
3 - Alterar faltas
4 - Listar alunos
5 - Listar disciplinas
6 - Sair
```

# Feito isso basta digitar o número correspondente ao serviço desejado.
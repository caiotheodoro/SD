'''
    # Descrição: #Implementar um serviço de gerenciamento de notas de uma escola.
    - Tabelas:
      - Curso
      - Disciplina   
      - Aluno
      - Matricula

    - Funções:
      - Inserir na tabela Matricula
      - Alterar notas e faltas na tabela Matricula
      - Listar alunos de uma disciplina informado a disciplina, o ano e o semestre
      - Listar disciplinas, faltas e notas informado o ano e o semestre

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 28/04/2022
    # Data de modificação: 07/05/2022
'''


import socket
import Python.Proto.matriculas_pb2 as matriculas
import Python.Proto.cursos_pb2 as cursos
import json
import Python.Proto.alunos_pb2 as alunos
import Python.Proto.disciplinas_pb2 as disciplinas
import sqlite3
s = socket.socket()       # Cria o socket
host = "127.0.0.1"
port = 20205
s.bind((host, port))     # Associa o socket ao endereço
con = sqlite3.connect('./src/database.db')   # Cria a conexão com o banco de dados
cur = con.cursor()   # Cria o cursor

s.listen(5) 
while True: 
   c, addr = s.accept()    # Aceita conexões
   print("connection from", addr)   
   data = c.recv(1024)  # Recebe os dados
   if data:    # Se houver dados
      data = data.decode() # Decodifica os dados
      output = json.loads(data)  # Converte os dados para json
      typeOperation =  output['type']  # Pega o tipo de operação
      matricula = output['matricula']  # Pega a matricula
      if typeOperation == 1:  # Se for uma operação de matriculação
         cur.execute("INSERT INTO matricula (ra, cod_disciplina, ano,semestre,nota,faltas) VALUES (?, ?, ?, ?, ?, ?)", (matricula['RA'], matricula['codDisciplina'], matricula['ano'], matricula['semestre'], 0, 0))    # Insere a matricula no banco de dados
         con.commit()   # Commita as alterações
         c.send(bytes("Matricula inserida com sucesso!", 'utf-8'))   # Envia a mensagem de sucesso
      elif typeOperation == 2:   # Se for uma operação de remoção de matriculação
         cur.execute("UPDATE matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['nota'],  matricula['RA'], matricula['codDisciplina']))  # Atualiza a matricula no banco de dados
         con.commit()   # Commita as alterações
         c.send(bytes("Notas atualizadas com sucesso!", 'utf-8'))  # Envia a mensagem de sucesso
      elif typeOperation == 3:   # Se for uma operação de atualização de notas
         cur.execute("UPDATE matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['faltas'],  matricula['RA'], matricula['codDisciplina'])) # Atualiza as faltas
         con.commit()   # Commita as alterações
         c.send(bytes("Faltas atualizadas com sucesso!", 'utf-8'))   # Envia a mensagem de sucesso
      elif typeOperation == 4:   # Se for uma operação de consulta de matriculação
         cur.execute("SELECT matricula.ra, aluno.nome, aluno.periodo, matricula.cod_disciplina  FROM matricula INNER JOIN aluno ON matricula.ra = aluno.ra WHERE matricula.cod_disciplina = ? AND matricula.ano = ? AND matricula.semestre = ?", (matricula['codDisciplina'], matricula['ano'], matricula['semestre'])) # Busca a matricula no banco de dados
         con.commit()   # Commita as alterações
         data = cur.fetchall()   # Pega todos os dados
         newData = []   # Cria uma lista para os dados
         for row in data:     # Para cada linha
            newData.append(   # Adiciona os dados na lista
               {
                  'RA': row[0],
                  'nome': row[1],
                  'periodo': row[2],
                  'codDisciplina': row[3]
               })
         if data:
            c.send(bytes(json.dumps(newData), 'utf-8'))  # Envia os dados
         else:
            c.send(bytes("Nenhuma matricula encontrada!", 'utf-8'))  # Envia a mensagem de erro
      elif typeOperation == 5:   # Se for uma operação de consulta de disciplina
         cur.execute("SELECT matricula.ra, disciplina.nome, matricula.nota, matricula.faltas FROM matricula INNER JOIN disciplina ON matricula.cod_disciplina = disciplina.codigo WHERE  matricula.ano = ? AND matricula.semestre = ?", ( matricula['ano'], matricula['semestre'])) # Busca a matricula no banco de dados
         con.commit()   # Commita as alterações
         data = cur.fetchall()   # Pega todos os dados
         newData = []   
         print(data)
         for row in data:   # Para cada linha
            newData.append(   # Adiciona os dados na lista
               {
                  'RA': row[0],
                  'nome': row[1],
                  'nota': row[2],
                  'faltas': row[3]
               })
         if data: # Se houver dados
            c.send(bytes(json.dumps(newData), 'utf-8'))  # Envia os dados
         else:
            c.send(bytes("Nenhuma matricula encontrada!", 'utf-8'))  # Envia a mensagem de erro
   c.close()   # Fecha o socket
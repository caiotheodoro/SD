import socket
import Python.Proto.matriculas_pb2 as matriculas
import Python.Proto.cursos_pb2 as cursos
import json
import Python.Proto.alunos_pb2 as alunos
import Python.Proto.disciplinas_pb2 as disciplinas
import sqlite3
s = socket.socket()      
host = "127.0.0.1"
port = 20205
s.bind((host, port))
con = sqlite3.connect('./src/database.db')
cur = con.cursor()

s.listen(5)
while True:
   c, addr = s.accept()
   print("connection from", addr)
   data = c.recv(1024)
   if data: 
      data = data.decode()
      output = json.loads(data)
      typeOperation =  output['type']
      matricula = output['matricula']
      print(typeOperation)
      if typeOperation == 1:
         cur.execute("INSERT INTO matricula (ra, cod_disciplina, ano,semestre,nota,faltas) VALUES (?, ?, ?, ?, ?, ?)", (matricula['RA'], matricula['codDisciplina'], matricula['ano'], matricula['semestre'], 0, 0))
         con.commit()
         c.send(bytes("Matricula inserida com sucesso!", 'utf-8'))
      if typeOperation == 2:
         cur.execute("UPDATE matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['nota'],  matricula['RA'], matricula['codDisciplina']))
         con.commit()
         c.send(bytes("Notas atualizadas com sucesso!", 'utf-8'))
      if typeOperation == 3:
         cur.execute("UPDATE matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['faltas'],  matricula['RA'], matricula['codDisciplina']))
         con.commit()
         c.send(bytes("Faltas atualizadas com sucesso!", 'utf-8'))
   
         #create


   c.close()
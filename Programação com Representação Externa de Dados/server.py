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
      elif typeOperation == 2:
         cur.execute("UPDATE matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['nota'],  matricula['RA'], matricula['codDisciplina']))
         con.commit()
         c.send(bytes("Notas atualizadas com sucesso!", 'utf-8'))
      elif typeOperation == 3:
         cur.execute("UPDATE matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ? ", (matricula['faltas'],  matricula['RA'], matricula['codDisciplina']))
         con.commit()
         c.send(bytes("Faltas atualizadas com sucesso!", 'utf-8'))
      elif typeOperation == 4:
         cur.execute("SELECT matricula.ra, aluno.nome, aluno.periodo, matricula.cod_disciplina  FROM matricula INNER JOIN aluno ON matricula.ra = aluno.ra WHERE matricula.cod_disciplina = ? AND matricula.ano = ? AND matricula.semestre = ?", (matricula['codDisciplina'], matricula['ano'], matricula['semestre']))
         con.commit()
         data = cur.fetchall()
         newData = []
         print(data)
         for row in data:
            newData.append(
               {
                  'RA': row[0],
                  'nome': row[1],
                  'periodo': row[2],
                  'codDisciplina': row[3]
               })
         if data:
            c.send(bytes(json.dumps(newData), 'utf-8'))
         else:
            c.send(bytes("Nenhuma matricula encontrada!", 'utf-8'))
      elif typeOperation == 5:
         cur.execute("SELECT matricula.ra, disciplina.nome, matricula.nota, matricula.faltas FROM matricula INNER JOIN disciplina ON matricula.cod_disciplina = disciplina.codigo WHERE  matricula.ano = ? AND matricula.semestre = ?", ( matricula['ano'], matricula['semestre']))
         con.commit()
         data = cur.fetchall()
         newData = []
         print(data)
         for row in data:
            newData.append(
               {
                  'RA': row[0],
                  'nome': row[1],
                  'nota': row[2],
                  'faltas': row[3]
               })
         if data:
            c.send(bytes(json.dumps(newData), 'utf-8'))
         else:
            c.send(bytes("Nenhuma matricula encontrada!", 'utf-8'))

         
         #create


   c.close()
from typing import List
import grpc
import concurrent
from concurrent import futures
import sqlite3
import rcp_pb2 as servicos
import rcp_pb2_grpc as servicos_grpc


def ListarAlunosQuery(cod_disciplina,ano,semestre):
  cur.execute("SELECT matricula.ra, aluno.nome, aluno.periodo  FROM matricula INNER JOIN aluno ON matricula.ra = aluno.ra WHERE matricula.cod_disciplina = ? AND matricula.ano = ? AND matricula.semestre = ?", (cod_disciplina,ano, semestre)) 
  rows = cur.fetchall()
  print(rows)
  return rows


def InserirAlunoQuery(ra, cod_disciplina, ano, semestre, nota, faltas):
  respose = cur.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre,nota,faltas) VALUES (?,?,?,?,?,?)", (ra, cod_disciplina, ano, semestre, nota, faltas))
  con.commit()
  print(respose)
  print('Aluno inserido com sucesso')
  return True

def AlterarNotaQuery(ra, cod_disciplina, nota):
  cur.execute("UPDATE matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ?", (nota, ra, cod_disciplina))
  con.commit()
  print('Nota alterada com sucesso')
  return True

def AlterarFaltasQuery(ra, cod_disciplina, faltas):
  cur.execute("UPDATE matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ?", (faltas, ra, cod_disciplina))
  con.commit()
  print('Faltas alterada com sucesso')
  return True


class ServicesServicer(servicos_grpc.ServicesServicer):
  

  def ListarAlunos(self, request, context):
    response = servicos.AlunosRes()
    response.message = f"Listado com sucesso!"
    data = ListarAlunosQuery(request.cod_disciplina, request.ano, request.semestre)
    for row in data:
      response.alunos.append(servicos.Aluno(RA=row[0], nome=row[1], periodo=row[2]))
    return response

  def InserirMatricula(self, request, context):
    response = servicos.InserirMatriculaRes()
    response.message = f"Matricula inserida com sucesso!"
    InserirAlunoQuery(request.RA, request.cod_disciplina, request.ano, request.semestre, request.nota, request.faltas)
    return response

  def AlterarNota(self, request, context):
    response = servicos.MessageRes()
    response.message = f"Nota alterada com sucesso!"
    AlterarNotaQuery(request.RA, request.cod_disciplina,  request.nota)
    return response

  def AlterarFaltas(self, request, context):
    response = servicos.MessageRes()
    response.message = f"Faltas alterada com sucesso!"
    AlterarFaltasQuery(request.RA, request.cod_disciplina,  request.faltas)
    return response
  




def main():
  global cur
  global con
  con = sqlite3.connect('./db.db', check_same_thread=False, isolation_level=None)   # Cria a conexão com o banco de dados
  cur = con.cursor()   # Cria o cursor  

  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  servicos_grpc.add_ServicesServicer_to_server(ServicesServicer(), server)
  print('Server Started. Listening on port 50051')
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()








main()

'''
    # Descrição: #Implementar um serviço de gerenciamento de notas de uma escola usando GRPC.
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
    # Data de criação: 08/05/2022
    # Data de modificação: 15/05/2022
'''

from typing import List
import grpc
import concurrent
from concurrent import futures
import sqlite3
import rcp_pb2 as servicos
import rcp_pb2_grpc as servicos_grpc


def ListarAlunosQuery(cod_disciplina,ano,semestre): # Função que busca os alunos na matricula
  cur.execute("SELECT matricula.ra, aluno.nome, aluno.periodo  FROM matricula INNER JOIN aluno ON matricula.ra = aluno.ra WHERE matricula.cod_disciplina = ? AND matricula.ano = ? AND matricula.semestre = ?", (cod_disciplina,ano, semestre)) 
  rows = cur.fetchall()
  return rows


def ListarDisciplinasQuery(ano,semestre): # Função que busca as disciplinas na matricula
  cur.execute("SELECT matricula.ra, disciplina.nome, matricula.nota, matricula.faltas FROM matricula INNER JOIN disciplina ON matricula.cod_disciplina = disciplina.codigo WHERE  matricula.ano = ? AND matricula.semestre = ?", (ano, semestre)) # Busca a matricula no banco de dados
  rows = cur.fetchall()
  return rows      

def InserirAlunoQuery(ra, cod_disciplina, ano, semestre, nota, faltas): # Função que insere os alunos na matricula
  respose = cur.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre,nota,faltas) VALUES (?,?,?,?,?,?)", (ra, cod_disciplina, ano, semestre, nota, faltas))
  con.commit()
  print(respose)
  print('Aluno inserido com sucesso')
  return True

def AlterarNotaQuery(ra, cod_disciplina, nota): # Função que altera a nota do aluno
  cur.execute("UPDATE matricula SET nota = ? WHERE ra = ? AND cod_disciplina = ?", (nota, ra, cod_disciplina))
  con.commit()
  print('Nota alterada com sucesso')
  return True

def AlterarFaltasQuery(ra, cod_disciplina, faltas): # Função que altera a faltas do aluno
  cur.execute("UPDATE matricula SET faltas = ? WHERE ra = ? AND cod_disciplina = ?", (faltas, ra, cod_disciplina))
  con.commit()
  print('Faltas alterada com sucesso')
  return True


class ServicesServicer(servicos_grpc.ServicesServicer): # Classe que implementa o servidor (mesma classe gerada pelo protobuf)
  

  def ListarAlunos(self, request, context): # Função que lista os alunos
    response = servicos.AlunosRes() # Resposta vinda do client
    response.message = f"Listado com sucesso!"
    data = ListarAlunosQuery(request.cod_disciplina, request.ano, request.semestre) # Busca os alunos na matricula
    for row in data:
      response.alunos.append(servicos.Aluno(RA=row[0], nome=row[1], periodo=row[2]))  # Adiciona os alunos na lista
    return response # Retorna a lista de alunos

  def InserirMatricula(self, request, context): # Função que insere os alunos na matricula
    response = servicos.InserirMatriculaRes() # Resposta vinda do client 
    response.message = f"Matricula inserida com sucesso!"
    InserirAlunoQuery(request.RA, request.cod_disciplina, request.ano, request.semestre, request.nota, request.faltas)  # Insere os alunos na matricula
    return response

  def AlterarNota(self, request, context):  # Função que altera a nota do aluno
    response = servicos.MessageRes()  # Resposta vinda do client
    response.message = f"Nota alterada com sucesso!"
    AlterarNotaQuery(request.RA, request.cod_disciplina,  request.nota) # Altera a nota do aluno
    return response # Retorna a mensagem de sucesso

  def AlterarFaltas(self, request, context):
    response = servicos.MessageRes()  # Resposta vinda do client
    response.message = f"Faltas alterada com sucesso!"
    AlterarFaltasQuery(request.RA, request.cod_disciplina,  request.faltas) # Altera a faltas do aluno
    return response # Retorna a mensagem de sucesso
  
  def ListarDisciplinas(self, request, context):
    response = servicos.DisciplinasRes()  # Resposta vinda do client
    response.message = f"Listado com sucesso!"  
    data = ListarDisciplinasQuery(request.ano, request.semestre)  # Busca as disciplinas na matricula
    for row in data:  
      response.disciplinas.append(servicos.ListaDisciplina(RA=row[0], nome=row[1], nota=row[2], faltas=row[3])) # Adiciona as disciplinas na lista
    return response
  




def main():
  global cur    # Variável global que representa o cursor do banco de dados
  global con  # Variável de conexao
  con = sqlite3.connect('./db.db', check_same_thread=False, isolation_level=None)   # Cria a conexão com o banco de dados
  cur = con.cursor()   # Cria o cursor  

  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Cria o servidor
  servicos_grpc.add_ServicesServicer_to_server(ServicesServicer(), server)  # Adiciona o servidor ao servidor
  print('Listening 50051')
  server.add_insecure_port('[::]:50051')  #porta localhost 50051
  server.start()  # Inicia o servidor
  server.wait_for_termination() # Espera o servidor








main()

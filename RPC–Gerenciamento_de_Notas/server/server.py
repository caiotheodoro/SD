import grpc
import concurrent
from concurrent import futures

import rcp_pb2 as servicos
import rcp_pb2_grpc as servicos_grpc

class ServicesServicer(servicos_grpc.ServicesServicer):
  def ListarAlunos(self, request, context):
    print('we got something!!')
    response = servicos.AlunosRes()
    response.message = f"Listado com sucesso!"
    response.alunos.extend(
      [servicos.Aluno(RA=1,nome="João", periodo=20,cod_curso=1)
      ,servicos.Aluno(RA=2,nome="Maria", periodo=20,cod_curso=1)
      ,servicos.Aluno(RA=3,nome="Pedro", periodo=20,cod_curso=1)
      ,servicos.Aluno(RA=4,nome="José", periodo=20,cod_curso=1)
      ,servicos.Aluno(RA=5,nome="Paulo", periodo=20,cod_curso=1)
      ]
    )
    

    return response

def main():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  servicos_grpc.add_ServicesServicer_to_server(ServicesServicer(), server)
  print('Server Started. Listening on port 50051')
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

main()

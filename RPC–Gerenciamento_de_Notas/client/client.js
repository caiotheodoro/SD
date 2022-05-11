const grpc = require('grpc');
const messages = require('./rcp_pb');
const servicos = require('./rcp_grpc_pb');

function main() {
  const client = new servicos.ServicesClient(
    'localhost:50051', grpc.credentials.createInsecure()
  );

  const gerenciamentoRequest = new messages.AlunosReq();
  gerenciamentoRequest.setCodDisciplina('ES38A');
  gerenciamentoRequest.setAno(8);
  gerenciamentoRequest.setSemestre(4);

  client.listarAlunos(gerenciamentoRequest, function (err, response) {
    if (err) {
      console.log('this thing broke!', err);
    } else {
      console.log('response from python:', response.getMessage(), response.getAlunosList());
    }
  })
}

main();

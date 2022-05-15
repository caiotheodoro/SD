const grpc = require("grpc");
const messages = require("./rcp_pb");
const servicos = require("./rcp_grpc_pb");
var readline = require("readline");

const client = new servicos.ServicesClient(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

var ra;
var cod_disciplina;
var ano;
var semestre;
var nota;
var faltas;

async function main() {
  const opcao = await new Promise((resolve) => {
    rl.question(
      "\n\n\nDigite o serviço requirido: \n1 - Inserir Matricula\n2 - Alterar notas\n3 - Alterar faltas\n4 - Listar alunos\n5 - Sair\n ",
      resolve
    );
  });
 

  switch (Number(opcao)) {
    case 1:
      ra = await new Promise((resolve) => {
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      ano = await new Promise((resolve) => {
        rl.question("Digite o ano:\n ", resolve);
      });
      semestre = await new Promise((resolve) => {
        rl.question("Digite o semestre:\n ", resolve);
      });

      const inserirMatriculaRequest = new messages.Matricula();
      inserirMatriculaRequest.setRa(ra);
      inserirMatriculaRequest.setCodDisciplina(cod_disciplina);
      inserirMatriculaRequest.setAno(Number(ano));
      inserirMatriculaRequest.setSemestre(Number(semestre));
      inserirMatriculaRequest.setNota(0);
      inserirMatriculaRequest.setFaltas(0);

      client.inserirMatricula(inserirMatriculaRequest, function (err, response) {
        if (err) {
          console.log("Erro!", err);
        } else {
          console.log(response.getMessage() + "\n\n");
        }
      });

    case 2:
      ra = await new Promise((resolve) => {
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      nota = await new Promise((resolve) => {
        rl.question("Digite a nova nota:\n ", resolve);
      });

      const alterarNotaRequest = new messages.AlterarNotaReq();
      alterarNotaRequest.setRa(ra);
      alterarNotaRequest.setCodDisciplina(cod_disciplina);
      alterarNotaRequest.setNota(nota);

      client.alterarNota(alterarNotaRequest, function (err, response) {
        if (err) {
          console.log("Erro!", err);
        } else {
          console.log(response.getMessage() + "\n\n");
        }
      });

      break;
      case 3:
      ra = await new Promise((resolve) => {
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      faltas = await new Promise((resolve) => {
        rl.question("Digite as novas faltas:\n ", resolve);
      });

      const alterarFaltasRequest = new messages.AlterarFaltasReq();
      alterarFaltasRequest.setRa(ra);
      alterarFaltasRequest.setCodDisciplina(cod_disciplina);
      alterarFaltasRequest.setFaltas(faltas);

      client.alterarFaltas(alterarFaltasRequest, function (err, response) {
        if (err) {
          console.log("Erro!", err);
        } else {
          console.log(response.getMessage() + "\n\n");
        }
      });

      break;
    case 4:
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      ano = await new Promise((resolve) => {
        rl.question("Digite o ano:\n ", resolve);
      });
      semestre = await new Promise((resolve) => {
        rl.question("Digite o semestre:\n ", resolve);
      });
      const gerenciamentoRequest = new messages.AlunosReq();
      gerenciamentoRequest.setCodDisciplina(cod_disciplina);
      gerenciamentoRequest.setAno(Number(ano));
      gerenciamentoRequest.setSemestre(Number(semestre));

      client.listarAlunos(gerenciamentoRequest, function (err, response) {
        if (err) {
          console.log("Erro!", err);
        } else {
          console.log(response.getMessage() + "\n\n");
          let dados = response.getAlunosList();
          dados.forEach((element) => {
            console.log(
              `RA: ${element.array[0]} Nome: ${element.array[1]} Semestre: ${element.array[2]}`
            );
          });
        }
      });
      //sleep 1 sec then call main again

      break;
    case 3:
      process.exit();
    default:
      console.log("Opção inválida!");
      break;
  }
  setTimeout(main, 1000);
}

main();

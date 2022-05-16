// '''
//     # Descrição: #Implementar um serviço de gerenciamento de notas de uma escola usando GRPC.
//     - Tabelas:
//       - Curso
//       - Disciplina   
//       - Aluno
//       - Matricula

//     - Funções:
//       - Inserir na tabela Matricula
//       - Alterar notas e faltas na tabela Matricula
//       - Listar alunos de uma disciplina informado a disciplina, o ano e o semestre
//       - Listar disciplinas, faltas e notas informado o ano e o semestre

//     # Autores: Caio Theodoro e Gustavo Kioshi
//     # Data de criação: 08/05/2022
//     # Data de modificação: 15/05/2022
// '''


const grpc = require("grpc"); //imorta o grpc 
const messages = require("./rcp_pb"); //importa o arquivo rcp_pb.js
const servicos = require("./rcp_grpc_pb"); //importa o arquivo rcp_grpc_pb.js
var readline = require("readline"); //importa o leitor de linhas de comando

const client = new servicos.ServicesClient( //cria um novo cliente do servidor
  "localhost:50051", //endereço do servidor 
  grpc.credentials.createInsecure() //credenciais de conexão
);

const rl = readline.createInterface({ //cria um leitor de linhas de comando
  input: process.stdin, //entrada padrão
  output: process.stdout, //saída padrão
});

var ra;
var cod_disciplina;
var ano;
var semestre;
var nota;
var faltas;

async function main() { //função principal
  const opcao = await new Promise((resolve) => { 
    rl.question( //pergunta ao usuário
      "\n\n\nDigite o serviço requirido: \n1 - Inserir Matricula\n2 - Alterar notas\n3 - Alterar faltas\n4 - Listar alunos\n5 - Listar disciplinas\n6 - Sair\n ", 
      resolve 
    );
  });

  switch (Number(opcao)) {
    case 1: //caso seja inserir matricula
      ra = await new Promise((resolve) => { //le o RA
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => { //le o código da disciplina
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      ano = await new Promise((resolve) => { //le o ano
        rl.question("Digite o ano:\n ", resolve); 
      });
      semestre = await new Promise((resolve) => { //le o semestre
        rl.question("Digite o semestre:\n ", resolve);
      });
      if (ra && cod_disciplina && ano && semestre) { //se todos os campos foram preenchidos
        const inserirMatriculaRequest = new messages.Matricula(); //cria um novo objeto da classe Matricula (classe de request do rpc)
        inserirMatriculaRequest.setRa(ra); //seta o RA
        inserirMatriculaRequest.setCodDisciplina(cod_disciplina); //seta o código da disciplina
        inserirMatriculaRequest.setAno(Number(ano)); //seta o ano
        inserirMatriculaRequest.setSemestre(Number(semestre)); //seta o semestre
        inserirMatriculaRequest.setNota(0); //seta a nota (padrao 0)
        inserirMatriculaRequest.setFaltas(0); //seta as faltas (padrao 0)
 
        client.inserirMatricula( //chama o serviço inserirMatricula
          inserirMatriculaRequest, //envia o objeto criado
          function (err, response) { //recebe a resposta do servidor
            if (err) {  //se houver erro
              console.log("Erro!", err);
            } else {  //se não houver erro
              console.log(response.getMessage() + "\n\n");
            }
          }
        );
      } else {
        console.log("Os parâmetros não podem conter valores vazios!");  
      }
      break;
    case 2: //caso seja alterar notas
      ra = await new Promise((resolve) => { //le o RA
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => { //le o código da disciplina
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      nota = await new Promise((resolve) => { //le a nota
        rl.question("Digite a nova nota:\n ", resolve);
      });
      if (ra && cod_disciplina && nota) { //se todos os campos foram preenchidos
        const alterarNotaRequest = new messages.AlterarNotaReq(); //cria um novo objeto da classe AlterarNotaReq (classe de request do rpc)
        alterarNotaRequest.setRa(ra); //seta o RA
        alterarNotaRequest.setCodDisciplina(cod_disciplina);  //seta o código da disciplina
        alterarNotaRequest.setNota(nota); //seta a nota

        client.alterarNota(alterarNotaRequest, function (err, response) { //chama o serviço alterarNota
          if (err) {  //se houver erro
            console.log("Erro!", err);
          } else {  //se não houver erro
            console.log(response.getMessage() + "\n\n");
          }
        });
      } else {
        console.log("Os parâmetros não podem conter valores vazios!");
      }
      break;
    case 3: //caso seja alterar faltas
      ra = await new Promise((resolve) => {
        rl.question("Digite o RA:\n ", resolve);
      });
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      faltas = await new Promise((resolve) => {
        rl.question("Digite as novas faltas:\n ", resolve);
      });
      if (ra && cod_disciplina && faltas) { //se todos os campos foram preenchidos
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
      } else {
        console.log("Os parâmetros não podem conter valores vazios!");
      }
      break;
    case 4: //caso seja listar alunos 
      cod_disciplina = await new Promise((resolve) => {
        rl.question("Digite o código da disciplina:\n ", resolve);
      });
      ano = await new Promise((resolve) => {
        rl.question("Digite o ano:\n ", resolve);
      });
      semestre = await new Promise((resolve) => {
        rl.question("Digite o semestre:\n ", resolve);
      });

      if (ano && cod_disciplina && semestre) {  //se todos os campos foram preenchidos
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
                `RA: ${element.array[0] ? element.array[0] : "0"} Nome: ${
                  element.array[1]
                } Semestre: ${element.array[2]}`
              );
            });
          }
        });
      } else {
        console.log("Os parâmetros não podem conter valores vazios!");
      }
      break;  
    case 5: //caso seja listar disciplinas
      ano = await new Promise((resolve) => {
        rl.question("Digite o ano:\n ", resolve);
      });
      semestre = await new Promise((resolve) => {
        rl.question("Digite o semestre:\n ", resolve);
      });

      if (ano && semestre) {
        const listagemDiciplinasRequest = new messages.DisciplinasReq();
        listagemDiciplinasRequest.setAno(Number(ano));
        listagemDiciplinasRequest.setSemestre(Number(semestre));

        client.listarDisciplinas(
          listagemDiciplinasRequest,
          function (err, response) {
            if (err) {
              console.log("Erro!", err);
            } else {
              console.log(response.getMessage() + "\n\n");
              let dados = response.getDisciplinasList();
              dados.forEach((element) => {
                console.log(
                  `RA: ${element.array[0] ? element.array[0] : "0"} Nome: ${
                    element.array[1]
                  } Nota: ${
                    element.array[2] ? element.array[2] : "0"
                  } Faltas: ${element.array[3] ? element.array[3] : "0"}`
                );
              });
            }
          }
        );
      } else {
        console.log("Os parâmetros não podem conter valores vazios!");
      }

      break;  
    case 6: //caso seja sair
      process.exit();
    default:  //caso não seja nenhum dos casos anteriores
      console.log("Opção inválida!");
      break;
  }

  (ra = -1),
    (cod_disciplina = ""),
    (ano = -1),
    (semestre = -1),
    (nota = -1),
    (faltas = -1);

  setTimeout(main, 1000);
}

main();

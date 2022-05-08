<!-- 
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
    # Data de modifica -->

<!DOCTYPE html>
<html lang="en" dir="ltr">
<?php
require_once "../vendor/autoload.php";
use App\Proto\CrudMatricula;
use App\Proto\Matricula;
?>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
  <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <?php
  $host = "127.0.0.1";  //localhost
  $port = 20205;  //porta de conexão
  $sock = socket_create(AF_INET, SOCK_STREAM, 0); //cria o socket
  socket_connect($sock, $host, $port);  //conecta o socket
  $db = new SQLite3('database.db'); //cria a conexão com o banco de dados
  $editRa;  
  $editCodDisciplina; 
  $resultArray = array();
  $matricula = new Matricula(); //cria a matricula
  $resultArrayDisciplinas= array(); //cria o array de disciplinas
  $crudMatricula = new CrudMatricula(); //cria o crud de matricula
  ?>
<div style="display: flex; width: 100%; margin-top: 30px; ">
  <section style=" width: 50%; height:100%">
    <div id="myModal" class="modal modalMatricula">
      <div class="modal-content">
        <span class="close" onclick="fecharModalMatricula()">&times;</span> <!-- fecha o modal -->
        <form method="post">
          <div style="justify-content: space-between; display:flex; flex-direction: column; height: 250px;">
            <h1>Inserir Matricula</h1>
            <input type="number" name="ra" placeholder="RA" />
            <input type="text" name="cod_disciplina" placeholder="Codigo da disciplina" />
            <input type="number" name="ano" placeholder="Ano" />
            <input type="number" name="semestre" placeholder="Semestre" />
            <input type="submit" name="submit" value="submit" />
          </div>
        </form>
        <?php
        if (isset($_POST['submit'])) {  //se o submit for clicado
          $matricula->setRA($_POST['ra']);  //seta o ra
          $matricula->setSemestre($_POST['semestre']);  //seta o semestre
          $matricula->setCodDisciplina($_POST['cod_disciplina']); //seta o codigo da disciplina
          $matricula->setAno($_POST['ano']);  //seta o ano
          $crudMatricula->setMatricula($matricula); //seta a matricula
          $crudMatricula->setType(1); //seta o tipo de operação
          $matricula_string = $crudMatricula->serializeToJsonString();  //serializa a matricula
          $len = strlen($matricula_string); //tamanho da string
          socket_write($sock, $matricula_string, $len); //envia a string para o servidor
          $serv = socket_read($sock, 1024); //recebe a string do servidor
          echo "Server: \t" . trim($serv);  //imprime o servidor
        }
        ?>
      </div>
    </div>
    <div id="myModal2" class="modal modalAluno">
      <div class="modal-content">
        <span class="close" onclick="fecharModalAluno()">&times;</span>
        <form method="post">
          <div style="justify-content: space-between; display:flex; flex-direction: column; height: 250px;">
            <h1>Listar Disciplinas</h1>
            <input type="number" name="ano" placeholder="Ano" />
            <input type="number" name="semestre" placeholder="Semestre" />
            <input type="submit" name="submit2" value="submit" />
          </div>
        </form>
        <?php
        if (isset($_POST['submit2'])) { //se o submit for clicado
          $matricula->setAno($_POST['ano']);  //seta o ano
          $matricula->setSemestre($_POST['semestre']);  //seta o semestre
          $crudMatricula->setMatricula($matricula); //seta a matricula
          $crudMatricula->setType(5); //seta o tipo de operação
          $matricula_string = $crudMatricula->serializeToJsonString();  //serializa a matricula
          $len = strlen($matricula_string); //tamanho da string
          socket_write($sock, $matricula_string, $len); //envia a string para o servidor
          $serv = socket_read($sock, 1024); //recebe a string do servidor
          $resultArrayDisciplinas  = json_decode($serv, true);  //decodifica a string
          $matricula->setAno(0);  //seta o ano
          $matricula->setSemestre(0); //seta o semestre
          $matricula->setRA(0); //seta o ra
        }
        ?>
      </div>
    </div>
    <div id="myModal5" class="modal modalEditNotas">
      <div class="modal-content">
        <span class="close" onclick="fecharModalNotas()">&times;</span>
        <form method="post">
          <div style="justify-content: space-between; display:flex; flex-direction: column; height: 250px;">
            <h1>Editar Nota</h1>
            <input id="raEditNota" type="number" name="ra" placeholder="RA" value="" />
            <input id="codDisciplinaEditNota" type="text" name="cod_disciplina" placeholder="Codigo_disciplina" value="" />
            <input type="number" name="nota" placeholder="Nota" />
            <input type="submit" name="submitEditNota" value="submit" />
          </div>
        </form>
        <?php
        if (isset($_POST['submitEditNota'])) {  //se o submit for clicado
          $matricula->setNota($_POST['nota']);      //seta a nota
          $matricula->setRA($_POST['ra']);  //seta o ra
          $matricula->setCodDisciplina($_POST['cod_disciplina']); //seta o codigo da disciplina
          $crudMatricula->setMatricula($matricula); //seta a matricula
          $crudMatricula->setType(2); //seta o tipo de operação 
          $matricula_string = $crudMatricula->serializeToJsonString();  //serializa a matricula
          $len = strlen($matricula_string); //tamanho da string
          socket_write($sock, $matricula_string, $len); //envia a string para o servidor  
          $serv = socket_read($sock, 1024); //recebe a string do servidor
          echo "Server: \t" . trim($serv);  //imprime o servidor
          $matricula->setRA(0); //seta o ra
          $matricula->setCodDisciplina(0);  //seta o codigo da disciplina
        }
        ?>
      </div>
    </div>
    <div id="myModal6" class="modal modalEditFaltas">
      <div class="modal-content">
        <span class="close" onclick="fecharModalFaltas()">&times;</span>
        <form method="post">
          <div style="justify-content: space-between; display:flex; flex-direction: column; height: 250px;">
            <h1>Editar Faltas</h1>
            <input id="raEditFalta" type="number" name="ra" placeholder="RA" value="" />
            <input id="codDisciplinaEditFalta" type="text" name="cod_disciplina" placeholder="Codigo_disciplina" value="" />
            <input type="number" name="faltas" placeholder="Faltas" />
            <input type="submit" name="submitEditFalta" value="submit" />
          </div>
        </form>
        <?php
        if (isset($_POST['submitEditFalta'])) { 
          $matricula->setFaltas($_POST['faltas']);    //seta as faltas
          $matricula->setRA($_POST['ra']);  //seta o ra
          $matricula->setCodDisciplina($_POST['cod_disciplina']); //seta o codigo da disciplina
          $crudMatricula->setMatricula($matricula); //seta a matricula
          $crudMatricula->setType(3); //seta o tipo
          $matricula_string = $crudMatricula->serializeToJsonString();  //serializa a matricula
          $len = strlen($matricula_string); //tamanho da string
          socket_write($sock, $matricula_string, $len); //envia a string para o servidor
          $serv = socket_read($sock, 1024); //recebe a string do servidor
          echo "Server: \t" . trim($serv);  //imprime o servidor
          $matricula->setRA(0);
          $matricula->setCodDisciplina(0);
        }
        ?>
      </div>
    </div>
    <div id="myModal7" class="modal modalListarAlunos">
      <div class="modal-content">
        <span class="close" onclick="fecharModalListarAlunos()">&times;</span>
        <form method="post">
          <div style="justify-content: space-between; display:flex; flex-direction: column; height: 250px;">
            <h1>Listar alunos</h1>
            <input type="text" name="cod_disciplina" placeholder="Codigo Disciplina" />
            <input type="number" name="ano" placeholder="Ano" />
            <input type="number" name="semestre" placeholder="Semestre" />
            <input type="submit" name="submitListaAlunos" value="submit" />
          </div>
        </form>
        <?php
        if (isset($_POST['submitListaAlunos'])) { //se o submit for clicado
          $matricula->setCodDisciplina($_POST['cod_disciplina']); //seta o codigo da disciplina
          $matricula->setAno($_POST['ano']);  //seta o ano
          $matricula->setSemestre($_POST['semestre']);  //seta o semestre
          $crudMatricula->setMatricula($matricula); //seta a matricula
          $crudMatricula->setType(4); //seta o tipo
          $matricula_string = $crudMatricula->serializeToJsonString();  //serializa a matricula 
          $len = strlen($matricula_string); //tamanho da string
          socket_write($sock, $matricula_string, $len); //envia a string para o servidor
          $serv = socket_read($sock, 1024); //recebe a string do servidor
          @$resultArray  = json_decode($serv, true);  //decodifica a string
          $matricula->setAno(0);  //seta o ano
          $matricula->setSemestre(0); //seta o semestre
          $matricula->setCodDisciplina(0);  //seta o codigo da disciplina
        }
        ?>
      </div>
    </div>
    <div class="home-content">
      <div class="sales-boxes">
        <div class="recent-sales box" style=" background-color: #52784F;">
          <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
          ">
            <div class="title">Matriculas</div>
            <div style="display: flex; ">
          
            <div class="button" id="myBtn" style="margin-right: 10px;">
                <a onclick="abrirModalListarAlunos()">Listar alunos</a>
              </div>
              <div class="button" id="myBtn">
                <a onclick="abrirModalMatricula()">Adicionar</a>
              </div>
            </div>
          </div>
          <div class="sales-details">
          
            
            <ul class="details">

              <li class="topic"><a href="#">RA</a></li>
              <?php
               if ($resultArray) {  //se o resultado for diferente de vazio
              foreach ($resultArray as $key => $row) {  //percorre o array
                echo '<li ><a href="#">' . $row['RA'] . '</li>';  //imprime o ra
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Nome</a></li>
              <?php
               if ($resultArray) {
               foreach ($resultArray as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['nome'] . '</li>';  //imprime o nome
              }
              }
              ?>
              
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Periodo</a></li>
              <?php
              if ($resultArray) {
               foreach ($resultArray as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['periodo'] . '</a></li>'; //imprime o periodo
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Editar nota</li>
              <?php
                if ($resultArray) {
               foreach ($resultArray as $key => $row) { //percorre o array
                echo '<li><button id='. $row['RA'] . ',' . $row['codDisciplina'] .' onclick="javascript:abrirModalEditNotas(this.id)">Editar</button></li>';  //imprime o periodo
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Editar faltas</li>
              <?php
                if ($resultArray) {
               foreach ($resultArray as $key => $row) { //percorre o array
                echo '<li><button id='. $row['RA'] . ',' . $row['codDisciplina'] .' onclick="javascript:abrirModalEditFaltas(this.id)">Editar</button></li>'; //imprime o periodo
              }
            }
              ?>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section style=" width: 50%">
    <div class="home-content">
      <div class="sales-boxes">
        <div class="recent-sales box" style=" background-color: #FFBA53;">
          <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
          ">
            <div class="title">Disciplinas</div>
            
            <div style="display: flex; ">
             
              <div class="button" id="myBtn">
              <a onclick="abrirModalAluno()">Listar disciplinas</a>
            </div>
            </div>
          </div>
          <div class="sales-details">
            <ul class="details">
              <li class="topic">RA</li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['RA'] . '</li>';    //imprime o ra
              }
              ?>
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Nome</a></li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['nome'] . '</a></li>';  //imprime o nome
              } 
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Nota</li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['nota'] . '</a></li>';  //imprime o nome
              }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Faltas</li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) { //percorre o array
                echo '<li ><a href="#">' . $row['faltas'] . '</a></li>';  //imprime o nome
              }
              ?>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

  <script>
    let modalMatricula = document.querySelector(".modalMatricula"); //seleciona o modal
    let modalAluno = document.querySelector(".modalAluno"); //seleciona o modal
    let modalNota = document.querySelector(".modalEditNotas");  //seleciona o modal
    let modalFalta = document.querySelector(".modalEditFaltas");  //seleciona o modal
    let modalListarAlunos = document.querySelector(".modalListarAlunos"); //seleciona o modal
 
    // Get the modal
    function abrirModalMatricula() {  //função para abrir o modal
      modalMatricula.style.display = "block";
    }

    function fecharModalMatricula() {
      modalMatricula.style.display = "none";
    }

    function abrirModalAluno() {
      modalAluno.style.display = "block";
    }

    function fecharModalAluno() {
      modalAluno.style.display = "none";
    }

   
    function abrirModalEditNotas(id) {  //função para abrir o modal
      console.log(id)
      document.getElementById("raEditNota").value = id.split(",")[0]; //pega o ra
      document.getElementById("codDisciplinaEditNota").value = id.split(",")[1];  //pega o codigo da disciplina
      modalNota.style.display = "block";
    }

    function fecharModalNotas() {
      modalNota.style.display = "none";
    }

    function abrirModalEditFaltas(id) {
      document.getElementById("raEditFalta").value = id.split(",")[0];  //pega o ra
      document.getElementById("codDisciplinaEditFalta").value = id.split(",")[1]; //pega o codigo da disciplina
      modalFalta.style.display = "block";
    }

    function fecharModalFaltas() {
      modalFalta.style.display = "none";
    }

    function abrirModalListarAlunos() {
      modalListarAlunos.style.display = "block";
    }

    function fecharModalListarAlunos() {
      modalListarAlunos.style.display = "none";
    }

   
  </script>

</body>

</html>
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
  $host = "127.0.0.1";
  $port = 20205;
  $sock = socket_create(AF_INET, SOCK_STREAM, 0);
  socket_connect($sock, $host, $port);
  $db = new SQLite3('database.db');
  $editRa;
  $editCodDisciplina;
  $resultArray = array();
  $matricula = new Matricula();
  $resultArrayDisciplinas= array();
  $crudMatricula = new CrudMatricula();
  ?>
<div style="display: flex; width: 100%; margin-top: 30px; ">
  <section style=" width: 50%; height:100%">
    <div id="myModal" class="modal modalMatricula">
      <div class="modal-content">
        <span class="close" onclick="fecharModalMatricula()">&times;</span>
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
        if (isset($_POST['submit'])) {
          $matricula->setRA($_POST['ra']);
          $matricula->setSemestre($_POST['semestre']);
          $matricula->setCodDisciplina($_POST['cod_disciplina']);
          $matricula->setAno($_POST['ano']);
          $crudMatricula->setMatricula($matricula);
          $crudMatricula->setType(1);
          $matricula_string = $crudMatricula->serializeToJsonString();
          $len = strlen($matricula_string);
          socket_write($sock, $matricula_string, $len);
          $serv = socket_read($sock, 1024);
          echo "Server: \t" . trim($serv);
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
        if (isset($_POST['submit2'])) {
          $matricula->setAno($_POST['ano']);
          $matricula->setSemestre($_POST['semestre']);
          $crudMatricula->setMatricula($matricula);
          $crudMatricula->setType(5);
          $matricula_string = $crudMatricula->serializeToJsonString();
          $len = strlen($matricula_string);
          socket_write($sock, $matricula_string, $len);
          $serv = socket_read($sock, 1024);
          $resultArrayDisciplinas  = json_decode($serv, true);
          $matricula->setAno(0);
          $matricula->setSemestre(0);
          $matricula->setRA(0);
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
        if (isset($_POST['submitEditNota'])) {
          $matricula->setNota($_POST['nota']);
          $matricula->setRA($_POST['ra']);
          $matricula->setCodDisciplina($_POST['cod_disciplina']);
          $crudMatricula->setMatricula($matricula);
          $crudMatricula->setType(2);
          $matricula_string = $crudMatricula->serializeToJsonString();
          $len = strlen($matricula_string);
          socket_write($sock, $matricula_string, $len);
          $serv = socket_read($sock, 1024);
          echo "Server: \t" . trim($serv);
          $matricula->setRA(0);
          $matricula->setCodDisciplina(0);
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
          $matricula->setFaltas($_POST['faltas']);
          $matricula->setRA($_POST['ra']);
          $matricula->setCodDisciplina($_POST['cod_disciplina']);
          $crudMatricula->setMatricula($matricula);
          $crudMatricula->setType(3);
          $matricula_string = $crudMatricula->serializeToJsonString();
          $len = strlen($matricula_string);
          socket_write($sock, $matricula_string, $len);
          $serv = socket_read($sock, 1024);
          echo "Server: \t" . trim($serv);
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
        if (isset($_POST['submitListaAlunos'])) {
          $matricula->setCodDisciplina($_POST['cod_disciplina']);
          $matricula->setAno($_POST['ano']);
          $matricula->setSemestre($_POST['semestre']);
          $crudMatricula->setMatricula($matricula);
          $crudMatricula->setType(4);
          $matricula_string = $crudMatricula->serializeToJsonString();
          $len = strlen($matricula_string);
          socket_write($sock, $matricula_string, $len);
          $serv = socket_read($sock, 1024);
          @$resultArray  = json_decode($serv, true);
          $matricula->setAno(0);
          $matricula->setSemestre(0);
          $matricula->setCodDisciplina(0);
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
               if ($resultArray) {
              foreach ($resultArray as $key => $row) {
                echo '<li ><a href="#">' . $row['RA'] . '</li>';
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Nome</a></li>
              <?php
               if ($resultArray) {
               foreach ($resultArray as $key => $row) {
                echo '<li ><a href="#">' . $row['nome'] . '</li>';
              }
              }
              ?>
              
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Periodo</a></li>
              <?php
              if ($resultArray) {
               foreach ($resultArray as $key => $row) {
                echo '<li ><a href="#">' . $row['periodo'] . '</a></li>';
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Editar nota</li>
              <?php
                if ($resultArray) {
               foreach ($resultArray as $key => $row) {
                echo '<li><button id='. $row['RA'] . ',' . $row['codDisciplina'] .' onclick="javascript:abrirModalEditNotas(this.id)">Editar</button></li>';
              }
            }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Editar faltas</li>
              <?php
                if ($resultArray) {
               foreach ($resultArray as $key => $row) {
                echo '<li><button id='. $row['RA'] . ',' . $row['codDisciplina'] .' onclick="javascript:abrirModalEditFaltas(this.id)">Editar</button></li>';
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
              foreach ($resultArrayDisciplinas as $key => $row) {
                echo '<li ><a href="#">' . $row['RA'] . '</li>';
              }
              ?>
            </ul>
            <ul class="details">
              <li class="topic"><a href="#">Nome</a></li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) {
                echo '<li ><a href="#">' . $row['nome'] . '</a></li>';
              }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Nota</li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) {
                echo '<li ><a href="#">' . $row['nota'] . '</a></li>';
              }
              ?>
            </ul>
            <ul class="details">
              <li class="topic">Faltas</li>
              <?php
              foreach ($resultArrayDisciplinas as $key => $row) {
                echo '<li ><a href="#">' . $row['faltas'] . '</a></li>';
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
    let modalMatricula = document.querySelector(".modalMatricula");
    let modalAluno = document.querySelector(".modalAluno");
    let modalNota = document.querySelector(".modalEditNotas");
    let modalFalta = document.querySelector(".modalEditFaltas");
    let modalListarAlunos = document.querySelector(".modalListarAlunos");
 
    // Get the modal
    function abrirModalMatricula() {
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

   
    function abrirModalEditNotas(id) {
      console.log(id)
      document.getElementById("raEditNota").value = id.split(",")[0];
      document.getElementById("codDisciplinaEditNota").value = id.split(",")[1];
      modalNota.style.display = "block";
    }

    function fecharModalNotas() {
      modalNota.style.display = "none";
    }

    function abrirModalEditFaltas(id) {
      document.getElementById("raEditFalta").value = id.split(",")[0];
      document.getElementById("codDisciplinaEditFalta").value = id.split(",")[1];
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
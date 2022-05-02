const Schema = require("./methods/matriculas_pb");

const matricula = new Schema.Matricula();

matricula.setRa(2044560);
matricula.setCodDisciplina("12345");
matricula.setAno(4);
matricula.setSemestre(8);
matricula.setNota(10.5);
matricula.setFaltas(12);

const bytes = matricula.serializeBinary();

console.log(bytes);
console.log(matricula);

const matriculas2 = Schema.Matricula.deserializeBinary(bytes);

console.log(matriculas2.toString());

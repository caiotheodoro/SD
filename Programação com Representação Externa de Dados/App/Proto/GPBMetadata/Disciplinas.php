<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disciplinas.proto

namespace App\Proto\GPBMetadata;

class Disciplinas
{
    public static $is_initialized = false;

    public static function initOnce() {
        $pool = \Google\Protobuf\Internal\DescriptorPool::getGeneratedPool();

        if (static::$is_initialized == true) {
          return;
        }
        $pool->internalAddGeneratedFile(
            '
�
disciplinas.proto"P

Disciplina
codigo (	
nome (	
	professor (	
	cod_curso ("?
CrudDisciplina
type (

disciplina (2.DisciplinaB$�	App\\Proto�App\\Proto\\GPBMetadatabproto3'
        , true);

        static::$is_initialized = true;
    }
}


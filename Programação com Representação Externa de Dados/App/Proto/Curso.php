<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cursos.proto

namespace App\Proto;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>Curso</code>
 */
class Curso extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>string codigo = 1;</code>
     */
    protected $codigo = '';
    /**
     * Generated from protobuf field <code>string nome = 2;</code>
     */
    protected $nome = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $codigo
     *     @type string $nome
     * }
     */
    public function __construct($data = NULL) {
        \App\Proto\GPBMetadata\Cursos::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>string codigo = 1;</code>
     * @return string
     */
    public function getCodigo()
    {
        return $this->codigo;
    }

    /**
     * Generated from protobuf field <code>string codigo = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setCodigo($var)
    {
        GPBUtil::checkString($var, True);
        $this->codigo = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string nome = 2;</code>
     * @return string
     */
    public function getNome()
    {
        return $this->nome;
    }

    /**
     * Generated from protobuf field <code>string nome = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setNome($var)
    {
        GPBUtil::checkString($var, True);
        $this->nome = $var;

        return $this;
    }

}


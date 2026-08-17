'''Teste com @Dataclass As dataclasses são uma forma simplificada de criar classes que armazenam dados,
implementando classes com atributos e métodos específicos para manipulação de dados.'''

from dataclasses import dataclass


@dataclass
class Usuario:
    id: str
    nome: str
    idade: int
    email: str


def test_dados_usuario():
    #Arrange
    id_usuario = 1
    nome = "Fryero"
    idade = 30
    email = "fryero@mail.com"

    #Act

    v = Usuario(id_usuario, nome, idade, email)

    #Assert

    assert v.id == id_usuario
    assert v.nome == nome
    assert v.idade == idade
    assert v.email == email



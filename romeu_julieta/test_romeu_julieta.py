def romeu_e_julieta( val: int): #SUT é a unidade que vai ser testada
    ''' Parametros val é um inteiro

        Se val for divisivel por 3 == 'Queijo'
        Se val for divisivel por 5 == 'Goiabada'
        Se val for divisivel por 3 e 5 == 'Romeu e Julieta'
        Se val não for divisivel por 3 ou 5 == 'val'
    
    '''
    match val % 3 == 0, val % 5 == 0:
        case [True, False]:
            return 'Queijo'
        case [False, True]:
            return 'Goiabada'
        case [True, True]:
            return "Romeu e Julieta"
        case _:
            return val
#Pytest
def test_romeu_e_julieta():
    '''
    Quatro fases de testes: SetUp / Preparação, Exersice / Exercício, Verifity / Verificação e TearDown / 
    AAA: Arrange, Act e Assert
    
    '''
    #Arrange / SetUp

    valor_inserido = 3
    valor_desejado = 'Queijo'

    #Act / Exercise / Chamada do SUT (chamar a função que vai ser testada)

    resultado = romeu_e_julieta (valor_inserido)

    #Assert / Verifity / Fase de Verificação

    assert resultado == valor_desejado


    '''Como executar os testes: 
        pytest test_romeu_julieta.py -v // 
        ''coverage''
        pytest test_romeu_julieta.py -v --cov=romeu_julieta 
        ou 
        pytest test_romeu_julieta.py -v --cov=. quando o teste está dentro do mesmo arquivo
    '''
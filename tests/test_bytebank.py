from Aula_9_1_Bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    # Aula_9_2_Pytest.py
    def test_quando_idade_recebe_13_03_20_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 23
        
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)        
        resultado = funcionario_teste.idade() # When-Ação
        
        assert resultado == esperado #Then-Desfecho
    
    # Aula_9_2_Mais_Teste.py
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado
    
    # @mark.skip
    # Aula_9_3_Funcionalidade_Nova.py
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then
    
    @mark.calcular_bonus
    # Aula_9_4_Exception.py
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado  # then
    
    @mark.calcular_bonus
    # Aula_9_4_Exception_Pytest.py
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then
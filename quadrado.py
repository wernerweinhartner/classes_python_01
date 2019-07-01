# -*- coding: utf-8 -*-

from helper import input_type

lado = 10

class Quadrado:
    """
    Nomes de classes devem utilizar o  padrao CamelCase:
        MinhaClasse
    nomes de métodos e atributos devem utilizar o padrão underline:
        meu_atributo
        meu_metodo
    """
    # Atributos
    lado = 0
    nome = ''

    # Métodos
    def set_lado(self, valor):
        self.lado = valor

    def get_lado(self):
        return "%0.2f cm" % (float(self.lado))

    def calcular_area(self):
        return float(self.lado * self.lado)

    def area_formatada(self):
        area = self.calcular_area()
        return "%0.2f cm²" % (area)

    def __str__(self):
        return self.nome

    def imprimir(self):
        area_superior = ' ' + ('-' * self.lado)
        area_lateral = '|' + (' ' * self.lado) + '|'
        
        print(area_superior);
        for i in range(0, self.lado):
            print(area_lateral)
        print(area_superior)

    def teste_args(self, *args):
        """
        *args recebe multiplos parametros e os transforma em
        uma tupla.
        Ex de chamada: objeto.teste_args(1, 2, 3);
        resultando na tupla: (1,2,3)
        """
        print(args)


    def teste_kwargs(self, **kwargs):
        """
        *kwargs recebe multiplos parametros nomeados e os transforma em
        um dicionario, contendo o nome como a chave do valor.
        Ex: objeto.teste_kwargs(nome='rober', param1=10)
        resultando no dicionario: {'nome': "rober", 'param1': 10}
        """
        print(kwargs)

#Instanciar === inicializar um objeto através de uma classe
# execucaodo meu programa
quad = Quadrado()
quad.lado = 10
quad.set_lado(10)


#  ----- 
# |     |
# |     |
# |     |
# |     |
#  ----- 
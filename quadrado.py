# -*- coding: utf-8 -*-

from helper import input_type

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
    def set_lado(self, valor_lado):
        self.lado = valor_lado

    def get_lado(self):
        return "%0.2f cm" % (float(self.lado))

    def calcular_area(self):
        return float(self.lado * self.lado)

    def area_formatada(self):
        area = self.calcular_area()
        return "%0.2f cm²" % (area)


# execucaodo meu programa
quad = Quadrado()

quad.lado = input_type("Informe o lado do quadrado: ", 'float>0')
print("A área do quadrado é %s." % (quad.area_formatada()))




    



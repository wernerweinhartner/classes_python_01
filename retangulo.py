class Retangulo:
    #Atributos (variáveis dentro de classes)
    lado1 = 0
    lado2 = 0
    #self === acessa um atributo da classe
    #nos métodos (funções) somente o parametro SELF é obrigatório
    #Caso necessário receber mais parâmetros adicionar depois do self
    #Ou seja: so havera algo alem do self se for receber um (ou mais) parametro(s)
    #set é uma boa prática para indicar alteração do valor de um atributo
    #assim como o get é uma convenção para indicar o retorno do valor de um atributo
    def set_lado1(self, altura):
        self.lado1 = altura

    def set_lado2(self, largura):
        self.lado2 = largura
    
    def set_lados(self, altura, largura):
        self.lado1 = altura
        self.lado2 = largura

    def get_lado1(self):
        return ('A altura do retângulo é: %s' % (str(self.lado1) + 'cm'))

    def get_lado2(self):
        return ('A largura do retângulo é: %s' % (str(self.lado2) + 'cm'))

    def calcular_area(self):
        return ('A área do retângulo é: %s' % (str(self.lado1*self.lado2) + 'cm²'))

    def perimetro(self):
        perimetro = float(((self.lado1)*2) + ((self.lado2)*2))
        return ('O perímetro do retângulo é: %s' % ((str(perimetro)+ 'cm')))

    def desenho(self):
        print(' ' + (self.lado2*'-') + ' ')
        for i in range(0, (self.lado1)):
            print('|' + ((self.lado2))*' ' + '|')
        print(' ' + (self.lado2*'-') + ' ')


r = Retangulo()
r.set_lados(10,20)
# print(r.lado1)
# print(r.lado2)
print(r.get_lado1())
print(r.get_lado2())
print(r.calcular_area())
print(r.perimetro())
print(r.desenho())
    


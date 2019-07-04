"""
Implemente a classe Funcionário. Um empregado tem um nome (um string)
 e um salário(um double). Escreva um construtor com dois parâmetros 
 (nome e salário) e métodos para devolver nome e salário.
  Escreva um pequeno programa que teste sua classe.

"""
"""
Aprimore a classe do exercício anterior para
 adicionar o método aumentarSalario (porcentualDeAumento) 
 que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)


"""
class Funcionario:
    #Atributos

    nome = ''
    salario = 0
    aumento = 0
    #Metodos:

    def set_nome(self, nome):
        self.nome = nome

    def set_salario(self, salario):
        self.salario = salario

    def get_nome(self):
        return ('Nome do funcionário: %s' % (self.nome))

    def get_salario(self):
        return ('Salário: R$ %s' % (self.salario))

    # def set_aumento(self, aumento):
    #     self.aumento = aumento

    def aumento(self):
        a = input('Você gostaria de dar um aumento ao funcionário %s (s ou n)? ' % (self.nome))
        if a == 's':
            b = input('Qual a porcentagem de aumento de salário? ')
            prc = b + '%'
            b = float(b)
            b = b/100
            self.salario = float(self.salario)
            self.salario += self.salario*b
            return('O novo salário será R$ %.2f' % (self.salario))
        else:
            self.salario = float(self.salario)
            return ('O salário continuará R$ %.2f' % (self.salario))


f = Funcionario()
f.set_nome(input('Informe o nome do funcionário: '))
f.set_salario(input('Informe o salário desse funcionário: '))
print(f.get_nome())
print(f.get_salario())
print(f.aumento())
"""
Crie uma classe para implementar uma conta corrente.
 A classe deve possuir os seguintes atributos: 
 número da conta, nome do correntista e saldo.
  Os métodos são os seguintes: alterarNome, 
  depósito e saque; No construtor, saldo é opcional,
   com valor default zero e os demais atributos são obrigatórios.

"""

class Conta:
    #Atributos:
    num_conta = 0
    nome = ''
    saldo = 0

    #Metodos:
    def set_num_conta(self, conta):
        self.num_conta = conta

    def set_nome(self, nome_correntista):
        self.nome = nome_correntista

    def set_saldo(self, saldo):
        self.saldo = float(saldo)

    def get_nome(self):
        return self.nome

    def get_num_conta(self):
        return self.num_conta

    # def get_saldo(self):
    #     """
    #     Alterar para somente retornar o valor do saldo.
    #     """
    #     a = float(input('Qual o valor que você deseja depositar?: '))
    #     b = float(input('Qual o valor que você deseja sacar?: '))
    #     self.saldo = float(self.saldo)
    #     self.saldo += a - b
    #     if self.saldo < 0:
    #         return ('Atenção! Seu saldo está negativo em  R$ %.2f!' % (self.saldo))
    #     else:
    #         return ('Seu saldo é: R$ %.2f' % (self.saldo))
    
    def sacar(self, saque):
        """
        Deve receber um valor a ser sacado, subtrair do saldo e retornar o mesmo valor
        sacado para o usuário.
        """
        saque_permitido = 0
        if saque > self.saldo:
            saque_permitido = self.saldo
            if saque_permitido == 0:
                print('Seu saldo já está zerado')
            self.saldo = 0
            return saque_permitido
        else: 
            self.saldo = self.saldo - saque
            return saque



    def depositar(self, dep):
        """
        Deve receber um valor a ser depositado e adiciona-lo ao saldo.
        Nao precisa retornar nada.
        """
        self.saldo += dep

    def get_saldo(self):
        return self.saldo


c = Conta()
c.set_nome(input('Informe seu nome: '))
c.set_num_conta(input('Insira o número da sua conta corrente: '))
c.set_saldo(input('Informe seu saldo: '))
dep = float(input('Quanto você gostaria de depositar?: '))
c.depositar(dep)
saque = float(input('Quanto você gostaria de sacar?: '))
c.sacar(saque)
print('Nome do correntista: ' + c.get_nome())
print('Número de conta corrente: ' + c.get_num_conta())
print(c.get_saldo())
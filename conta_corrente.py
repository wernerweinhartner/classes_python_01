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

    def __init__(self, valor = 0):
        """
        Construtor da Classe, executado sempre que a classe Conta é instanciada,
        ex: 
        Instanciar a classe Conta sem passar parametros:
            conta = Conta()
        Instanciar a classe Conta passando como parametro o valor do saldo de 100 reais:
            conta = Conta(100)
        """
        if valor:
            self.saldo = valor

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


# c = Conta()
# c.set_nome(input('Informe seu nome: '))
# c.set_num_conta(input('Insira o número da sua conta corrente: '))
# c.set_saldo(input('Informe seu saldo: '))
# dep = float(input('Quanto você gostaria de depositar?: '))
# c.depositar(dep)
# saque = float(input('Quanto você gostaria de sacar?: '))
# c.sacar(saque)
# print('Nome do correntista: ' + c.get_nome())
# print('Número de conta corrente: ' + c.get_num_conta())
# print(c.get_saldo())


# Exemplo de instancia da classe Conta passando um parametro para o construtor.
conta = Conta(100)
print("Saldo = %0.2f." % conta.get_saldo())

op = ''

while op != '0':
    print(" ")
    print("-----------------")
    print("Opções da Conta:")
    print(" 1 - Depositar.")
    print(" 2 - Sacar.")
    print(" 3 - Ver Saldo.")
    print(" 0 - Sair.")
    op = input("Escolha uma das opções:")

    if op == '1':
        valor = float(input("Valor a ser depositado: "))
        conta.depositar(valor)
    elif op == '2':
        valor = float(input("Valor a ser sacado: "))
        conta.sacar(valor)
    elif op == '3':
        print("Saldo atual = %0.2f." % conta.get_saldo())
    elif op == '0':
        print("Tchau.")
    else:
        print("Opção inválida.")
    


# Exmplos de manipulacao de data:
from datetime import datetime

# Pegar a data atual na variavel date:
date = datetime.now() # A partir daqui date é um objeto do tipo datetime (uma instancia de datetime).
# formata o objeto date para string no padrao brasileiro:
data_atual = date.strftime("%d/%m/%Y %H:%M:%S")
print("Data e hora atuais: %s." % (data_atual))

# Para converter uma data string em objeto datetime:
data = datetime.strptime("01/02/2001 10:30:00", "%d/%m/%Y %H:%M:%S")
# Convertendo somente a data:
data = datetime.strptime("01/02/2001", "%d/%m/%Y")
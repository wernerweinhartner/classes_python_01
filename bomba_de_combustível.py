"""
Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido
 e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade 
em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade
 de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é 
necessário atualizar a quantidade de combustível total na bomba.

"""

class BombaDeCombustivel:
    #Atributos:
    combustivel = ''
    preço = 0
    quantidade = 0
    quantidade_bomba = 0
    #Métodos:

    def set_quantidade_bomba(self, qtd_bomba):
        self.quantidade_bomba = qtd_bomba

    def set_tipo_de_combustivel(self, combustivel):
        self.combustivel = combustivel

    def set_preço_por_litro(self, preço):
        self.preço = preço

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_tipo_fuel(self):
        return ('Você escolheu: %s' % (self.combustivel.capitalize()))

    def get_preço_litro(self):
        self.preço = float(self.preço)
        return ('Você pagará R$ %.2f por litro desse combustível' % (self.preço))

    def get_quantidade(self):
        return self.quantidade

    def abastecer_valor(self):
        a = float(input('Informe quantos reais você gostaria de gastar: '))
        self.preço = float(self.preço)
        p = a/self.preço
        return ('Com R$ %.2f, você terá %.2f litros de combustivel' % (a, p))

    def abastecer_litro(self):
        e = float(input('Informe quantos litros você gostaria de abastecer: '))
        self.quantidade = e
        self.preço = float(self.preço)
        o = e*self.preço
        return ('Para abastecer %.1f litros, você pagará R$ %.2f' % (e, o))

    def set_altera_valor(self, novo_valor):
        self.preço = novo_valor

    def set_altera_fuel(self, novo_fuel):
        self.combustivel = novo_fuel

    def fuel_left(self):
        self.quantidade_bomba = float(self.quantidade_bomba)
        self.quantidade = float(self.quantidade)
        y = self.quantidade_bomba - self.quantidade
        return ('Quantidade restante de combustível na bomba: %.2f litros' % (y))


b = BombaDeCombustivel()
b.set_tipo_de_combustivel('gasolina')
b.set_preço_por_litro('4.00')
#b.set_quantidade('15')
b.set_altera_fuel(input('Insira o tipo de combustível: '))
b.set_quantidade_bomba(input('Insira a quantidade inicial de combustível na bomba: '))
b.set_altera_valor(input('Informe o valor por litro do combustível: '))
print(b.get_tipo_fuel())
print(b.get_preço_litro())
ask = input('Você gostaria de abastecer por valor ou por litro? (v ou l): ')
if ask == 'l': 
    print(b.abastecer_litro())
else:
    print(b.abastecer_valor())
#print(b.get_quantidade())
print(b.fuel_left())
#Fazer menu

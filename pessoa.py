"""
Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: 
Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
Após os 30 anos, a cada ano envelhecido a pessoa deve adquirir 1kg a mais.
(é uma pessoa beeeem sedentária).

"""

# class Pessoa:
#     nome = ''
#     idade = 0
#     peso = 0
#     altura = 0
    
#     #get === serve mais para formatar dados
#     def set_nome(self, nome_completo):
#         self.nome = nome_completo

#     def set_idade(self, idade):
#         self.idade = idade

#     def set_peso(self, peso):
#         self.peso = peso
    
#     def set_altura(self, altura):
#         self.altura = altura

#     def get_nome(self):
#         return ('Nome completo: %s' % (self.nome))
    
#     def get_idade(self):
#         return ('Idade: %s anos' % (self.idade))

#     def get_altura(self):
#         return ('Altura: %s metros' % (str(self.altura)))

#     def get_peso(self):
#         return ('Peso: %s kg' % (str(self.peso)))

#     def crescer(self):
#         self.idade = float(self.idade)
#         self.altura = float(self.altura)
#         if self.idade < 21:
#             self.altura += 0.05
#         return ('A sua altura daqui a 1 ano será: %.2f m' % (self.altura))

#     def engordar(self):
#         self.idade = float(self.idade)
#         self.peso = float(self.peso)
#         if self.idade > 30:
#             self.peso += 1
#         return ('O seu peso daqui a 1 ano será: %.2f kg' % (self.peso))
        



# p = Pessoa()
# p.set_nome('Werner Heckler')
# p.set_idade('25')
# p.set_altura('1.8')
# p.set_peso('80')
# print(p.get_nome())
# print(p.get_idade())
# print(p.crescer())
# print(p.engordar())


class Pessoa:
    nome = ''
    idade = 0
    peso = 0
    altura = 0
    previsao_altura = 0
    previsao_peso = 0
    #get === serve mais para formatar dados
    #previsao_altura === inserir quantos anos falta pra 21. quanto vai crescer
    #ate la
    #previsao peso === vai informar qual sera o peso em x anos
    def set_previsao_altura(self, altura2):
        self.previsao_altura = altura2

    def set_previsao_peso(self, peso2):
        self.previsao_peso = peso2

    def get_previsao_altura(self):
        return self.previsao_altura

    def get_previsao_peso(self):
        return self.previsao_peso

    def set_nome(self, nome_completo):
        self.nome = nome_completo

    def set_idade(self, idade):
        self.idade = idade

    def set_peso(self, peso):
        self.peso = peso
    
    def set_altura(self, altura):
        self.altura = altura

    def get_nome(self):
        return ('Nome completo: %s' % (self.nome))
    
    def get_idade(self):
        return ('Idade: %s anos' % (self.idade))

    def get_altura(self):
        return ('Altura: %s metros' % (str(self.altura)))

    def get_peso(self):
        return ('Peso: %s kg' % (str(self.peso)))

    def crescer(self):
        self.idade = float(self.idade)
        self.altura = float(self.altura)
        if self.idade < 21:
            self.altura += 0.05
        return ('A sua altura daqui a 1 ano será: %.2f m' % (self.altura))

    def engordar(self):
        self.idade = float(self.idade)
        self.peso = float(self.peso)
        r = self.peso
        if self.idade >= 30:
            self.peso += 1
        elif self.idade < 30:
            self.peso += 0.5
        return ('O seu peso atual é %.2f kg. Daqui a 1 ano ele será: %.2f kg' % (r, self.peso))
        
    def crescer2(self):
        self.idade = float(self.idade)
        self.altura = float(self.altura)
        self.previsao_altura = float(self.previsao_altura)
        a = 0
        if self.idade < 21:
            while a < self.previsao_altura:
                a += 1
                self.altura += 0.005
            return ('Quando completar 21 anos, sua altura será %.2f m' % (self.altura))
        else:
            return ('Sua fase de crescimento já passou')
    #Arrumar o detalhe da idade referente ao aumento de peso
    #O aumento será efetivo a partir dos 30 anos
    #Ex: a pessoa tem 20 anos e quer saber o seu peso daqui a 40 anos
    #Entao o aumento efetivo sera 30 - 20 =10 ===== 40 - 10 = 30 
    #Logo o aumento vai corresponder a 30 anos (30kg)
    def engordar2(self):
        self.idade = float(self.idade)
        self.peso = float(self.peso)
        self.previsao_peso = int(self.previsao_peso)
        if self.idade > 30:
            b = 0
            while b <= self.previsao_peso:
                b += 1
                self.peso += 1
            return ('Em %d anos, seu peso será %.2f kg' % (self.previsao_peso, (self.peso -2)))
        elif self.idade < 30:
            z = 30 - self.idade
            w = self.previsao_peso - z
            y = 0
            while y <= w:
                y += 1
                self.peso += 1
            return ('Em %d anos, seu peso será %.2f kg' % (self.previsao_peso, self.peso))











p = Pessoa()
p.set_nome(input('Insira seu nome: '))
p.set_idade(input('Insira sua idade: '))
c = float(input('Insira sua altura: '))
p.set_altura(c)
p.set_peso(input('Insira seu peso: '))
p.set_previsao_altura(str(21 - c))
p.set_previsao_peso(input('Insira um periodo de tempo para ver qual sera seu peso ao final desse periodo: '))
# print(p.get_previsao_peso())
# print(p.get_previsao_altura())
print(p.get_nome())
print(p.get_idade())
print(p.crescer())
print(p.crescer2())
print(p.engordar())
print(p.engordar2())


# def engordar2(self):
#         self.idade = float(self.idade)
#         self.peso = float(self.peso)
#         self.previsao_peso = int(self.previsao_peso)
#         if self.idade > 30:
#             b = 0
#             while b < self.previsao_peso:
#                 b += 1
#                 self.peso += 1
#             return ('Em %d anos, seu peso será %f kg' (self.previsao_peso, self.peso))
#         else:
#             return ('Você ainda não vai engordar')
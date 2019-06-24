#-*- encoding: utf-8 -*-

# Funcoes auxiliares

# Declaração da funcão/método: é todo o código do início ao final da função.
# Assinatura da função: é composta pelo nome dela e parametros recebidos.

def input_type(message, type_input):
    """
    *** ISTO É UMA DOCSTRING (comentario para documentação do código) ***
    Este método tem comportamento similar ao método nativo input().
    O parâmetro message recebe a mensagem (string) a ser exibida para o usuário.
    O parâmetro type_input determina o tipo de dado que este input deverá retornar para o usuário.
    type_input aceitos:
        'str': retorna uma string normal.
        'int': retorna um inteiro.
        'int>0': retorna um inteiro maior que zero.
        'int>=0': retorna um inteiro maior ou igual a zero.
        'float': retorna um valor float.
        'float>0': retorna um valor float maior que zero.
        'float>=0': retorna um valor float maior ou igual a zero.
    """
    valor = None

    if type_input == 'str':
        # Aceita qualquer caracter string
        while valor == None:
            try:
                valor = input(message)
            except:
                valor = None
    elif type_input == 'int':
        # Aceita qualquer caracter numerico inteiro (positivo, negativo ou zero)
        while valor == None:
            try:
                valor = int(input(message))
            except:
                valor = None
    elif type_input == 'int>0':
        # Aceita somente caracteres numéricos Positivos maiores que zero.
        valor = 0
        while valor <= 0:
            try:
                valor = int(input(message))
            except:
                valor = 0
    elif type_input == 'int>=0':
        # Aceita somente caracteres numéricos positivos maiores ou iguais a zero
        valor = 0
        while valor < 0:
            try:
                valor = int(input(message))
            except:
                valor = -1
    elif type_input == 'float':
        # Aceita somente caracteres numéricos decimais (positivos, negativos ou zero)
        while valor == None:
            try:
                valor = float(input(message))
            except:
                valor = None
    elif type_input == 'float>=0':
        # Aceita somente caracteres numéricos decimais positivos maiores ou iguais a zero
        valor = -1.0
        while valor < 0.0:
            try:
                valor = float(input(message))
            except:
                valor = -1.0
    elif type_input == 'float>0':
        # Aceita somente caracteres numéricos decimais positivos maiores que zero
        valor = 0.0
        while valor <= 0.0:
            try:
                valor = float(input(message))
            except:
                valor = 0
    return valor


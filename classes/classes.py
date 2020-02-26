####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
# Reference: https://www.w3schools.com/python/python_classes.asp
####################################################
#

class FirstClass:
    def __init__(self):
        self == __init__

class Pessoa:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def informacoes(self):
        nome = self.name
        idade = self.age
        return "Olá, eu sou o/a {} e tenho {}".format(nome,idade)

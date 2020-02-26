####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
# Reference: https://www.w3schools.com/python/python_classes.asp
####################################################
#

from classes import Pessoa
import sys

if sys.version_info.major == 2:
    nome = raw_input("Insira seu nome: ")
elif sys.version_info.major == 3:
    nome = input("Insira seu nome: ")

idade = str(input("Insira sua idade: "))

pessoa = Pessoa(nome,idade)
print(pessoa.informacoes())

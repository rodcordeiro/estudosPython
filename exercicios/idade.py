# -*- coding: utf-8 -*-
#Lista de exercicios - Exercicio1
#Solicitando a idade e verificando se é maior ou menor de idade

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

if idade <18:
	msg = "menor de idade"
else:
	msg = "maior de idade"

print("Olá {}, você tem {} anos e é {}.".format(nome,idade,msg))
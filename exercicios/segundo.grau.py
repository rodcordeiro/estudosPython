# -*- coding: utf-8 -*-
#Escreva um programa que resolva uma equação de segundo grau.   
#

import math


print("""
 Hoje iremos calcular uma equaçao de segundo grau! Para isso preciso que insira os valores de a, b e c.
""")

a=int(input("Insira o valor de a: "))
b=int(input("Insira o valor de b: "))
c=int(input("Insira o valor de c: "))
print("""Então nossa equação é:
{}x^2+{}x+{} = 0
""".format(a,b,c))

#Calculando o delta
d=int((b**2)-4*a*c)

#Bhaskara
x1 = int((-b + math.sqrt(d))/2*a)
x2 = int((-b - math.sqrt(d))/2*a)


print("""
E suas respostas são:
X1 = {}
X2 = {}""".format(x1,x2))
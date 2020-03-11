# -*- coding: utf-8 -*-
# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
op = raw_input("Insira a operação: ")
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "%":
    result = num1 % num2
elif op == "**":
    result = num1 ** num2


print("{} {} {} = {}".format(num1,op,num2, result))

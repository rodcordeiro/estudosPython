####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
####################################################
#
from classes import Password, Validacoes

print("Generating Password")
def password():
    passwd = Password().generate()
    validate = Validacoes(passwd).validate()
    if validate != False:
        print('='*10+'\n'+passwd)
        print(validate[1])
        print("Pontuação: {}".format(validate[0]))
    else:
        password()

password()

#  -*- coding: utf-8 -*-
from random import choice



def password():
    passwd = Password().generate()
    print('\n'+'='*10+'\n'+passwd)
    # validaPass(passwd)

password()
password()
password()

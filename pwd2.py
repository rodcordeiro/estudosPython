#  -*- coding: utf-8 -*-
from random import choice

def validaPass(passwd):
    pwd = validaTamanho(passwd)[0]

    print pwd

def validaTamanho(pwd):
    if len(pwd) > 8:
        return {'tamanho':len(pwd),'pontos':len(pwd)*4,'requires':1}

def pwdSize():
    size = choice(range(12))
    while size <=8:
        size = choice(range(12))
    return size


def passGen():
    special_characters=['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '.', ',', ';', '?', '{', '[', '}', ']', '^', '>', '<', ':']
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    all=numbers + special_characters + uppercase + lowercase
    passwd = ''.join([choice(all) for a in range(pwdSize())])
    return passwd

def pwd():
    passwd = passGen()
    print('\n'+'='*10+'\n'+passwd)
    validaPass(passwd)

pwd()
pwd()
pwd()

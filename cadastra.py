#!/usr/bin/env python

import pymongo
import random
import datetime

cli = pymongo.MongoClient()

db = cli['treinamento']

def gera_nome():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pw_length = 16
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    return(mypw)


ufs = ['AC','AP','AM','RO','PI','PE','CE','DF','RJ','SP','SC','RS','GO']

while True:
    cod = random.randint(1,9999999)
    nome = gera_nome()
    email = nome + "@email.net"
    agora = datetime.datetime.now()
    db.cadastro.insert({
        'cod': cod,
        'nome': nome,
        'email': email,
        'uf': random.choice(ufs),
        'data_cadastro': agora})

    print nome



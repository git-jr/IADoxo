#!/usr/bin/env python
# -*-coding:utf8;-*-

import os
import time
from util import Cronos
from util import Arquivo
from androidhelper import sl4a
import androidhelper as android


class Load:
    nomeUsu, nomeIa, primeiroUso = "", "", ""  # Inicializando

    def __init__(self):
        pass

    def carregarInformacoesIniciais(self):
        arquivo = Arquivo()

        if not arquivo.lertudo()[1]:
            arquivo.criar("/infos.txt")

        info = arquivo.lertudo()
        return info

    def iniciar(self, info):
        self.nomeUsu = info[0]  # Nome do usuário é a primeria linha do arquivo txt
        self.nomeIa = info[1]
        self.primeiroUso = str(info[2])  # "0" se for o primeiro uso da IA e "1" se não for

        self.nomeUsu = self.nomeUsu[:-1]  # Retira o caractere "\n" gerado na leitura de arquivos txt
        self.nomeIa = self.nomeIa[:-1]

        if "0" in self.primeiroUso:
            droid = sl4a.Android()
            self.nomeUsu, self.nomeIa = None, None

            while self.nomeUsu is None:
                self.nomeUsu = droid.dialogGetInput("Como devo lhe chamar? ", "Insira seu nome").result

            while self.nomeIa is None:
                self.nomeIa = droid.dialogGetInput("Nome da IA", "Insira um nome").result

            os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o caminho da pasta da IA
            caminho = os.getcwd() + "/infos.txt"  # Monta o caminho do txt das informações

            arq = open(caminho, 'w')
            arq.writelines(self.nomeUsu + "\n" + self.nomeIa + "\n" + "1 \n")
            arq.close()

        cronos = Cronos()
        saudacao_gerada = str(cronos.tempo()[0] + " " + self.nomeUsu)  # Saudação: Periodo do dia + Nome do usuário
        time.sleep(1)  # Um leve delay para o carregamento dos arquivos

        return saudacao_gerada

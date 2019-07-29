#!/usr/bin/env python
#-*-coding:utf8;-*-
# Junior Obom 26/12/17
# Classe que vai carregar informações primárias para o Assistente

import os
import time
from util import Cronos
from util import Arquivo
from androidhelper import sl4a
import androidhelper as android



class Load():
    nomeUsu,nomeIa,first="","","" #Inicializando

    def __init__(self):
        pass
    
    def carregar(self):
        arq=Arquivo() 

        if(arq.lertudo()[1]==False): # Verifica existência do arquivo
            arq.criar("/infos.txt") # Cria se não existir       
                    
        info=arq.lertudo()
        
        return info # Retorno as informações do aqruivo de inicio
    
    def iniciar(self, info): # Faz a verificações iniciais

        self.nomeUsu=info[0] # O nome do usuário é a primeria linha do txt
        self.nomeIa=info[1] # O nome da IA é a segunda linha.
        self.first=str(info[2]) # "0" se for o primeiro uso da IA e "1" se não for

        self.nomeUsu = self.nomeUsu [:-1] # Cuida do "\n" resultante de variavéis vindas a partir da leitura de arquivos txt
        self.nomeIa = self.nomeIa [:-1]
                
        
        if (("0"in self.first) or ("Obom" in self.nomeUsu)) : # Se for o primeiro acesso
            droid = sl4a.Android()
            self.nomeUsu=droid.dialogGetInput("Como devo lhe chamar? ","Insira seu nome").result
            self.nomeIa=droid.dialogGetInput("Nome da IA","Insira um nome").result

            os.chdir(os.path.dirname(os.path.abspath(__file__))) # Aponta para o caminho da pasta da IA
            caminho=os.getcwd()+"/infos.txt" # Monta o caminho do txt de infos
        
            arq = open(caminho, 'w')
            arq.writelines(self.nomeUsu+"\n"+self.nomeIa+"\n"+"1 \n" ) # No caso seria 1,mas para testes é 0 por enquanto 
            
            arq.close()      
        
        
        cr=Cronos() 
        sd=str(cr.tempo()[0]+" "+self.nomeUsu) # Saudação: Periodo do dia + Nome do usuário
        time.sleep(1) # Um leve delay para o carregamento dos arquivos
        
        return sd

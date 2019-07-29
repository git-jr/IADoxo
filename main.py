#-*-coding:utf8;-*-
# Junior Obom
# 26/12/17
# Classe principal, responsável por usar os recursos das demais classes e iniciar a IA



from LoadAndroid import Load
from chatbot import Chatbot
from util import Voz
from util import Log



v=Voz()
lg=Log() 
ld=Load()
ch=Chatbot()

info=ld.carregar() # Carregando o arquivo de informações iniciais


modo_texto=False
aprender=False
log=[]

if(modo_texto==False):
    v.fale(ld.iniciar(info)) # Verificando nome e primeiro acesso
else:
    ld.iniciar(info)

 
while(True):
        if(modo_texto==False):
            entrada=(v.escute())
        else:
            entrada=input(str("%s: "%(ld.nomeUsu))) 
        
        saida=ch.interagir(entrada, lg.listar())
        
                         
        if(modo_texto==False) : 
            print(ld.nomeUsu,": ",entrada)
            v.fale(saida[0])
        print(ld.nomeIa,": ",saida[0])
        
        lg.reg(entrada, saida[0]) # Registra log 
            
        if (saida[1]==False and aprender==True): # Cadastrar uma resposta se não existir
            if(modo_texto==False):
                ch.aprender1(entrada)
            else:
                ch.aprenderTxt1(entrada) 
           

        
        


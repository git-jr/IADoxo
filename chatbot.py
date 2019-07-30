#-*-coding:utf8;-*-
# Junior Obom 
# 04/01/2018

# Classe responsável por receber entrada, fazer processamentos, identificações e devolver saídas correspondentes


from util import Voz
from util import Arquivo
from paciencia import Paciencia
from Classificador import Classificador
from BuscaWeb import BuscaWeb

class Chatbot():
    entradasrecentes=[]

    def __init__(self):
        pass

    def interagir(self, entrada, log=[] ): # Recebe uma string, busca no txt e se houver uma resposta devolve
       
        cl=Classificador()
        entrada=cl.normalizar(entrada) # Normalizando a entrada, por enquanto isso apenas deixa tudo em minúsculo

        resposta = "Infelizmente não tenho nenhuma resposta para isso" 

	   
        if("pare" == entrada or "sair" in entrada): exit() # Força a parada do app logo de cara se necessário

        # É verificado se a reposta é idêntica as últimas e qual ação tomar a partir dali através do módulo impaciência. 
        paciencia=Paciencia() 
        resp=paciencia.ent_rep(self.entradasrecentes,entrada)
        if(resp[1]==True): # Se a paciência já passou do limite 
            self.entradasrecentes=[]
            return resp # Reposta já está no formatado de trabalho da classe principal
        self.entradasrecentes.append(entrada) 


        # Deixa mais dinâmico no futuro essa parte sobre repetir a última coisa falada
        repita=["repita", "repete", "o que você disse", "repete por favor"]
        
        for r in repita:
            if(r==entrada and len(log)!=0): # Se o usuário quiser saber sua última resposta e ela existir
                
                return log[len(log)-1][1],True
            
        # É feito uma busca rápida por ações
        numop=cl.idacao(entrada)
        if(numop[0]!=0): # Se existir uma ação para ser executada:   
            resp=cl.execacao(entrada,numop)
            if(resp[0]!=0):
                return resp,True
                     
        
        # Se chegar até aqui sem uma reposta, é hora de buscar no banco
        arq=Arquivo()

        if((arq.lertudo("/BD/txt/i.txt")[1]==False) or (arq.lertudo("/BD/txt/o.txt")[1]==False)): # Verifica existência do arquivo              
            arq.criar("/BD/txt/i.txt")# Cria se não existir 
            arq.criar("/BD/txt/o.txt")

        inputs=arq.lertudo("/BD/txt/i.txt") # lista de possíveis entradas
        outputs=arq.lertudo("/BD/txt/o.txt") # lista de possíveis saídas
        
        
        n=0 # Setando
        for i in inputs: # Busca nos arquivos
            
            if(entrada+"\n"==i): # O "\n" é para igualar as quebras linha do txt
                resposta=outputs[n]              
                return resposta,True
            n+=1


        # Se a resposta não foi econtrada até agora, vamos tentar buscar na internet
        cb = BuscaWeb()
        resultado = cb.start(entrada)
        if(resultado[1]):
            return resultado # Reposta já está no formatado de trabalho da classe principal
            
		
		
        # Caso nenhuma resposta tenha sido atribuída
        return resposta,False 

    
    def aprender1(self, entrada): # Responsável apenas por cadastrar uma saida para entrada
        v=Voz() 
        cl=Classificador()
        
        v.fale("Quer Cadastrar uma agora?")
        saida=(v.escute())     
        saida=cl.normalizar(saida) 
                
        sim=["sim", "claro", "com certeza", "óbvio que sim","por favor", "correto", "certo", "isso mesmo", "pode pá" ] 
        
        for i in sim:
            if(saida in i):
                while(True): #Looping infinito que só é encerrado quando uma entrada é gravada
                    v.fale("Qual a resposta?")
                    saida=(v.escute())
                    
                
                    v.fale("Então a sua entrada é:, "+entrada)
                    v.fale("E a saída é:, "+saida)
                    v.fale("Correto?") 
                    resp=(v.escute())
                
                    for i in sim:
                        if(resp in i):
                            v.fale("Ok, gravando resposta") 
                       
                            entrada=cl.normalizar(entrada) # Normalizando a entrada, por enquanto isso apenas deixa tudo em minúsculo
                            saida=cl.normalizar(saida)
                           
                            arq=Arquivo() 
                            arq.gravar("/BD/txt/i.txt",entrada)
                            arq.gravar("/BD/txt/o.txt",saida)
                               
                            return
                
                    # Mas caso o usuário diga qualquer outra coisa, reiniciar... 
                    v.fale("Você pode repitir por favor?")
                    v.fale("Qual é a pergunta?") 
                    entrada=(v.escute())
        
        
        v.fale("Ok, fica para próxima") 
        return # Saia caso o usuário não queria cadastrar uma resposta

    # Reutilizar a função anterior depois, mas por hora
    def aprenderTxt1(self, entrada): # Responsável apenas por cadastrar uma saida para entrada através do modo texto
        v=Voz() 
        cl=Classificador()
        
        saida = input("Quer Cadastrar uma agora?: ")         
        saida=cl.normalizar(saida) 
                
        sim=["sim", "claro", "com certeza", "óbvio que sim","por favor", "correto", "certo", "isso mesmo", "pode pá" ] 
        
        for i in sim:
            if(saida in i):
                while(True): #Looping infinito que só é encerrado quando uma entrada é gravada
                    saida=input("Qual a resposta?: ")
                    
                    saida=cl.normalizar(saida) 
                    
                
                    print("Então a sua entrada é: "+entrada)
                    print("E a saída é: "+saida)
                     
                    resp=input("Correto?: ") 
                
                    for i in sim:
                        if(resp in i):
                            print("Ok, gravando resposta") 
                       
                            entrada=cl.normalizar(entrada) # Normalizando a entrada, por enquanto isso apenas deixa tudo em minúsculo
                            saida=cl.normalizar(saida)
                           
                            arq=Arquivo() 
                            arq.gravar("/BD/txt/i.txt",entrada)
                            arq.gravar("/BD/txt/o.txt",saida)
                               
                            return
                
                    # Mas caso o usuário diga qualquer outra coisa, reiniciar... 
                    print("Você pode repitir por favor?")
                    entrada=input("Qual é a pergunta?") 
                    
        
        
        print("Ok, fica para próxima") 
        return # Saia caso o usuário não queria cadastrar uma re

# Paciência assim como outros estados vão compor um estado emocional totalizando 100%
import random as r

class Paciencia():
    paciencia="" # Setando nível de paciência
    
    def __init__(self):
        self.paciencia=r.randrange(2,5) # 20-01-18 Quantas vezes uma mesma reposta vai poder ser recebida seguidamente sem nenhuma ação por parte do chatbot. Todo reinicio da ia esse número muda.
        
    def ent_rep(self,lista_entradas,entrada_atual): # Entradas repetidas, verifica se o número de entradas iguais já excedeu o limite (paciencia) 
        if(lista_entradas.count(entrada_atual)>=self.paciencia) : # Se o tamanho da lista for igual a número de elementos idênticos nela faça:
            
            ordinal=["0","primeira", "segunda", "terceira", "quarta", "quinta"] 
            
            p = self.paciencia # Pra ficar mais fácil de trabalhar a seguir 
            
            saidas=["parece que alguém está com mau de Alzheimer", 
            	"você sabe que ja falou isso umas %d vezes né?"%(p), 
            	"porque você insiste em se repetir?", 
            	"sabe, fazer a mesma coisa sempre esperando resultados diferentes, é controverso", 
            	"então você acha que se repetir muda algo?", 
            	"essa é a %s vez que você diz isso" %ordinal[p], 
            	"não se cansa de repetir a mesma coisa? ", 
            	"%s vez que você fala a mesma coisa, tem mesmo certeza disso não é" %ordinal[p] 
            ]
                       
            saida=r.choice(saidas) 
            return saida, True
        
        return "Paciência ok", False
"""
i = Paciencia()
print("Level:", i.paciencia)
print(i.ent_rep(["5", "5", "5","5"],"5"))
"""
#-*-coding:utf8;-*-
# Junior Obom
# 07/01/2018
# Classificador de palavras, deve ser capaz de:
# Normalizar palavras: Deixar palavrasem minúsculo para fácil análise
# Separar palavras
# Conter um método que possar receber uma lista de frase/classe e ser treinado semelhante ao que encontramos no TextBlob porém funcional no Android
                                             
                                             
import random
import util


class Classificador(object):
    def __init__(self):
        pass
    
    def fatiar(self,frase): # Recebe uma frase e devolve uma lista com cada palavra sendo um elemento de uma lista
        palavras=frase.split(" ")
        return palavras


    def normalizar(self,frase): # Deixa palavras em minúsculo
        frase=frase.lower()
        return frase

    def aprende(self,listadetreino): #
        listadetreino
             
                
    def analisarresp(self,entrada):
        # Deve identificar uma tendência do usuário baseado em 5 Categorias:
        # - Respostas Afirmativas
        # - Respostas Negativas
        # - Tendência a um "não" (incentiva-lo a um não completo)
        # - Tendência a um "sim" (incentiva-lo a um sim completo)
        # - Incerteza (incentiva-lo a escolher um lado)
        # Uma resposta que seja indecisa mas aponte pra um sim, pode influenciar o bot a dizer um "vai, eu sei que vc quer"
        # Já uma que tenda para não, pode significar um "é melhor você pensar melhor sobre isso"

        

        resp_afir=["yes", "sim", "claro","claro que sim", "com certeza", "afirmativo", "pode crer", "agora","óbvio que sim","por favor","correto", "certo", "isso mesmo", "pode pá"]
        resp_nega=["not","não","claro que não", "nem pensar", "com certeza não","nunca", "negativo","nunca","jamais","errado","incorreto"]

        resp_duv=["não sei","talvez","pode ser","talvez sim","talvez não","incerto"] 

        resp_duva=["pode ser","talvez sim","provavelmente","é provável"] # Com maior probabilidade de sim
        resp_duvn=["acho que não","talvez não","provavelmente não","é provável que não","melhor não"] # Com maior probabilidade de não

 
        # Vamos usar o sistema de potução que elege a melhor resposta
        # Usar algum cálculo para tornar as procentagens parte de 100% no fim
        # Da pra fazer com regra de três
        ra=0 #%
        rn=0 #%
        rdv=0 #%
        rdva=0 #%
        rdvn=0 #%
        
        for resp in resp_afir:
            if (entrada==resp): # Verifica se exatamente igual
                ra=100
                break
            if (entrada in resp or resp in entrada): # Verifica se está contida
                ra+=1 # Pontua como mais provavel
                
        for resp in resp_nega:
            if (entrada==resp):
                rn=100
                break
            if (entrada in resp or resp in entrada):
                rn+=1 
                
        for resp in resp_duv:
            if (entrada==resp): 
                rdv=100
                break
            if (entrada in resp or resp in entrada): 
                rdv+=1
                
        for resp in resp_duva:
            if (entrada==resp):
                rn=100
                break
            if (entrada in resp or resp in entrada): 
                rdva+=1 

        for resp in resp_duvn:
            if entrada==resp: 
                rdva=100
                break
            if (entrada in resp or resp in entrada):
                rdvn+=1 

        total=ra+rn+rdv+rdva+rdvn # Vamos usar regra de três para normalizar os dados

        if ra != 0: ra=ra*100/total
        if rn != 0: rn=rn*100/total
        if rdv != 0: rdv=rdv*100/total
        if rdva != 0: rdva=rdva*100/total
        if rdvn != 0: rdvn=rdvn*100/total

        prob={"Afirmativa:":ra,"Negativa:":rn,"Talvez:":rdv,"Talvez sim:":rdva,"Talvez não:":rdvn}
        
        for i in sorted(prob, key = prob.get,reverse=True):
            print (i,prob[i])
        return
    
    nome_cat=[] # Por enquanto não vamos gravar em TXT, mas isso perite armazenar várias listas enquanto o programa estiver rodando
    categorias=[]



    def treinar(self,listadetreino): # "l" é qual lista de treino deve ser testada

        # 1º Separar categorias
        # Salvar em txt se 
        # Salvar em TXT para ler e interpretar depois

        nome_cat=[]
        categorias=[]

        j=0
        for i in range(len(listadetreino)): # Nomeia as categorias
            if ((listadetreino[j][0] in nome_cat) == False):
                categorias.append([])
                nome_cat.append(listadetreino[j][0])
            j+=1

        j=0 # Setando novamente
        for i in range(len(listadetreino)): # Separa as categorias
            for h in nome_cat:
                if (listadetreino[j][0]==h):
                    categorias[nome_cat.index(h)]=listadetreino[j][1]
            j+=1

        self.nome_cat=nome_cat # Passando para os atributos globais da classe para que o método "testartreino" possa fazer uso
        self.categorias=categorias

        # 19-01-18
        # OK: Separação de nome categorias
        # OK: Separação de categorias

        return
        
        
    def testartreino(self,entrada,literal=True):

        k=0
        resultado=[]
        corre100=False # Uma correspondênica 100% deve para todos os ciclos para poupar processamento

        for i in self.nome_cat: # Ao invés de usar 5 "for" como antes
            for resp in self.categorias[self.nome_cat.index(i)]:
                if (entrada==resp): # Verifica se exatamente igual
                    for a in range(100): # Esse ciclo DEVE garantir que a resposta exata seja a de mairo número para os cálculos finais
                        resultado.append(i) # Adicionando várias vezes
                    corre100=True
                    break  # Isso pode acabar bugando ciclo, ficar esperto 

                if (literal==False): # Caso as buscas necessitem de grande precisão
                    if (entrada in resp or resp in entrada):
                        resultado.append(i)
                else: # Caso as buscas não necessitem de grande precisão
                    if(entrada in resp): # Ou para resultados mais interessantes e bugados: if (entrada in resp or resp in entrada):
                        resultado.append(i) # Para contabilizar no final dos resultados



            if(corre100==True):
                #print("Correspondência 100% identificada")
                break # Para quebrar o segundo ciclo caso uma correspondênica 100% seja encontrada
                 

        total=0
        pontoscatego=[] # Contabilizando
        for i in self.nome_cat:
            pontoscatego.append([i,resultado.count(i)])
            total+=resultado.count(i)


        for i in pontoscatego: # Usando regra de três para normalizar os dados a um total de 100%
            if (i[1] != 0):
                pontoscatego[pontoscatego.index(i)][1]=i[1]*100/total

        
        pontoscatego.sort(key=lambda x: x[1], reverse=True) # Organaiza do maior para o menor

        #for i in pontoscatego: # Exibi
        #    print(i)

        saida=pontoscatego[0]

        if (saida[1]==0):
            saida= False
        return saida

    def conta(self,entrada): # Verifica se a entrada recebida contém alguma conta matmática a ser realizada.
        conta=False # Se exitir algua operação a ser realizada isso muda
        operacao=[["+","mais"],["-","menos"],["*","x","vezes","multiplicado por"],["/","dividido por"]]

        
        for sinal in operacao:
            for i in sinal:
                if i in entrada:
                    posiope=entrada.index(i) # Posição do sinal apra ajudar a indentficar os números da operação
                    tamposiope=len(i)
                    

                    k=2 # Já desconsiderando o sinal em si e o espaço entre ele e o número
                    while (posiope-k>=0): # Vamos achar o primeiro número da operação
                        # Vamos fazer isso usando intervalos de String
                        
                       
                        try:
                            x=int(entrada[posiope-k]) # Se conseguir é pq é um número
                             
                        except:
                            try:
                                num1=int(entrada[(posiope-k):posiope-1])
                                
                                break # Quando não ouver mais números pare

                            except: # Evita que palavras como "mais" fora de contextto bug o programa
                                #print("Nenhuma operação a ser realizada")
                                return False
                        
                        if(posiope-k==0):
                            num1=int(entrada[(posiope-k):posiope-1])
                            
                            break # Quando não ouver mais números pare

                       
                        k+=1

                    # Pra poder achar o segundo número, antes vamos ter que achar o final do sinal da operção já que ele pode ser algo enttre 1 e 7 caracters( "dividio" tem 7)

                    k=tamposiope+2 # Já desconsiderando o tamanho do sinal em si e o espaço entre ele e o número


                    while (True and k<=len(entrada)): # Vamos achar o segundo número da operação
                        try:
                            x=int(entrada[posiope+k]) 

                        except:
                            num2=int(entrada[posiope+tamposiope+1:(posiope+k)])
                            break
                            
                        k+=1
                    
                    #print("O primeiro número é:",num1)
                    #print("O segundo número é:",num2)

                    resultado=0

                    while (True):
                        if (i=="+") or (i=="mais"):
                            resultado=(str(num1)+" mais "+str(num2)+" é igual a "+str(num1+num2))                         
                            break
                        
                        if (i=="-") or (i=="menos"):
                            resultado=(str(num1)+" menos "+str(num2)+" é igual a "+str(num1-num2))      
                            break
                        
                        if (i=="x") or (i=="vezes") or (i=="multiplicado por"):
                            resultado=(str(num1)+" vezes "+str(num2)+" é igual a "+str(num1*num2))
                            break
                        
                        if (i=="/" or "dividido por"):
                            resultado=(str(num1)+" dividido por "+str(num2)+" é igual a "+str(num1/num2))
                            break

                    #print("Resultado:",len(resultado)) 
                    return resultado
        
        
        #print("Nenhuma operação a ser realizada")
        return False

    def idacao(self,entrada): # Verifica se existi alguma ação no texto passado como entrada 

        if(self.conta(entrada)!=False): # Verifica se a ação é uma conta
            saida=self.conta(entrada)    
            return 1, saida # Resultado mais número da opção para uso futuro            
            

            
        else:
            hora=["2 Saber horas",["que horas são", "que hora é agora", "horas por favor","me diga as horas"]]
            
            data=["3 Saber data",["que dia é hoje", "qual a data de hoje","data de hoje"]]
        
            fecharIa=["4 Fechar App da IA",["sair", "encerrar", "fechar programa", "cessar funções motoras"]]  
  
            abrirapp=["5 Abrir um aplicativo",["abrir aplicativo","abrir app","iniciar app","iniciar aplicativo","abrir"]]

            tocarmusica=["6 Reproduzir música",["tocar música", "toque a música", "reproduzir música", "toque uma música", "tocar", "toque", "reproduzir" ]] 
            

            listadetreino1=[fecharIa]
            listadetreino2=[hora,data,fecharIa,abrirapp,tocarmusica]
            

            self.treinar(listadetreino1) # Ações que requerem saida ao pé da letra
            saida=self.testartreino(entrada)

            
            if (saida==False):
                #print("Nenhuma ação ao pé da letra detectada")

                self.treinar(listadetreino2) # Ações que não requerem saida ao pé da letra
                saida=self.testartreino(entrada,False)

                if (saida==False):
                    #print("Nenhuma ação detectada")
                    saida=0,"Nenhuma ação"
               
                else: # Se identificar a ação
                    saida=(int(self.testartreino(entrada,False)[0][0]), True) # Pega apenas o número da op
               
        return saida

    def execacao(self,entrada,na): # Recebe a entrada para trabalhar com ela e o Número da Ação que deve ser executada
        saida=0,False # Setando a saída para o caso de nenhuma ação ser correspondente
        
        if (na[0]==1): # Contas
            saida=str(na[1])
            return saida
            
        if(na[0]==2): # Horas
            cr=util.Cronos() 
            saida=str("São "+str(cr.tempo()[1])+" e "+str(cr.tempo()[2])) # Saudação: Periodo do dia + Nome do usuário        
            return saida
            
        if(na[0]==3): # Datas
            cr=util.Cronos()
            t=cr.tempo()
            saida=str("Hoje é dia "+str(t[3]) +" de "+str(t[4]) +" de "+str(t[5])) # Saudação: Periodo do dia + Nome do usuário
            return saida

        if(na[0]==4): # Excerrar IA
            v=util.Voz() 
            v.fale("Programa encerrado")
            print("Programa encerrado")
            exit()
            
        if(na[0]==5): # Abrir Apps
            
            a=util.Apps() 
            a.listarapps()
            listaapp=a.listaapps
                
            for i in listaapp:
                #print(i[0])
                if(i[0] in entrada): # Se o nome de algum app estiver na entrada
                    saida=a.abrirapp(i[0])
                    return saida

            for i in listaapp: # Mesmo se nome do app não estiver na extrada, vamos buscar por parte do nome dele
                j=self.fatiar(i[0])                   
                for k in j:
                    if(k in entrada):
                        saida=a.abrirapp(k)
        
        if(na[0]==6): # Tocar músicas              return saida
            chaves=["tocar música", "toque a música", "reproduzir música", "toque uma música", "tocar", "toque", "reproduzir" ]# Notar que as possibilidades de maior tamanho devem ficar em primeiro para facilitar a precisão em buscas com ciclo for
            
            ms=util.Musicas()
            musicas=ms.nomemusicas

            for chave in chaves:
                if chave in entrada:
                    if (chave=="toque uma música"): #Se a música a ser tocada for uma aleatória
                        musica=random.choice(musicas)
                        
                    else: # Se não, vamos considerar que tudo no sentido da esquera pra direita deve ser o nome da música
                        musica=entrada[entrada.index(chave)+len(chave)+1:len(entrada)]

                    musica=ms.locmusica(musica)
                    if(musica[1] != False): # Se a música existir
                        saida=ms.tocarmusica(musica[0])[0]
                        return saida
                    else:
                        saida=musica[0]                        
                        return saida                                        
        return saida


resp_afir=["Respostas Afirmativas",["yes", "sim", "claro","claro que sim", "com certeza", "afirmativo", "pode crer", "agora","óbvio que sim","por favor","correto", "certo", "isso mesmo", "pode pá","obviamente"]]
resp_nega=["Respostas Negativas",["not","não","claro que não", "nem pensar", "com certeza não","nunca", "negativo","nunca","jamais","errado","incorreto"]]
resp_duv=["Em dúvida",["não sei","talvez","pode ser","talvez sim","talvez não","incerto"]] 
resp_duva=["Provavelmente sim",["pode ser","talvez sim","provavelmente","é provável"]] # Com maior probabilidade de sim
resp_duvn=["Provavelmente não",["acho que não","talvez não","provavelmente não","é provável que não","melhor não"]] # Com maior probabilidade de não

listadetreino=[resp_afir,resp_nega,resp_duv,resp_duva,resp_duvn]


#cl=Classificador()

#cl.treinar(listadetreino)
#cl.testartreino("mas é claro que sim")
#print(cl.analisarresp("provavelmente sim")) 
#print(cl.conta("3 multiplicado por 7") )
#print(cl.idacao("que dia é hoje"))

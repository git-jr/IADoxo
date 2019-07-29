#-*-coding:utf8;-*-
# Junior Obom
# 28/06/2018
# Classe responsável por receber uma frase ou palavra e realizar
# uma busca na internet, mais precisamente utilizando o Google.
# O o site de busca pode ser modificado e adaptado no futuro para outras aplicações


import urllib.request
from unicodedata import normalize

import urllib.parse
import urllib.request

class BuscaWeb(object):
    def __init__(self):
        pass

    def gerarUrl(self,chave): # Recebe uma palavara ou frase chave e a prepara para busca
        textoBusca = chave.replace(" ","+") # No lugar dos espaços vamos colocar sinais de adição "+" pois é assim que a url de busca do google deve ser montada
        
        url = str("https://www.google.com.br/search?q="+textoBusca)
        #print(url)
        return url
    
    def busca(self,url): # Faz uma busca com a URL e devolve o HTML da página
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0','Accept-Charset':'utf-8'}  

        req = urllib.request.Request(url, headers = headers)   
        retorno = urllib.request.urlopen(req).read()
        retorno = str(retorno.decode('utf-8','ignore'))
        
        
        return retorno

    def remover_acentos(self,txt, codif='utf-8'):
        txt=txt.encode('utf-8') # Para usar o "decode" em uma str é preciso fazer isso antes
        semAce = str(normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore'))   
        semAce=semAce[2:len(semAce)-1] # Tirando os dois primeiros caracteres para que a string seja correspondente com a original
        print(semAce) 
        return semAce

    def responder(self,html): # Vai devolver qual o tipo da pesquisa e a resposta

        codTipos = ["""class="Z0LcW">""",
            """data-dobid="dfn"><span>""",
            """class="vk_gy vk_sh">""",
                      
            """class="ILfuVd yZ8quc c3biWd">""", # Essa ordem é importante
            """class="ILfuVd yZ8quc">""",

            """id="knowledge-currency__tgt-amount">""",
            """class="cwcot" id="cwos">""",
            """id="tw-target-text" style="text-align:left"><span>"""]
        
        tipos = ["quem é ou data de",
            "significado",
            "que dia é",

            "descobrimento 2",
            "descobriento 1",
                
            "dolar",
            "calcular",
            "tradução"]

        resposta = "nenhum resultado"
        tipoCorte = None
        for ct in codTipos:
            if(ct in html):
                if (tipos[codTipos.index(ct)] == "que dia é"):
                    if( """class="dDoNo vk_bk">""" in html):                        
                        ct2 = """class="dDoNo vk_bk">""" # Dolar
                       
                        break
                ct2 = ct
                break
            
        try: 
            html = html[(html.index(ct2)+len(ct2)):len(html)] # Tudo que vier antes
            html = html.replace("<b>","") # Texto enfáticos que poderiam atrapalhar o próximo racioncínio
            html = html.replace("</b>","") # Texto enfáticos que poderiam atrapalhar o próximo racioncínio

            resposta = html[0:html.index("<")] # Tudo que vier depois                 

        finally: # Caso haja algum possível erro na busca
            
            return resposta

    def start(self,busca):
        try:
            cb = BuscaWeb()
            url = cb.gerarUrl(cb.remover_acentos(busca))
            resultado = cb.responder(cb.busca(url))

            if (resultado == "nenhum resultado"):
                return resultado,False
            else:
                resultado = str(resultado)              
                return resultado, True
        except:
            resultado = "não foi possivel concluir a busca"
            return resultado, False
            
                   
"""
# Uso
cb = BuscaWeb()
resultado = cb.start("dolar")
print(resultado[0])
"""










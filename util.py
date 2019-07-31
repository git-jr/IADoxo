# -*-coding:utf8;-*-
# Junior Obom 26/12/17
# Classe fornecedora de recursos uteis

import os
import time
import glob
from androidhelper import sl4a
import androidhelper as android
from classificador import Classificador

droid = android.Android()


class Apps(object):
    # Classe resposnável por:
    # Listar todos aplicativos do dispositivo;
    # Identificar um app através de uma entrada( nome ou parte do app ) 
    # Executar o app identificado

    listaapps = []
    pacotes = ""

    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o arquivo atual
    os.chdir("..")
    os.chdir("..")  # Sobe para o diretório raiz do dispositivo
    os.chdir(os.getcwd() + "/Android/data")  # Pasta onde ficam localizados os nomes dos pacotes
    pacotes = sorted(os.listdir())

    def __init__(self):
        pass

    def listarapps(self):  # Lista todos aplicativos do dispositivo no formato App/Atividade Principal/ Nome do pacote
        apps = droid.getLaunchableApplications()  # Obtém a lista das ativiades e nome dos apps

        # Como não estamos trabalhando diretamente com Java não é possivel usar "getpackagemanager" para o obeter o nome dos pacotes, por isso é preciso muito mais código para conseguir um resultado semelhante
        listaapps = []

        for i in apps[1]:  # Ciclo que organiza as coisas
            cl = Classificador()
            nomeapp = cl.normalizar(
                i)  # O nome do app deve ficar em minúsculo para agilizar comparações futuramente
            atividade = apps[1][i]

            listaapps.append([nomeapp, atividade])

        self.listaapps = sorted(listaapps)  # A variável global recebe a local só que organizada em ordem alfabética

        lapps = self.listaapps
        lpacotes = self.pacotes

        for j in lapps:  # Ciclo para adicionar os pacotes que foram listados no instaciamento da classe
            for i in lpacotes:
                if (i in j[1]):
                    self.listaapps[self.listaapps.index(j)].append(
                        i)  # O app correspondente recebe o nome do pacote agora
                    lpacotes.pop(lpacotes.index(
                        i))  # Retira o pacote para não acabar sendo associado a outro app

        self.listaapps = lapps  # Adicionando á variavél global

        # A lista a seguir é o conjunto de nomes de pacotes que não puderam ser identificados pelo código e vão ter que ser adicionados manualmente 
        listanegra = [["com.google.android.apps.youtube.creator", "yt studio"],
                      ["com.socialnmobile.dictapps.notepad.color.note", "colornote"],
                      ["com.cyberlink.powerdirector.DRA140225_01", "powerdirector"],
                      ["com.estrongs.android.pop.pro", "es file explorer pro"],
                      ["com.iudesk.android.photo.editor", "editor de fotos"],
                      ["com.zeptolab.thieves.google", "king of thieves"],
                      ["com.touchtype.swiftkey", "teclado swiftKey"],
                      ["com.google.android.videos", "play filmes"],
                      ["com.google.android.music", "play música"],
                      ["com.google.android.youtube", "youtube"],
                      ["com.google.android.apps.maps", "maps"],
                      ["pl.solidexplorer2", "solid explorer"]]

        for i in listanegra:  # Vamos adicionar o nome dos pacotes da lista negra a lista global de apps
            for j in self.listaapps:
                if i[1] == j[0]:  # Se tiver o mesmo nome, adicionar o nome do pacote a lista
                    self.listaapps[self.listaapps.index(j)].append(i[0])

        return

    def abrirapp(self, appsele):
        saida = "Nenhum aplicativo correspondente foi encontrado"

        apps = self.listaapps

        for i in apps:  # Ciclo para achar a atividade principal do aplicativo selecionado
            if (appsele in i[0]) or (i[
                                         0] in appsele):  # Mesmo se a pessoa não falar o nome do app completo deve funcionar

                if (len(i) == 2):  # Para os apps que não foi possível carregar o pacote
                    droid.launch(i[1])
                else:  # Para os apps que foi possível carregar pacotes carregados
                    droid.startActivity('android.intent.action.MAIN', None, None, None, False, i[2], i[1])

                saida = ("Abrindo " + i[0])
                break

        return saida


class Arquivo(object):

    def __init__(self):
        pass

    def criar(self, nomearquivo, texto="Junior\nAIA\n0\n"):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o caminho da pasta da IA
        caminho = os.getcwd()
        arq = open(caminho + nomearquivo, "w+")
        arq.writelines(texto)  # Algo padrão nos arquivos
        arq.close()

    def lertudo(self, complemento="/infos.txt"):  # Usando parâmetros default mutáveis para aumentar reutilização

        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o caminho da pasta da IA
        caminho = os.getcwd() + complemento  # Monta o Caminho Completo

        try:
            arq = open(caminho, 'r')
        except:
            # print("Arquivo não existe")
            return ["Arquivo não existe", False]

        info = arq.readlines()
        arq.close()

        return info  # Retorno as informações do aqruivo de inicio

    def gravar(self, caminho, texto):  # Parte 1 do Crud

        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o caminho da pasta da IA
        cc = os.getcwd() + caminho  # Monta o Caminho Completo

        arq = open(cc, 'r+')
        arq.readlines()  # Movendo o ponteiro de gravação para última linha
        arq.write(texto + "\n")  # Gravando no fim do arquivo

        arq.close()  # Fecha o arquivo para evitar bugs


class Cronos(object):

    def __init__(self):
        pass

    def tempo(self):
        t = time.localtime()
        hora = t[3]

        periodo = "Boa noite"
        if (hora > 0 and hora <= 4): periodo = "Boa madrugada"
        if (hora > 4 and hora < 12): periodo = "Bom dia"
        if (hora >= 12 and hora < 18): periodo = "Boa tarde"

        # O mês está como número, vamos fazer para adicionar seu nome também
        meses = ["Só pra usar o índice 0", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Julho",
                 "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        tempo = [periodo, t[3], t[4], t[2], meses[t[1]], t[0]]  # Periodo do dia, hora, minuto, dia, mês, ano
        return tempo


class Log(object):
    listaLogs = []  # Lista geral dos logs

    def __init__(self):
        pass

    def reg(self, entrada, saida):  # Registra um log padrão com entrada, saída e tempo
        cr = Cronos()
        agora = cr.tempo()

        log = [entrada, saida, agora]

        self.listaLogs.append(log)

        return True

    def listar(self):
        return self.listaLogs

    # Adicionar logs mais avançados que gravem o tipo da interação como "aprendizado", "conversa", "abrir app" 


class Musicas(object):
    # 07/02/2018
    # Classe resposnável por:
    # Listar todos aqruivos mp3 do dispositivo (memória ienterna e externa);
    # Identificar uma música através de uma entrada ( parte do titulo do arquivo mp3 ) 
    # Executar o música identificada
    # Controle da música em repodução:
    # Parar: Colocar brilho aparelho no máximo
    # Pausar/ Despausar: Diminuir brilho no mínimo

    listamusicas = []  # Vai armazenar as músicas e seus respectivos caminhos
    nomemusicas = []  # Vai armazenar apenas o nome das músicas

    def __init__(self):
        self.locext()
        self.locint()

    def listar(self, diretorio_usuario, diretorio):  # Função recursiva
        if os.path.isdir(diretorio_usuario + diretorio):
            os.chdir(diretorio_usuario + diretorio)
            for arquivo in glob.glob("*.mp3"):
                if os.path.isdir(diretorio_usuario + diretorio + arquivo):
                    self.listar(diretorio_usuario, diretorio + arquivo + '/')


                else:
                    # print ('arquivo: '+diretorio_usuario+diretorio+arquivo)
                    caminho = str(diretorio_usuario + diretorio + arquivo)
                    self.listamusicas.append(caminho)
                    self.nomemusicas.append(arquivo.lower())
        else:
            print('arquivo: ' + diretorio_usuario + diretorio)

    def tdp(self, caminho):  # Retorna todas as pastas de um arquivo
        try:
            pastas = next(os.walk(caminho))[1]  # Lista apenas pastas do diretório
            return pastas
        except:
            return None

    def tda(self, caminho):  # Retorna todas as pastas de um arquivo
        try:
            arquivos = next(os.walk(caminho))[2]  # Lista apenas arquivos do diretório
            return arquivos
        except:
            return None

    def locint(self):  # Primeiro na memória interna
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o arquivo atual
        os.chdir(
            "..")  # Sobe para o diretório raiz do dispositivo # Pasta onde ficam localizados os nomes dos pacotes
        os.chdir("..")

        x = os.getcwd()
        diretorio_usuario = x + "/"

        musicsd = self.tda(os.getcwd())

        if musicsd != None:
            for i in musicsd:
                if ".mp3" in i:
                    musica = diretorio_usuario + i
                    self.listamusicas.append(musica)

        for i in self.tdp(x):
            diretorio = i + "/"
            self.listar(diretorio_usuario, diretorio)

    def locext(self):  # Agora na memória externa
        os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Aponta para o arquivo atual

        for i in range(4):
            os.chdir(
                "..")  # Sobe para o diretório raiz do dispositivo # Pasta onde ficam localizados os nomes dos pacotes

        pasext = os.listdir()  # Pastas externas, provavelmente o SD está aqui
        raiz = os.getcwd()  # Raiz

        for i in pasext:
            z = raiz + "/" + i + "/"
            os.chdir(z)  # Das pastas externas

            pastas = self.tdp(os.getcwd())  # Pastas da primeira pasta externa

            if pastas == None: break
            for j in pastas:
                j = j + "/"

                listar(z, j)

    def locmusica(self,
                  musica):  # Busca uma música em todos os arquivos do dispositivo e se ela existir, retorna seu caminho
        saida = "Nenhuma música correspondente encontrada", False

        for i in self.listamusicas:
            k = i.lower()  # Normalizando a entrada, por enquanto isso apenas deixa tudo em minúsculo
            if (musica in k):
                return i, True
        return saida

    def tocarmusica(self, caminhomusica):

        droid.mediaPlay(caminhomusica)

        print("\nReproduzindo " + caminhomusica)
        print("\nAumente o brilho da tela no máximo para parar a reprodução")
        print("\nDiminua no mínimo para pausar/despausar")

        brilho = int(droid.getScreenBrightness()[1])  # se brilho já no máximo (255), ajustar pra 254
        bmax = 255
        bmin = 10
        pausado = False

        if brilho == 255: bmax = 254  # Se o brilha já estiver no máximo, vamos testar forçar o usuário a diminuí-lo e aumentá-lo novamente

        if brilho <= 10: bmin = brilho + 1

        brilho = 0  # Pra não bugar o ciclo while seguinte

        while (brilho != bmax):  # Para a música se o brilho for aumentado para o máximo
            brilho = int(droid.getScreenBrightness()[1])

            if (brilho <= bmin):  # Um sistema de Interruptor para identificar quando pausar ou despausar a música
                if (pausado == False):
                    droid.mediaPlayPause()
                    pausado = True
                    print("Música pausada")

                else:
                    droid.mediaPlayStart()
                    pausado = False
                    print("Reproduzindo música")

                while (droid.getScreenBrightness()[
                           1] <= bmin):  # Prende o usuário nesses lopping até tirar o brilho do mínimo
                    pass

            from time import sleep
            sleep(5)

            if (droid.mediaIsPlaying()[1] == False and pausado == False): break  # Se a música acabar, saia do ciclo

        if (droid.mediaIsPlaying()[1] == True):  # Se existir, pare
            droid.mediaPlayClose()

        return "Música encerrada", True

        # Como usar a classe

    # ms= Musicas() # Instancia
    # musica=ms.locmusica("lucky") # Retorna o caminho da música e "True" se existir, caso contrário uma mensgem informando que não e "False"
    # m=ms.nomemusicas # Retorna uma lsita de todas as músicas, mas não é algo necessáro para reprodução

    # if(musica[1] != False): # Se a música existir
    # print(ms.tocarmusica(musica[0])[0])
    # else:
    # print(musica[0])


class Voz(object):
    delay = 0.2  # Delay para impedir que uma possível saída anterior seja interpretada como entrada

    def __init__(self):
        pass

    def fale(self, texto):
        # self.delay=len(texto)
        droid = sl4a.Android()
        droid.ttsSpeak(texto)
        # time.sleep(0.095*self.delay) # Delay para impedir que uma possível saída anterior seja interpretada como entrada 

        while (droid.ttsIsSpeaking()[1]):  # Espera a fala terminar para sair
            pass

        return

    def escute(self):
        droid = android.Android()
        (id, result, error) = droid.recognizeSpeech("Fale")

        return result  # Retorna uma string com o que foi ouvido
